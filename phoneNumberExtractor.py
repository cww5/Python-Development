#! python3

import re
import pyperclip

'''
TODO:
>>DONE 1. Create a regex object for phone numbers
>>DONE 2. Create a regex object for email addresses
>>DONE 3. Get text from clipboard
>>DONE 4. Extract emails / phone numbers from the text
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
        (\d\d\d-) |      # XXX-
        (\(\d\d\d\)-) |  # (XXX)-
        (\(\d\d\d\) )    # (XXX) 
        \d{3}           # XXX
        -
        \d{4}           # XXXX
        (\sx\d{2,5})?
        ''', re.VERBOSE
    )
    phone_number_regex = re.compile(r'\(\d{3}\) \d{3}-\d{4}')
    email_address_regex = re.compile(r'([a-z|A-Z]|[0-9]|_)*\@[a-zA-Z]+\.[a-z]+')
    email_address_regex = re.compile(r'[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-z]+')
    return phone_number_regex, email_address_regex


def get_phone_numbers_from_text(text, phone_regex):
    phone_list = phone_regex.findall(text)
    return phone_list


def get_emails_from_text(text, email_regex):
    email_list = email_regex.findall(text)
    return email_list


def main():
    copied_text = get_text_from_clipboard()
    print(copied_text)
    phone_regex, email_regex = create_phone_email_regex()
    all_numbers = get_phone_numbers_from_text(copied_text, phone_regex)
    print(all_numbers)
    all_emails = get_emails_from_text(copied_text, email_regex)
    print(all_emails)


if __name__ == '__main__':
    main()
