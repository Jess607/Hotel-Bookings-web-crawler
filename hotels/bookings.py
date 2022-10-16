from selenium import webdriver as webdriver
import os
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from hotels.bookings_lagos import Booking_Lagos

class Booking(webdriver.Chrome):
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(executable_path='C:\chromedriver_win32\chromedriver', options=chrome_options)
        self.driver=driver
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def find_hotel(self):
        self.driver.get('https://hotels.ng/')
        

    def book_lagos(self):
        lagos_hotel=Booking_Lagos(driver=self.driver)
        lagos_hotel.hotels_lagos()
        lagos_hotel.select_budget(budget=3000)