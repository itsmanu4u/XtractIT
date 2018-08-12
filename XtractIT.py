'''
a Python Script to scrape websites for
email addresses and US phone numbers
Author: Manmohan Chauhan
https://github.com/itsmanu4u
'''

from bs4 import BeautifulSoup
import re
from urllib.request import urlopen


#Lets use the input box for Website to Scrap

k = input('\nType/paste the Website(i.e http://www.example.com) for Scraping(E-mail, Contacts) : ')

f = urlopen(k)

s = BeautifulSoup(f, 'html.parser')
s = s.get_text()

phone = re.findall(r"((?:\d{3}|\(\d{3}\))?(?:\s|-|\.)?\d{3}(?:\s|-|\.)\d{4})",s)
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}",s)
print('\n\n=================| MyWebScrappy |=================')   
if len(phone) == 0:
    print ("Sorry, no phone number found.")

    print('----------------------------------------')
    print ()
else :
    count = 1
    for item in phone:
        print ( '\n',count, ' phone number(s) found : ',item )
        count += 1

print('---------------------------------------')
print()

if len(emails) == 0:
    print("Sorry, no email address found.")
    print('\n\n==================================================\n')
    print()
else:
    count = 1
    for item in emails:
        print(count, ' email address(es) found : ', item)
        count += 1

print('')
