'''
Расчеты о случаях выгодности ожидания обвалов рынка
- - -
Calculations about the cases of profitability of waiting for market collapses
'''

import datetime # https://pythonru.com/primery/kak-ispolzovat-modul-datetime-v-python
import dateutil # https/stackoverflow.com/questions/32083726/how-do-i-convert-days-into-years-and-months-in-python
import numpy as np
import matplotlib.pyplot as plt
import pprint
from p_date_time import *

num_points_in_year = 4

def calc_max_onbase_prc(min_:float,prc:float)->float:
        '''
        Вычисление конечного значения
        '''
        end_ = min_*(1+prc/100)
        return end_

def calc_test_data(min_:float, max_:float, n:int)->(np.ndarray, np.ndarray, np.ndarray):
    '''
    Тестовые данные: тренд + шум
    '''
    # https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html
    a = np.random.rand(n)
    # print(min(a),' ',max(a))
    b = np.linspace(start=min_, stop=max_, num=n)
    b = np.logspace(start=min_, stop=max_, num=n)
    b = np.geomspace(start=min_, stop=max_, num=n)
    return a, b, a+b

def growth_calculations(start_year:int, end_year:int, market_growth_in_pc:list, deposit_growth_in_pc:list)->(np.ndarray, np.ndarray):
    llst = create_list_of_first_day_of_month_full_year_with_next_months(start_year,end_year)
    arr_x:np.ndarray = np.array(llst)
    print('1 last = ',arr_x[0],' ', arr_x[-1])
    sz = arr_x.size
    # print(f'{sz=}')

    rnd_, trend_, arr_y = calc_test_data(min_=1, max_=2, n=sz)
    print('Рост')
    return arr_x, arr_y, trend_, rnd_

def work_with_growth_calculations():
    start_year = 2022
    end_year = 2024
    num_years = end_year - start_year +1
    year_market_growth_in_pc = [50 for i in range(num_years)]
    deposit_growth_in_pc = [14 for i in range(num_years)]
    x, y, trend_, rnd_  = growth_calculations(start_year, end_year,
                                              market_growth_in_pc=year_market_growth_in_pc,
                                              deposit_growth_in_pc=deposit_growth_in_pc)
    fig = plt.figure(figsize=(10, 8))
    plt.plot(x,y, label='full data line')
    plt.plot(x, y,'ro',label='full data point')
    plt.plot(x, trend_, label='trend line')
    plt.plot(x, rnd_, label='random line')
    plt.title('Movement for the period')
    plt.grid()
    plt.legend()
    plt.show()

if __name__ == "__main__":
    work_with_growth_calculations()
