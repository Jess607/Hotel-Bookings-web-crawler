from selenium import webdriver as webdriver
import os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from hotels.bookings_ikeja import Booking_Ikeja
from hotels.bookings_ikoyi import Booking_Ikoyi
from hotels.bookings_lekki import Booking_Lekki
from hotels.constant import BASE_URL

class Booking(webdriver.Chrome):
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(executable_path='C:\chromedriver_win32\chromedriver', options=chrome_options)
        self.driver=driver
        self.driver.implicitly_wait(50)
        self.driver.maximize_window()

    # this method gets the url that holds all the hotels
    def find_hotel(self): 
        self.driver.get(BASE_URL)
        
    # method to book hotels in Ikeja
    def book_ikeja(self, budget, email):
        ikeja_hotel=Booking_Ikeja(driver=self.driver)
        ikeja_hotel.select_location()
        ikeja_hotel.select_budget(budget=budget)
        ikeja_hotel.send_email(email=email)

    # method to book hotels in Ikoyi
    def book_ikoyi(self, budget, email):
        ikoyi_hotel=Booking_Ikoyi(driver=self.driver)
        ikoyi_hotel.select_location()
        ikoyi_hotel.select_budget(budget=budget)
        ikoyi_hotel.send_email(email=email)

    # method to book hotels in Lekki
    def book_lekki(self, budget, email):
        lekki_hotel= Booking_Lekki(driver=self.driver)
        lekki_hotel.select_location()
        lekki_hotel.select_budget(budget=budget)
        lekki_hotel.send_email(email=email)