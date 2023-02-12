# import statements
from datetime import datetime
import MetaTrader5 as mt5
import pandas as pd

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
