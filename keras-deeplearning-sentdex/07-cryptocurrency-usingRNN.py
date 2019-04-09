import pandas as pd 
import numpy as np 
from sklearn import preprocessing
from collections import deque
import random
df = pd.read_csv('dataset/LTC-USD.csv', names = ['time', 'low', 'high', 'open' ,'close', 'volume'], index_col=0)



SEQ_LEN = 60 
FUTURE_PERIOD_PREDICT = 3 
RATIO_TO_PREDICT = 'LTC-USD'

def classify(current, future): 
    if float(future)>float(current): 
        return 1
    else: 
        return 0 

        
def preprocess_df(df): 
    df = df.drop('future',1)
    for col in df.columns: 
        # print(col)
        if col != 'target': 
            df[col] = df[col].pct_change()
            df.dropna(inplace=True)
            df[col]= preprocessing.scale(df[col].values)
    df.dropna(inplace=True)

    sequential_data = []
    prev_days = deque(maxlen=SEQ_LEN)
    for i in df.values: 
        prev_days.append([n for n in i[:-1]]) #n is each of the columns, which exlcudes target, karena target ada yang di terakhir
        if len(prev_days) == SEQ_LEN: 
            sequential_data.append([np.array(prev_days), i[-1]])
    random.shuffle(sequential_data)
    

    buys = []
    sells = []
    for seq, target in sequential_data: 
        print('seq:', seq, 'target',target)
        if target == 0: 
            sells.append([seq, target])
        elif target == 1: 
            buys.append([seq, target])
    random.shuffle(sells)
    random.shuffle(buys)
    lower = min(len(buys), len(sells))
    
    buys = buys[:lower]
    sells = sells[:lower]
    sequential_data = buys + sells
    print(sequential_data)

    random.shuffle(sequential_data)  #acak antara buys dan sells nya biar bikin modelnya tidak bingung dengan klasifikasinya.

    X = []
    y = []
    for seq, target in sequential_data:
        print('seq: ',seq, 'target: ',target) 
        X.append(seq)
        y.append(target)
    
    return np.array(X), y

main_df = pd.DataFrame()

ratios = ['BTC-USD', 'LTC-USD', 'BCH-USD','ETH-USD']
for ratio in ratios: 
    dataset = f'dataset/{ratio}.csv'
    df = pd.read_csv(dataset, names=['time', 'low','high','open', 'close', 'volume'])

    df.rename(columns={'close':f'{ratio}_close', 'volume': f'{ratio}_volume'}, inplace=True)

    df.set_index('time', inplace=True)
    df = df[[f"{ratio}_close", f'{ratio}_volume']]

    if len(main_df)==0:
        main_df = df 
    else: 
        main_df = main_df.join(df)

main_df.fillna(method="ffill",inplace=True)
main_df.dropna(inplace=True)


main_df['future'] = main_df[f'{RATIO_TO_PREDICT}_close'].shift(-FUTURE_PERIOD_PREDICT) # shift semacam menggeser tergantung axis dan berapa step
main_df['target'] = list(map(classify, main_df[f'{RATIO_TO_PREDICT}_close'],main_df['future']))


times = sorted(main_df.index.values)
last_5_percent= times[-int(0.05*len(times))]

validation_main_df = main_df[(main_df.index >= last_5_percent)]
main_df = main_df[(main_df.index < last_5_percent)]

X_train, y_train = preprocess_df(main_df)
X_test, y_test = preprocess_df(validation_main_df)


print(f'train data: {len(X_train)} validation: {len(X_test)}')
print(f"Don't buys: {y_train.count(0)}, buys: {y_train.count(1)}")
print(f"Validation don't buys: {y_test.count(0)}, buys: {y_test.count(1)}")
