import time, os, re
import argparse
from time import sleep  
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

parser = argparse.ArgumentParser(description='A Facebook lookup utility', usage='python3 facebook.py facebook id', add_help=False)
parser.add_argument('-i', '--id', help='Please put the Facebook ID for the first person')
parser.add_argument('-j', '--id2', help='Please put the Facebook ID for the second person')
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Please put the Facebook ID')
args = vars(parser.parse_args())


_browser_profile = webdriver.FirefoxProfile()
_browser_profile.set_preference("dom.webnotifications.enabled", False)
driver = webdriver.Firefox(firefox_profile=_browser_profile, executable_path = '/Users/dell3/Downloads/geckodriver')

driver.get('https://www.facebook.com')
driver.maximize_window()

elem = driver.find_element_by_id("email")
elem.send_keys("XXXX")

elem_pass= driver.find_element_by_id("pass")
elem_pass.send_keys("XXXX")
sleep(1) 
elem_login= driver.find_element_by_id('loginbutton')
elem.send_keys(Keys.RETURN)
sleep(4)

id = args['id']
number=id
print(number)
id2 = args['id2']
number2=id2
print(number2)
list =[ "places-visited", "pages-liked", "photos-of","photos-liked","photos-commented", "videos-of", "videos-liked","videos-commented",
"stories-commented","groups","/events/2010/after/events", 
 ]

for i in range(1,11):
    link= "https://www.facebook.com/search/{}/".format(str(number))
    link2= "/{}/".format(str(number2))
    intersect="/intersect/"
    driver.execute_script("window.open('"+link+list[i-1]+link2+list[i-1]+intersect+"', '_blank')")
    # chromewebdriver.execute_script("window.open('"+url+"', 'new_window"+str(i)+"')")
    sleep(2)
    print (i)


print ('\nCopyright Ionut Cohen(C)All rights reserved.')

