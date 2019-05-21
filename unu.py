import time, os, re
import argparse
from time import sleep  
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

parser = argparse.ArgumentParser(description='A Facebook lookup utility', usage='python3 firefox.py filename(s)', add_help=False)
parser.add_argument('id', nargs="*")
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Please put the Facebook ID')
args = vars(parser.parse_args())


_browser_profile = webdriver.FirefoxProfile()
_browser_profile.set_preference("dom.webnotifications.enabled", False)
driver = webdriver.Firefox(firefox_profile=_browser_profile, executable_path = '/Users/dell3/Downloads/geckodriver')

driver.get('https://www.facebook.com')
driver.maximize_window()

elem = driver.find_element_by_id("email")
elem.send_keys("XXX")

elem_pass= driver.find_element_by_id("pass")
elem_pass.send_keys("XXXX")
sleep(1) 
elem_login= driver.find_element_by_id('loginbutton')
elem.send_keys(Keys.RETURN)
sleep(4)

id = args['id']
number=id[0]

list =["apps-used", "employees", "employers", "events", "events-joined","events-joined/in-past/date/events/intersect/",
"friends/pages-liked", "groups", "pages-liked","photos", "photos-by","photos-commented","places-checked-in/",
"photos-liked", "places-visited", "places-liked", "places-visited", "recent-places-visited", "relatives",
"stories-by", "stories-tagged", "stories-liked", "stories-commented", "videos", "videos-of", "videos-by",
"videos-commented", "videos-liked",
 ]

for i in range(1,27):
    link= "https://www.facebook.com/search/{}/".format(str(number))
    driver.execute_script("window.open('"+link+list[i-1]+"', '_blank')")
    sleep(2)
    print (i)


print ('\nCopyright Ionut Cohen(C)All rights reserved.')

