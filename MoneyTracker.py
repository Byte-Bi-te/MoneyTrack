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
    
def transaction_history():
    for i in range(len(acc)):
        print(f"{'In' if acc.loc[i, 'in_out'] == 1 else 'Out'} "
              f"{acc.loc[i, 'value']} "
              f"{int(acc.loc[i, 'day'])}/"
              f"{int(acc.loc[i, 'month'])}/"
              f"{int(acc.loc[i, 'year'])} - "
              f"{int(acc.loc[i, 'hour'])}:"
              f"{int(acc.loc[i, 'minute'])}")

def total_calc():
    total = 0.0
    
    for i in range(len(acc)):
        if acc.loc[i, 'in_out'] == 1:
            total = total + acc.loc[i, 'value']
        else:
            total = total - acc.loc[i, 'value']
   
    print(f"Total: {total}")
    
def account_menu():
    while True:
        act = int(input(
              '''
    ========== ACCOUNT ==========
    
    1. View current balance
    2. Account overview
    3. Return to main menu
    
    =============================
              '''))
        
        match act:
            case 1:
                total_calc()
            case 2:
                print('Work in progress')
            case 3:
                break
            case _:
                print('Invalid option, try again')
            
def transactions_menu():
    while True:
        act = int(input(
            '''
    ======== TRANSACTIONS ========
    
    1. Add income
    2. Add expense
    3. Transaction history
    4. Search transactions
    5. Return to main menu
    
    ==============================
            '''))
    
        match act:
            case 1:
                transfer_in()
            case 2:
                transfer_out()
            case 3:
                transaction_history()
            case 4:
                print('Work in progress')
            case 5:
                break
            case _:
                print('Invalid option, try again')
    
def main_menu():
    while True:
        act = int(input(
              '''
    ========== EXPENSE TRACKER ==========
    
    1. Account
    2. Transactions
    3. Statistics
    4. Settings
    5. Exit
    
    =====================================
              '''))
              
        match act:
            case 1:
                account_menu()
            case 2:
                transactions_menu()
            case 3:
                print('Work in progress')
            case 4:
                print('Work in progress')
            case 5:
                sys.exit()
            case _: 
                print('Invalid option, please try again')

main_menu()

