'''
TA-Lib : Technical Analysis Library
https://ta-lib.github.io/

Взять библиотеку для Python 10
https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib
TA-Lib. Как установить. Библиотека технического анализа для Python / TA-Lib. How to install Python
https://www.youtube.com/watch?v=vvtAVAkpETE

Скинуть в C:\Python\Python310\Scripts
Установить как pip install TA_Lib-0.4.24-cp310-cp310-win_amd64.whl

# how to install Ta-lib with python 3.11 in Windows?
# https://stackoverflow.com/questions/75474154/how-to-install-ta-lib-with-python-3-11-in-windows

Краткий обзор библиотеки TA-lib | Теханализ в Python
https://www.youtube.com/watch?v=eBG8nCfeKXc

TA - LIB. Библиотека теханализа для Python. Обзор библиотеки индикаторов для трейдинга -
не работает визуализация как там указано, исправлено в данной программе
https://www.youtube.com/watch?v=5KHdKZqJg1E
'''

import pprint
import talib
import numpy as np
import yfinance as yf
import mplfinance as mpf
from talib import abstract
import pandas as pd
import matplotlib.pyplot as plt


def about_talib():
    # print('\n','-- dir(talib) --')
    # pprint.pprint(dir(talib))
    print('\n','-- list(talib.get_function_groups().keys()) --')
    pprint.pprint(list(talib.get_function_groups().keys()))
    print('\n','-- list(talib.get_function_groups()) --')
    pprint.pprint(list(talib.get_function_groups()))
    print('\n','-- list(talib.get_functions()) --')
    pprint.pprint(list(talib.get_functions()))
    print('\n','-- talib.get_function_groups()["Momentum Indicators"]) --')
    pprint.pprint(list(talib.get_function_groups()["Momentum Indicators"]))
    print('\n', 'help(talib.AROONOSC')
    pprint.pprint(help(talib.AROONOSC))

def thetest_talib_view():
    '''
    https://www.youtube.com/watch?v=5KHdKZqJg1E
    '''

    data = yf.download('SPY', start= '2021-01-01', end='2022-08-01')
    # print(type(data))
    print(data)

    sma = talib.SMA(data['High'])
    sma_plot = mpf.make_addplot(sma)
    mpf.plot(data, addplot=sma_plot,type='candle', style='yahoo')

    rsi = talib.RSI(data['High'],timeperiod = 14)
    rsi_plot = mpf.make_addplot(rsi,panel=1)
    mpf.plot(data, addplot=rsi_plot, type='candle', style='yahoo')

def thetest_talib_rename_data(data):
    data.rename(columns={'Open':'open',
                         'High':'high',
                         'Low' : 'low',
                         'Adj Close':'close',
                         'Volume':'volume'}, inplace=True)
    return data
def thetest_talib():
    '''
    https://www.youtube.com/watch?v=eBG8nCfeKXc
    '''
    st_d = '2021-01-01'
    en_d = '2021-05-07'
    data = yf.download('SPY', start= st_d, end=en_d)
    # print(type(data))
    print(data)

    # https://www.youtube.com/watch?v=eBG8nCfeKXc
    aroon = talib.AROONOSC(data['High'], data['High'], timeperiod=14)
    print('talib.AROONOSC.__doc__')
    print(talib.AROONOSC.__doc__)
    print(f'{type(aroon)=}')
    print(f'{aroon= }')
    print('\n')
    print(aroon[st_d:en_d])

    ms = talib.CDLMORNINGSTAR(data['Open'],data['High'], data['Low'], data['Close'])
    print(f'\n talib.CDLMORNINGSTAR \n {ms= }')

    data = thetest_talib_rename_data(data)
    ms2 = abstract.CDLMORNINGSTAR(data)
    print(f'\n {ms2=}')
    print()
    print(ms2[ms2!=0])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # about_talib()
    # thetest_talib_view()
    thetest_talib()

