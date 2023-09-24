'''
Расчеты о случаях выгодности ожидания обвалов рынка
Вычисление для полного числа лет.
Обвал происходит в последний месяц года и отображется
на месячном графике в первом месяце следующего года
- - -
Calculations about the cases of profitability of waiting for market collapses
'''

import datetime # https://pythonru.com/primery/kak-ispolzovat-modul-datetime-v-python
import dateutil # https/stackoverflow.com/questions/32083726/how-do-i-convert-days-into-years-and-months-in-python
import random # https://docs.python.org/3/library/random.html

from copy import deepcopy
from collections import Counter

import numpy as np
import matplotlib.pyplot as plt
import pprint
from p_date_time import *


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
    a1 = min_ + (max_-min_)*a
    # print(min(a),' ',max(a))
    b = np.linspace(start=min_, stop=max_, num=n)
    b = np.logspace(start=min_, stop=max_, num=n)
    b = np.geomspace(start=min_, stop=max_, num=n)
    return a1, b, a1+b

def calc_market_data(min_:float, growth_pc:float, n:int)->(np.ndarray, np.ndarray, np.ndarray, float):
    # https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html
    max_ = min_*(1+growth_pc/100)
    a = np.random.rand(n)
    a1 = min_ + (max_-min_)*a*0.3  # нормируем на нужный размах случайную составляющую
                                   # шум в долях от размаха значений
    # print(min(a),' ',max(a))
    b = np.linspace(start=min_, stop=max_, num=n)
    b = np.logspace(start=min_, stop=max_, num=n)
    b = np.geomspace(start=min_, stop=max_, num=n)
    return a1, b, a1+b, max_ # шум, тренд, тренд+шум

def calc_deposit_data(min_:float, growth_pc:float, n:int)->(np.ndarray, float):
    # https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html
    max_ = min_*(1+growth_pc/100)
    dat = np.linspace(start=min_, stop=max_, num=n)
    return dat, max_ #

def find_num_years_in_list(lst:list[datetime.date])->int:
    years = [dat.year for dat in lst]
    counts = Counter(years)
    print(f'{len(counts)=}')
    return len(counts)

def growth_calculations(start_year:int, end_year:int, market_growth_in_pc:list, deposit_growth_in_pc:list)->(np.ndarray, np.ndarray):
    llst = create_list_of_first_day_of_month_full_year_with_next_months(start_year,end_year)
    arr_x:np.ndarray = np.array(llst)
    sz = arr_x.size
    rnd_, trend_, arr_y = calc_test_data(min_=1, max_=2, n=sz)
    return arr_x, arr_y, trend_, rnd_

def growth_calculations2(start_year:int, end_year:int, market_growth_in_pc:list, deposit_growth_in_pc:list,
                         num_full_years:int)->(np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray):
    lst = create_list_of_first_day_of_month_full_year_with_next_months(start_year,end_year)
    num_years = find_num_years_in_list(lst)-1 # отбрасываем первый месяц последнего года (состоящего из одного месяца)
    arr_x:np.ndarray = np.array(lst)
    print('1 last = ',arr_x[0],' ', arr_x[-1])
    sz = arr_x.size
    # print(f'{sz=}')
    ysz = 13
    rnd_ = np.zeros(ysz); trend_=np.zeros(ysz); arr_y=np.zeros(ysz); depo_=np.zeros(ysz)
    for i in range(num_full_years):
        if i == 0:
            min_ = 1
            rnd_, trend_, arr_y, max_ = calc_market_data(min_=min_, growth_pc=market_growth_in_pc[i], n=ysz)
            depo_, maxdepo_ = calc_deposit_data(min_, deposit_growth_in_pc[i], n=ysz)
        elif i <num_full_years-1: # не последнее значение
            min_ = max_
            rnd_2, trend_2, arr_y2, max_ = calc_market_data(min_=min_, growth_pc= market_growth_in_pc[i], n=ysz)
            rnd_ = np.concatenate((rnd_, rnd_2[:-1]))
            trend_ = np.concatenate((trend_, trend_2[:-1]))
            arr_y = np.concatenate((arr_y, arr_y2[:-1]))
            depo_2, maxdepo_ = calc_deposit_data(maxdepo_, deposit_growth_in_pc[i], n=ysz)
            depo_ = np.concatenate((depo_, depo_2[:-1]))
        else: # последнее значение
            rnd_2, trend_2, arr_y2, max_ = calc_market_data(min_=max_, growth_pc= market_growth_in_pc[i], n=ysz)
            rnd_ = np.concatenate((rnd_, rnd_2[:-1]))
            trend_ = np.concatenate((trend_, trend_2[:-1]))
            arr_y = np.concatenate((arr_y, arr_y2[:-1]))
            depo_2, maxdepo_ = calc_deposit_data(maxdepo_, deposit_growth_in_pc[i], n=ysz)
            depo_ = np.concatenate((depo_, depo_2[:-1]))
        print(i, rnd_.size, trend_.size,arr_y.size)
    return arr_x, arr_y, trend_, rnd_, depo_

def decline_calculations(dat:np.ndarray, decline_in_pc:float)->np.ndarray:
    '''
    В последний месяц периода происходит спад на decline_in_pc процентов
    '''
    dat2 = deepcopy(dat)
    dat2[-1] = dat2[-1]*(1-decline_in_pc/100)
    return dat2

def work_with_growth_calculations():
    start_year = 2022
    end_year = 2024

    num_years = end_year - start_year +1
    # print(f'{num_years=}')
    year_market_growth_in_pc = 50
    year_market_growth_in_pc_lst = [year_market_growth_in_pc for i in range(num_years)]

    deposit_growth_in_pc = 14
    deposit_growth_in_pc_lst = [deposit_growth_in_pc for i in range(num_years)]
    # 1 вариант вычислений
    # x, y, trend_, rnd_  = growth_calculations(start_year, end_year,
    #                                           market_growth_in_pc=year_market_growth_in_pc_lst,
    #                                           deposit_growth_in_pc=deposit_growth_in_pc_lst)

    # 2 вариант вычислений
    x, y, trend_, rnd_, depo_  = growth_calculations2(start_year, end_year,
                                              market_growth_in_pc=year_market_growth_in_pc_lst,
                                              deposit_growth_in_pc=deposit_growth_in_pc_lst,
                                              num_full_years=num_years)
    # print('Длины массивов')
    # print(x.size);     print(y.size);     print(trend_.size);     print(rnd_.size)
    y1 =  decline_calculations(y, 30)

    fig = plt.figure(figsize=(10, 8))
    plt.plot(x,y1, label='market full data line with decline')
    plt.plot(x, y1,'ro',label='market full data point with decline')
    plt.plot(x, trend_, label='market trend line')
    plt.plot(x, rnd_, label='market random line')
    plt.plot(x, depo_, label='deposit line')
    plt.title('Movement for the period')
    plt.grid()
    plt.legend()
    plt.show()

if __name__ == "__main__":
    work_with_growth_calculations()
