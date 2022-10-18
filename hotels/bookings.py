from selenium import webdriver as webdriver
import os
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from hotels.bookings_ikeja import Booking_Ikeja

class Booking(webdriver.Chrome):
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(executable_path='C:\chromedriver_win32\chromedriver', options=chrome_options)
        self.driver=driver
        self.driver.implicitly_wait(50)
        self.driver.maximize_window()

    def find_hotel(self):
        self.driver.get('https://hotels.ng/hotels-in-lagos')
        

    def book_ikeja(self, budget):
        ikeja_hotel=Booking_Ikeja(driver=self.driver)
        ikeja_hotel.select_location()
        ikeja_hotel.select_budget(budget=budget)
        ikeja_hotel.send_email()