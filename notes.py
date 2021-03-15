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
import re


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


def is_phone_number(text):
    # expects a valid phone number to be XXX-XXX-XXXX
    if len(text) != 12:
        return False
    for i in range(len(text)):
        if i in (3, 7):
            if text[i] == '-':
                continue
            else:
                return False
        if not text[i].isdecimal():
            return False
            return True


def regex_basics(message):
    print('regex stuff')
    phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    # find the regex in message
    # if search can't find, then it returns None
    matchObject = phoneNumberRegex.search(message)
    # show the first result
    print('first group matched:', matchObject.group())
    # show all results
    print('findall', phoneNumberRegex.findall(message))


def regex_groups(message):
    # parentheses separate different groups of regex searches
    phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    mo = phoneNumberRegex.search(message)
    print('group 1:', mo.group(1))
    print('group 2:', mo.group(2))

    # \( and \) would allow us to look up for literally ()
    # | separates all possible options
    batRegex = re.compile(r'bat(man|boy|mobile|wing|copter)')
    mo = batRegex.search('Batman rides the batwing to the batmobile')
    print('bat thing found:', mo.group())
    # to get the particular suffix found within that group:
    print('bat thing found:', mo.group(1))


def regex_greedy_nongreedy_matching(message):
    # ? means 0 or 1 times but \? is literal question mark
    batRegex1 = re.compile(r'bat(man|woman)')
    batRegex2 = re.compile(r'batman|batwoman')
    batRegex1 = re.compile(r'bat(wo)?man|woman')
    # batwowowoman will not match

    phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
    mo = phoneRegex.search('234-234-2345 and 234-1345')
    print(mo.group())

    # * means 0 or more times \* is a literal *
    # + means 1 or more times \+ is a literal +
    # X{N} means match expression X exactly N times
    # X{x,y} means match expression X at least x, at most y times
    # x or y are optional like list slicing

    # find the longest possible string
    digitRegex = re.compile(r'(\d){3,5}')
    mo = digitRegex.search('1234567890')
    print('Greedy digit search:', mo.group())

    # non greedy - find the shortest possible string
    digitRegex = re.compile(r'(\d){3,5}?')
    mo = digitRegex.search('1234567890')
    print('NONGreedy digit search:', mo.group())


def regex_find_all(message):
    phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    nums = phoneRegex.findall(message) # return a list of all matches in message
    print(nums)
    phoneRegex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    groups2 =  phoneRegex2.findall(message) # return a list of all matches in message
    print(groups2)
    phoneRegex3 = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
    groups3 = phoneRegex3.findall(message)  # return a list of all matches in message
    print(groups3)

def main():
    print('we\'re in main')
    num1 = '656-435-3452'
    num2 = '1-' + num1
    print('Is {} a phone number?: {}'.format(num1, is_phone_number(num1)))
    print('Is {} a phone number?: {}'.format(num2, is_phone_number(num2)))
    message = 'Call me at 415-324-2342 for mobile, 313-234-2345 for work'
    regex_basics(message)
    regex_groups(message)
    regex_greedy_nongreedy_matching(message)
    regex_find_all(message)

if __name__ == '__main__':
    main()
