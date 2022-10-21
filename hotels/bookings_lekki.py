import smtplib
from selenium import webdriver as webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from hotels.constant import EMAIL 
from hotels.constant import PASSWORD 

# class for book_lekki that handles all crawling 
class Booking_Lekki():
    def __init__(self, driver:WebDriver):
        self.driver=driver


    def select_location(self):
        elems=self.driver.find_element(By.XPATH, '//form[@method="post"]//label[@for="196-lekki"]//span[1]')
        self.driver.execute_script("arguments[0].click();", elems)
                   

    def select_budget(self, budget):
        budget=int(budget)
        if 0<=budget<=15000:
            elems=self.driver.find_element(By.CSS_SELECTOR, 'body > main:nth-child(3) > section:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(3) > fieldset:nth-child(1) > label:nth-child(2) > span:nth-child(3)')
            self.driver.execute_script("arguments[0].click();", elems)
            link=self.driver.find_element(By.ID, 'refineBudget')
            self.driver.execute_script("arguments[0].click();", link)
        if 15000<budget<=20000:
            elems=self.driver.find_element(By.CSS_SELECTOR, 'body > main:nth-child(3) > section:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(3) > fieldset:nth-child(1) > label:nth-child(3) > span:nth-child(3)')
            self.driver.execute_script("arguments[0].click();", elems)
            link=self.driver.find_element(By.ID, 'refineBudget')
            self.driver.execute_script("arguments[0].click();", link)
        if 20000<budget<=30000:
            elems=self.driver.find_element(By.CSS_SELECTOR, 'body > main:nth-child(3) > section:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(3) > fieldset:nth-child(1) > label:nth-child(4) > span:nth-child(3)')
            self.driver.execute_script("arguments[0].click();", elems)
            link=self.driver.find_element(By.ID, 'refineBudget')
            self.driver.execute_script("arguments[0].click();", link)
        if 30000<budget<=49950:
            elems=self.driver.find_element(By.CSS_SELECTOR, 'body > main:nth-child(3) > section:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(3) > fieldset:nth-child(1) > label:nth-child(5) > span:nth-child(3)')
            self.driver.execute_script("arguments[0].click();", elems)
            link=self.driver.find_element(By.ID, 'refineBudget')
            self.driver.execute_script("arguments[0].click();", link)
        if budget>49950:
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


    def send_email(self, email):
        lst=self.get_hotels()
        server=smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login( f'{EMAIL}', f'{PASSWORD}')
        body=''
        for i in lst:
            body= body + 'Hotel name:' f'{i["name"]}' + '\n' + 'Address:' f'{i["address"]}' + '\n'+ 'Price:' + f'{i["price"][1:]}' +' ' + 'Naira' + '\n' + 'Ratings:' f'{i["ratings"]}' + '\n' + 'Book here:' f'{i["web"]}' + '\n' + '\n'
        subject= 'Hotels In Lekki'
        main_body= "Here's what we found for you!" + '\n' + '\n' + f'{body}'
        message = f"Subject : {subject}\n\n{main_body}"
        server.sendmail(
            f'{EMAIL}',
            f'{email}',
            message
        )
        server.quit()
       