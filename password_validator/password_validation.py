# This program validates the correctness of passwords entered by users
import re

valid = False

while not valid:
    password = input('Enter your password: ')

    if len(password) < 6 or len(password) > 12:
        print('Password must be between 6 and 12 characters')
        valid = False
    elif not re.search('[a-z]+', password):
        print('Password must have at least one lower case alphabet')
        valid = False
    elif not re.search('[A-Z]+', password):
        print('Password must have at least one upper case alphabet')
        valid = False
    elif not re.search('[0-9]+', password):
        print('Password must have at least one number between 0 and 9')
        valid = False
    elif not re.search('[$#@]+', password):
        print('Password must contain at least one $, # or @ sign')
        valid = False
    else:
        print('Password is correct')
        valid = True
