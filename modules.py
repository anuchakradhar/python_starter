# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules
#core model
from datetime import date
from time import time

#pip module
from camelcase import CamelCase

#import custom module
from validator import validate_email


today = date.today()
timestamp = time()

c = CamelCase()
print(c.hump('anu chakradhar'))

email = 'anu.chakradhar1@gmail.com'

if validate_email(email):
    print('Email is valid')
else:
    print('Not valid')

print (today)
print(timestamp)