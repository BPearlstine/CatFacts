from selenium import webdriver
import time
import random
import csv

driver = webdriver.Firefox()

print('loading foxtext')
driver.get('https://www.foxtext.com/')

print("Inputting phone number")
driver.find_element_by_id('phone_number').send_keys("someone's phone number")

#get random number for array
rnd = random.randint(1,11)
print('random array index: ' + str(rnd))

#get list of cat facts to bother Maria with
with open('cat_facts.csv', 'r') as f:
    reader = csv.reader(f)
    catFactsList = list(reader)

print("today's fact: " + catFactsList[rnd])

driver.find_element_by_tag_name('textarea').send_keys(catFactsList[rnd])
driver.save_screenshot('latest_text.png')
driver.find_element_by_id('btnsms').click()

time.sleep(50)
driver.quit()

