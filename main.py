import time
start_time = time.time()

from setup import *

# to get data
data = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_D1, datetime.now(), 1000)
mt5.shutdown()

# for print functionality
data_frame = pd.DataFrame(data)
data_frame['time']=pd.to_datetime(data_frame['time'], unit='s')
print(data_frame)  

end_time = time.time()
print(f"{float(end_time-start_time):.2f} sec")

