'''
a Python Script to scrape websites for
email addresses and US phone numbers
Author: Manmohan Chauhan
https://github.com/itsmanu4u
'''
print('\n\n======================| XtractIT V.2 |========================')

print("""


		      ("`-''-/").___..--''"`-._
                       `6_ 6  )   `-.  (     ).`-.__.`)
                       (_Y_.)'  ._   )  `._ `. ``-..-'
                     _..`--'_..-_/  /--'_.' ,'
                    (il),-''  (li),'  ((!.-'
""")
print('===============================================================')


import time
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

print('\n\n=================| XtractIT |=================')   
if len(phone) == 0:
    print ("Sorry, no phone number found.")
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
    print()
else:
    count = 1
    for item in emails:
        print(count, ' email address(es) found : ', item)
        count += 1

print('==================================================')
print('\n \n')

pref = input('Do you want to Export data into Excel ? (Y/N) : ')

if pref == 'Y':
    print('\n Please wait, exporting data.....')
    time.sleep(4)

    lst = (phone, emails)
    saveFile = open('Xtract.csv','w')
    saveFile.write(str(phone +  emails))
    saveFile.close()
else:
    print('\n Closing Program...')
    time.sleep(2)


