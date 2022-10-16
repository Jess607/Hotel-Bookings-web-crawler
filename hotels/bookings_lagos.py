from selenium import webdriver as webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

class Booking_Lagos():
    def __init__(self, driver:WebDriver):
        self.driver=driver

    def hotels_lagos(self):
        elems = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/div/div[2]/div[1]/a")
        link=elems.get_attribute('href')
        self.driver.get(link)

    def select_area(self, location):
        location=location.lower()
        if location =='ikeja':
            elems = self.driver.find_element(By.XPATH, "/html/body/main/section[1]/div/div[1]/div[4]/form/div/div[1]/label/a")
            link=elems.get_attribute('href')
            self.driver.get(link)

    def select_budget(self, budget):
        budget=int(budget)
        if 0<=budget<=5000:
            elems=self.driver.find_element(By.XPATH, '//fieldset//label[1]//span[1]')
            self.driver.execute_script("arguments[0].click();", elems)
            link=self.driver.find_element(By.ID, 'refineBudget').click()
            self.driver.execute_script("arguments[0].click();", link)
            




        
        