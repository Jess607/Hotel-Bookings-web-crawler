# Hotel-Bookings-web-crawler
This project is a bot that crawls the web for hotel bookings in three major locations in Lagos,Nigeria and sends hotels found to users via email.

# Table Of Contents
* [Installation](https://github.com/Jess607/Hotel-Bookings-web-crawler#installation)
* [About the Project](https://github.com/Jess607/Hotel-Bookings-web-crawler#about-the-project)
* [File Description](https://github.com/Jess607/Hotel-Bookings-web-crawler#file-description)
* [License And Authoring](https://github.com/Jess607/Hotel-Bookings-web-crawler#licensing-and-authoring)

# Installation 
The code requires:
 * `python version 3 and above`
 * `selenium version 4.5`
 * `smtplib`

# About The Project 
Bots provide easy pathways to crawl and gather data without much hassle. As a resident of Lagos city, it can be quite arduous getting hotels that fit a certain budget range in a certain part of the city. Using Object Oriented Programming, three methods namely:
* `book_ikeja`
* `book_ikoyi`
* `book_lekki` were created.
These methods each correspond to three major locations in the city. By taking in user's budget and email address as arguments, these methods can crawl the web for hotels in these locations that meet the specifications of the users. 
After crawling and scraping, the hotels found are sent to the user via email  with information about the hotel's name, its address, ratings, price as well as website to book.


# File Description 
The project contains an `hotels` folder that holds four python files used to create the automation task. `Bookings.py` is the main class file that contains the three methods for usage. There are three other files present which `Bookings.py` has inherited methods from for creation of the main methods. 
Utilization of the method may be carried out in main.py by importing the bookings class from bookings.py module and calling the necessary methods with the necessary arguments. This may be carried out on a local machine.

# Licensing And Authoring
This code was created by Jessica Ogwu and is protected under the GNU General Public License. Please feel free to use it in your own projects.
