#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: Fabio Rodrigues Jorge
Email: fabinhojorgenet@gmail.com
Description: This project was created as part of the job interview for Serasa Experian.
It´s a Web Scraper using Selenium and BeautifulSoup4 to collect temperature data from www.climatempo.com.br site.

The project is divided in 3 parts:
1st - Collect of the city codes
2nd - Collect of the information for each city code
3rd - Output information in different types: TextPlain, Json or CSV

Requirements:
- Install BeautifulSoup4
- Install Selenium
- Download and keep in the same folder the Chrome Web Driver


"""

from selenium import webdriver
# from bs4 import BeautifulSoup


def init_webdriver_config(impl_delay=30):
    """Function to set the configuration of the Selenium web Driver"""

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

    chrome_driver = webdriver.Chrome(chrome_options=chrome_options)
    chrome_driver.implicitly_wait(impl_delay)
    return chrome_driver


if __name__ == '__main__':

    print(" >> WebCrawler Started <<")

    # Set the preferences of the WebDriver. Changed the driver options to block the notifications
    driver = init_webdriver_config(30)

    init_url = 'https://www.doctoralia.com.br/especializacoes-medicas'
    driver.get(init_url)

    driver.quit()

    print(">> WebCrawler Finished <<")
