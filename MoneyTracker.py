#The app works with .csv files and should be secure enough to run locally
#457749 is peak writing btw

import pandas as pd
import matplotlib as plot
import math
import datetime as dt
import sys
import os

if os.path.exists('account.csv'):
    acc = pd.read_csv('account.csv')
else:
    acc = pd.DataFrame(columns=['in_out', 'value', 'hour', 'minute', 'second', 'day', 'month', 'year']) 
    acc.to_csv('account.csv', index=False)
    
def access_account():
    for i in range(len(acc)):
        print(f"{'In' if acc.loc[i, 'in_out'] == 1 else 'Out'} "
              f"{acc.loc[i, 'value']} "
              f"{int(acc.loc[i, 'day'])}/"
              f"{int(acc.loc[i, 'month'])}/"
              f"{int(acc.loc[i, 'year'])} - "
              f"{int(acc.loc[i, 'hour'])}:"
              f"{int(acc.loc[i, 'minute'])}")

def transfer_in():
    value_current = float(input('Amount to add: '))
    now = dt.datetime.now()
    acc.loc[len(acc)] = [
        1,
        value_current,
        now.hour,
        now.minute,
        now.second,
        now.day,
        now.month,
        now.year]
    acc.to_csv('account.csv', index=False)
    print('Added ', value_current, ' to account.')
    
def transfer_out():
    value_current = float(input('Amount to remove: '))
    now = dt.datetime.now()
    acc.loc[len(acc)] = [
        0,
        value_current,
        now.hour,
        now.minute,
        now.second,
        now.day,
        now.month,
        now.year]
    acc.to_csv('account.csv', index=False)
    print('Removed ', value_current, ' from account.')

def total_calc():
    total = 0.0
    
    for i in range(len(acc)):
        if acc.loc[i, 'in_out'] == 1:
            total = total + acc.loc[i, 'value']
        else:
            total = total - acc.loc[i, 'value']
   
    print(f"Total: {total}")
    
while True:

    act = int(input(
          '''
    Options:
    1. Access Account
    2. Transfer In
    3. Transfer Out
    4. Total
    5. Exit
          '''))

    match act:
        case 1:
            access_account()
        case 2:
            transfer_in()
        case 3:
            transfer_out()
        case 4:
            total_calc()
        case 5:
            sys.exit()