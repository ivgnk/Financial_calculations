'''
Мои дополнительные функции для работы с датой и временем
'''
import datetime
import pprint

def create_list_of_first_day_of_month_full_year(year_start:int, year_end:int)->list:
    '''
    Задать первые числа месяцев для указанных начального и конечного годов
    '''
    llst = []
    for curr_year in range(year_start, year_end+1):
        for j in range(1,13):
            llst.append(datetime.date(year=curr_year,month=j,day=1))
    return llst

def create_list_of_first_day_of_month_full_year_with_next_months(year_start:int, year_end:int)->list:
    '''
    Дополнительно к "Задать первые числа месяцев для указанных начального и конечного годов"
    добавляем первое число следующего года (1 января)
    '''
    llst = create_list_of_first_day_of_month_full_year(year_start, year_end)
    llst.append(datetime.date(year=year_end+1,month=1,day=1))
    return llst

if __name__ == "__main__":
    # work_with_growth_calculations()
    # pprint.pprint(create_list_of_first_day_of_month_full_year(2021, 2022))
    pprint.pprint(create_list_of_first_day_of_month_full_year_with_next_months(2021, 2022))
