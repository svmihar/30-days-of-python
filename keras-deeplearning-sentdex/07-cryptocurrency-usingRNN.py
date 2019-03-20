import pandas as pd 

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

main_df['future'] = main_df[f'{RATIO_TO_PREDICT}_close'].shift(-FUTURE_PERIOD_PREDICT) # shift semacam menggeser tergantung axis dan berapa step
main_df['target'] = list(map(classify, main_df[f'{RATIO_TO_PREDICT}_close'],main_df['future']))

print(main_df.head())
