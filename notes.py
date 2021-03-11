# this script highlights some interesting notes that I wasn't aware of prior to the udemy course

'''
All Python scripts should start with the following:
#! <>
Windows: python3
Mac: /usr/env/bin/python3
Linux: /usr/bin/python3

on Windows, shebang line is not needed unless you have multiple versions of Python
Win+R py \path\to\script.py


batch file XXX.bat
@py C:\path\to\script.py %*
@pause

@ tells windows (don't display the line just do it)
%* means forward and cmd args to the script

@pyw will run a script without a script

edit PATH - add folder which has all executable python scripts and .bat files
then Win+R XXX (don't need full path or .bat extension)

Win+R XXX arg1 arg2 arg3 (when using sys.argv)
this passes the arguments to the batch file
but the %* in the batch file forwards them to the python script


'''

import copy
import pprint


def list_notes():
    fruit = ['apple', 'watermelon', 'banana']
    red, green, yellow = fruit
    print(red, green, yellow)

    spam = list(range(6))
    # reference to a list
    cheese = spam
    # copy the reference to the list that spam is referencing
    cheese[1] = 'Hello'
    print(spam, cheese, sep='\n')
    # both cheese and spam get changed
    # cheese = spam are referencing the same list
    # this is the case with mutable variables

    cheese = copy.deepcopy(spam)
    # reference to a copy of spam's list reference
    cheese[2] = 'World'
    print(spam, cheese, sep='\n')

    print('Four score and' + \
          'seven years ago.')
    # ignore indentation


def count_string_letters(str):
    d = {}
    for let in str:
        d.setdefault(let, 0)
        d[let] += 1
    pprint.pprint(d)
    #dict_text = pprint.pformat(d)


def string_fun():
    'hello'.ljust(10)
    'hello'.rjust(10)
    'hello'.center(20)


def main():
    print('we\'re in main')


if __name__ == '__main__':
    main()