import smtplib
from selenium import webdriver as webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from hotels.constant import LAGOS_CITIES

class Booking_Ikeja():
    def __init__(self, driver:WebDriver):
        self.driver=driver


    def select_location(self):
        elems=self.driver.find_element(By.XPATH, '//label[@for="135-ikeja"]//span[@class="v7-checkbox-checkmark"]')
        self.driver.execute_script("arguments[0].click();", elems)
                   

    def select_budget(self, budget):
        budget=int(budget)
        if 0<=budget<=10000:
            elems=self.driver.find_element(By.XPATH, '//div[@class="listing-filter-range-box"]//label[1]//span[2]')
            self.driver.execute_script("arguments[0].click();", elems)
            link=self.driver.find_element(By.ID, 'refineBudget')
            self.driver.execute_script("arguments[0].click();", link)
        if 10000<budget<=14000:
            elems=self.driver.find_element(By.CSS_SELECTOR, 'body > main:nth-child(3) > section:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(3) > fieldset:nth-child(1) > label:nth-child(3) > span:nth-child(3)')
            self.driver.execute_script("arguments[0].click();", elems)
            link=self.driver.find_element(By.ID, 'refineBudget')
            self.driver.execute_script("arguments[0].click();", link)
        if 14000<budget<=20000:
            elems=self.driver.find_element(By.CSS_SELECTOR, 'body > main:nth-child(3) > section:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(3) > fieldset:nth-child(1) > label:nth-child(4) > span:nth-child(3)')
            self.driver.execute_script("arguments[0].click();", elems)
            link=self.driver.find_element(By.ID, 'refineBudget')
            self.driver.execute_script("arguments[0].click();", link)
        if 20000<budget<=28000:
            elems=self.driver.find_element(By.CSS_SELECTOR, 'body > main:nth-child(3) > section:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(3) > fieldset:nth-child(1) > label:nth-child(5) > span:nth-child(3)')
            self.driver.execute_script("arguments[0].click();", elems)
            link=self.driver.find_element(By.ID, 'refineBudget')
            self.driver.execute_script("arguments[0].click();", link)
        if budget>28000:
            elems=self.driver.find_element(By.CSS_SELECTOR, 'body > main:nth-child(3) > section:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(3) > fieldset:nth-child(1) > label:nth-child(6) > span:nth-child(3)')
            self.driver.execute_script("arguments[0].click();", elems)
            link=self.driver.find_element(By.ID, 'refineBudget')
            self.driver.execute_script("arguments[0].click();", link)

    def get_hotels(self):
        elems=self.driver.find_element(By.ID, 'topPicks')
        link=elems.find_elements(By.CLASS_NAME,'row')
        lis=[]
        for i in range(len(link)):
            new_dict={}
            try:
                anchor=link[i].find_element(By.CLASS_NAME, 'listing-hotels-details-property')
                h2_var=anchor.find_element(By.TAG_NAME, 'h2')
                website=anchor.find_element(By.TAG_NAME, 'a')
                address=link[i].find_element(By.CSS_SELECTOR,'p.listing-hotels-address.color-dark.hidden-md.hidden-lg')
                add=address.get_attribute('textContent')
                prices=link[i].find_element(By.CSS_SELECTOR,'p.listing-hotels-prices-discount')
                price=prices.get_attribute('textContent')
                ratings=link[i].find_element(By.CSS_SELECTOR, 'p.listing-hotels-rating')
                rating=ratings.find_element(By.TAG_NAME, 'span')
                new_dict['address']=add.split("-")[1]
                new_dict['name']=h2_var.text
                new_dict['web']=website.get_attribute('href')
                new_dict['price']=price.split(' ')[0].strip()
                new_dict['ratings']=rating.get_attribute('textContent')
                lis.append(new_dict)
            except:
                print('No')
        return lis


    def send_email(self):
        lst=self.get_hotels()
        server=smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('ogwujessica2222@gmail.com', 'Jersika790')
        names=lst[0]
        name=names['address']
        body=name
        server.sendmail(
            'ogwujessica2016@gmail.com',
            body
        )
        server.quit()
          
        
        

        


        
          



        
        