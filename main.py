# import statements
from datetime import datetime
import MetaTrader5 as mt5
import pandas as pd
import pandas_ta as ta
import time
import strategies

def setup():
    # package versions
    print("MetaTrader5 package author: ",mt5.__author__)
    print("MetaTrader5 package version: ",mt5.__version__)
    
    # setting
    pd.set_option('display.max_columns', 500) 
    pd.set_option('display.width', 1500)      

    # connection
    if not mt5.initialize():
        print("initialize() failed, error code =",mt5.last_error())
        quit()
    else:
        return True

def get_stochastic_values(data_frame, k=5, d=3):
    data_frame.ta.stoch(high='high', low='low', k=k, d=d, append=True)

    data_frame.rename(columns={ data_frame.columns[-1]: "red" }, inplace=True)
    data_frame.rename(columns={ data_frame.columns[-2]: "green" }, inplace=True)

    return data_frame
    

def main(symbol="GBPJPY", time_frame=mt5.TIMEFRAME_M1):
    # to get data
    data = mt5.copy_rates_from(symbol, time_frame, datetime.now(), 1440)
    mt5.shutdown()

    # for print functionality
    data_frame = pd.DataFrame(data)
    data_frame.drop('tick_volume', inplace=True, axis=1)
    data_frame.drop('spread', inplace=True, axis=1)
    data_frame.drop('real_volume', inplace=True, axis=1)
    data_frame['time']=pd.to_datetime(data_frame['time'], unit='s')

    data_frame = get_stochastic_values(data_frame)

    data_frame = strategies.strategy_01(data_frame)

    data_frame.to_csv('trade_trigger.csv', index=False)

    print("SL", len(data_frame[data_frame['SL']!=0]))
    print("TP", len(data_frame[data_frame['TP']!=0]))
    print("Total", len(data_frame))
    print(f"TP - PERCENTAGE: {(len(data_frame[data_frame['TP']!=0])/len(data_frame))*100:.2f}%")


if __name__ == '__main__':
    start_time = time.time()

    if setup():
        main()

    end_time = time.time()
    print(f"{float(end_time-start_time):.2f} sec")

