#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: Fabio Rodrigues Jorge
Email: fabinhojorgenet@gmail.com
Description: Web Crawler to extract information from Doctoralia site
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time


BASE_DOMAIN = "https://www.doctoralia.com.br"


def init_webdriver_config(impl_delay=30):
    """Function to set the configuration of the Selenium web Driver"""

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

    chrome_driver = webdriver.Chrome(chrome_options=chrome_options)
    chrome_driver.implicitly_wait(impl_delay)
    return chrome_driver


def get_soup_page(_driver, url):
    _driver.get(url)
    return BeautifulSoup(driver.page_source, 'html.parser')


def has_next_pagination(_soup, current_pagination, max_pagination=-1):
    """Function to check if has a next pagination. Extra functionality to limit the max_number of paginations"""
    if max_pagination > -1 and current_pagination >= max_pagination:
        return False
    else:
        return len(_soup.select("ul.pagination li.next")) == 1


# if __name__ == '__main__':

driver = init_webdriver_config(30)

init_url = BASE_DOMAIN + '/especializacoes-medicas'

driver.get(init_url)
soup = BeautifulSoup(driver.page_source, 'html.parser')

specialization_list = soup.select("div section div h3 div a.text-muted")

for spe in specialization_list[5:7]:
    pagination = 0
    while True:
        pagination += 1
        next_url = "{0}{1}/{2}".format(BASE_DOMAIN, spe["href"], pagination)
        soup = get_soup_page(driver, next_url)

        check_next_pagination = has_next_pagination(soup, pagination, max_pagination=2)
        doctor_list_per_pagination = soup.select("a.rank-element-name__link")

        # get doctor list per page
        for doctor in doctor_list_per_pagination[:2]:
            time.sleep(1)
            url_doctor = doctor['href']
            driver.get(url_doctor)
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            # Doctor
            name = " ".join(map(lambda x: x.text,
                                soup.select("div.unified-doctor-header-info div.unified-doctor-header-info__name span")
                                [:2]))
            image_select = soup.select("div.unified-doctor-header-info a.avatar")
            image_link = image_select[0]["href"] if len(image_select) > 0 else ""
            specialization = ", ".join(map(lambda x: x.text, soup.select("div.unified-doctor-header-info h2 a")))
            # experiences
            # address
            # telephone
            # image link

            print("Doctor: ", name, " - ", specialization, " - Image: ", image_link)

        # has_next_pagination
        if not check_next_pagination:
            break

# driver.quit()

print(">> WebCrawler Finished <<")
