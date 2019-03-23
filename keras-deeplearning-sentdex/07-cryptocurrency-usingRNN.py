import pandas as pd 
import numpy as np 
from sklearn import preprocessing
from collections import deque
import random
df = pd.read_csv('dataset/LTC-USD.csv', names = ['time', 'low', 'high', 'open' ,'close', 'volume'], index_col=0)

print(df.head())

main_df = pd.DataFrame()

ratios = ['BTC-USD', 'LTC-USD', 'BCH-USD','ETH-USD']
for ratio in ratios: 
    print(ratio)
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
print(main_df.head())

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
        if col != 'target': 
            df[col] = df[col].pct_change()
            df.dropna(inplace=True)
            df[col]= preprocessing.scale(df[col].values)
    df.dropna(inplace=True)

    sequential_data = []
    prev_days = deque(maxlen=SEQ_LEN)
    print(df.head())
    for i in df.values: 
        prev_days.append([n for n in i[:-1]]) #n is each of the columns, which exlcudes target, karena target ada yang di terakhir
        if len(prev_days) == SEQ_LEN: 
            sequential_data.append([np.array(prev_days), i[-1]])
    random.shuffle(sequential_data)
    

main_df['future'] = main_df[f'{RATIO_TO_PREDICT}_close'].shift(-FUTURE_PERIOD_PREDICT) # shift semacam menggeser tergantung axis dan berapa step
main_df['target'] = list(map(classify, main_df[f'{RATIO_TO_PREDICT}_close'],main_df['future']))

print(main_df.head())

times = sorted(main_df.index.values)
last_5_percent= times[-int(0.05*len(times))]
print(last_5_percent)

validation_main_df = main_df[(main_df.index >= last_5_percent)]
main_df = main_df[(main_df.index < last_5_percent)]

preprocess_df(main_df)

# X_train, y_train = preprocess_df(main_df)
# X_test, y_test = preprocess_df(validation_main_df)

