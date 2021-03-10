# this script highlights some interesting notes that I wasn't aware of prior to the udemy course
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