
def strategy_01(data_frame):
    current = data_frame
    previous = data_frame.shift(1)
    previous_previous = data_frame.shift(2)

    data_frame['sell'] = (current['high'] >= previous['high']) & (current['low'] > previous['low']) & (current['green'] > current['red']) & (previous['green'] > previous['red']) & (previous_previous['red'] > previous_previous['green']) & (current['close'] < previous['close'])
    data_frame['buy'] = (current['high'] < previous['high']) & (current['low'] <= previous['low']) & (current['green'] < current['red']) & (previous['green'] < previous['red']) & (previous_previous['red'] < previous_previous['green']) & (current['close'] > previous['close'])

    data_frame['SL'] = 0
    data_frame['TP'] = 0

    for i in range(len(data_frame)):
        if data_frame.iloc[i]['sell'] == True:
            high = data_frame.iloc[i]['high'] + 0.250
            close = data_frame.iloc[i]['close'] - 0.300
            sl = data_frame[data_frame['high']==high]
            if len(sl) > 0:
                data_frame.at[i,'SL'] = sl.iloc[0]['time']
            tp = data_frame[data_frame['close']==close]
            if len(tp) > 0:        
                data_frame.at[i,'TP'] = tp.iloc[0]['time']
        elif data_frame.iloc[i]['buy'] == True:
            high = data_frame.iloc[i]['high'] - 0.250
            close = data_frame.iloc[i]['close'] + 0.300
            sl = data_frame[data_frame['high']==high]
            if len(sl) > 0:
                data_frame.at[i,'SL'] = sl.iloc[0]['time']
            tp = data_frame[data_frame['close']==close]
            if len(tp) > 0:        
                data_frame.at[i,'TP'] = tp.iloc[0]['time']
            
    data_frame = data_frame[(data_frame['sell'] == True) | (data_frame['buy'] == True)] 
    
    return data_frame