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


def growth_calculations()->np.ndarray:
    start_year = 2022
    start_year_dt = datetime.datetime(year=start_year, month=1, day=1)
    end_year = 2024
    end_year_dt = datetime.datetime(year=end_year+1, month=12, day=31)
    delta = end_year_dt-start_year_dt
    pprint.pprint(delta)
    every_year_growth = 12
    curr_year = start_year
    num_years = end_year-start_year
    x = np.linspace(start_year, end_year, num =num_years * num_points_in_year)
    print(f'{num_years=}')
    print(f'{max(x)=}')
    print(f'{len(x)=}')
    return x

def work_with_growth_calculations():
    x = growth_calculations()
    fig = plt.figure(figsize=(10, 8))
    plt.plot(x,x)
    plt.plot(x, x,'ro')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    # work_with_growth_calculations()
    pprint.pprint(create_list_of_first_day_of_month_full_year(2021, 2022))


