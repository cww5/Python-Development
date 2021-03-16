#! python3

import re
import pyperclip

'''
TODO:
>>DONE 1. Create a regex object for phone numbers
>>DONE 2. Create a regex object for email addresses
>>DONE 3. Get text from clipboard
4. Extract emails / phone numbers from the text
5. Copy extracted emails / phone numbers to key board

'''


def get_text_from_clipboard():
    all_text = pyperclip.paste()
    return all_text


def create_phone_email_regex():
    '''
    Phone numbers can be in the following formats:
    XXX-XXX-XXXX   (XXX)-XXX-XXXX
    '''
    phone_number_regex = re.compile(
        r'''
        (\d{3}) |   # XXX
        \(\d{3}\)   # (XXX)
        -
        \d{3}       # XXX
        -
        \d{4}       # XXXX
        (x\d{4})?
        ''', re.VERBOSE
    )
    email_address_regex = re.compile(r'([a-zA-Z]|[0-9]|_)*@[a-zA-Z]+.[a-z]+')
    return phone_number_regex, email_address_regex


def main():
    copied_text = get_text_from_clipboard()
    print(copied_text)
    phone_regex, email_regex = create_phone_email_regex()


if __name__ == '__main__':
    main()
