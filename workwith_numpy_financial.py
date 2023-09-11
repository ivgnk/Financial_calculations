'''
https://pypi.org/project/numpy-financial/
https://github.com/numpy/numpy-financial

The numpy-financial Python package is a collection of elementary financial functions.
These functions were copied to this package from version 1.17 of NumPy.
The financial functions in NumPy are deprecated and eventually will be removed from NumPy
https://numpy.org/numpy-financial/

Financial functions
https://numpy.org/doc/1.17/reference/routines.financial.html


fv(rate, nper, pmt, pv[, when])  Compute the future value.
ipmt(rate, per, nper, pv[, fv, when])  Compute the interest portion of a payment.
irr(values)  Return the Internal Rate of Return (IRR).
mirr(values, finance_rate, reinvest_rate)  Modified internal rate of return.
nper(rate, pmt, pv[, fv, when])  Compute the number of periodic payments.
npv(rate, values)  Returns the NPV (Net Present Value) of a cash flow series.
pmt(rate, nper, pv[, fv, when])  Compute the payment against loan principal plus interest.
ppmt(rate, per, nper, pv[, fv, when]) Compute the payment against loan principal. pv(rate, nper, pmt[, fv, when]) Compute the present value.
rate(nper, pmt, pv, fv[, when, guess, tol, …]) Compute the rate of interest per period.https://numpy.org/numpy-financial/latest/
'''

import sys
import inspect
import numpy as np
import numpy_financial as npf
import pprint
import matplotlib.pyplot as plt


def about_numpy_financial():
    pprint.pprint(dir(npf))

    pprint.pprint(npf.pv.__doc__)

def thetest_numpy_financial_fv():
    '''
    numpy_financial.fv(rate, nper, pmt, pv, when='end')
    rate - scalar or array_like - Rate of interest as decimal (not per cent) per period
    npers - calar or array_like of shape(M, ) - Number of compounding periods
    pmt - scalar or array_like of shape(M, ) - Payment
    pv - scalar or array_like of shape(M, ) - Present value
    when{{‘begin’, 1}, {‘end’, 0}}, {string, int}, optional
    When payments are due (‘begin’ (1) or ‘end’ (0)). Defaults to {‘end’, 0}.

    Returns Future values. If all input is scalar, returns a scalar float.
    If any input is array_like, returns future values for each input element.
    If multiple inputs are array_like, they all must have the same shape.

    The future value is computed by solving the equation:
    fv + pv*(1+rate)**nper + pmt*(1 + rate*when)/rate*((1 + rate)**nper - 1) == 0
    or, when rate == 0:
    fv + pv + pmt * nper == 0
    https://numpy.org/numpy-financial/latest/fv.html#numpy_financial.fv
    '''
    print('1 step')
    # What is the future value after 10 years of saving $100 now,
    # with an additional monthly savings of $100.
    # Assume the interest rate is 5% (annually) compounded monthly?
    # By convention, the negative sign represents cash flow out (i.e. money not available today)
    print('total ', npf_fv:=npf.fv(0.05/12, 10*12, -100, -100))
    print('cash additions = ', cash_additions:=100*12*10)
    print('procents = ', procents:=npf_fv - cash_additions-100)
    print('part of procents = ', procents/npf_fv)

    print('\n2 step')
    a = np.array((0.05, 0.06, 0.07)) / 12
    print(npf.fv(a, 10 * 12, -100, -100))

def thetest_numpy_financial_fv2():
    print('Функция = ',inspect.currentframe().f_code.co_name,'\n')
    rate = 0.05/12
    nper = 10*12
    pmt = 0
    pv = -100
    print('total ', npf_fv:=npf.fv(rate, nper, pmt, pv))
    print('cash additions = ', cash_additions:=abs(pmt*nper))
    print('procents = ', procents:=npf_fv - cash_additions-abs(pv))
    print('part of procents = ', procents/npf_fv)
    x = np.zeros(nper+1)
    dat = np.zeros(nper+1)
    for i in range(nper+1):
        x[i] = i
        dat[i]= npf.fv(rate, i, pmt, pv)
    print(x)
    plt.plot(x,dat)
    plt.xlabel('Месяцы')
    plt.ylabel('Сумма')
    plt.grid()
    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # about_numpy_financial()
    thetest_numpy_financial_fv2()
