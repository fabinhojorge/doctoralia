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
import datetime
import csv
from Doctor import Doctor


BASE_DOMAIN = "https://www.doctoralia.com.br"

# Variables to help to control the application.
DOCTOR_LIST_THRESHOLD = 999
SPECIALIZATION_LIST_THRESHOLD = 999
MAX_PAGINATION = -1  # -1 means unlimited


def init_webdriver_config(impl_delay=30):
    """Function to set the configuration of the Selenium web Driver"""

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

    chrome_driver = webdriver.Chrome(chrome_options=chrome_options)
    chrome_driver.implicitly_wait(impl_delay)
    return chrome_driver


def get_soup_page(_driver, url):
    """Helper function that navigates and returns an BeautifulSoup page"""
    _driver.get(url)
    time.sleep(2)
    return BeautifulSoup(driver.page_source, 'html.parser')


def has_next_pagination(_soup, current_pagination, max_pagination=-1):
    """Function to check if has a next pagination. Extra functionality to limit the max_number of paginations"""
    if max_pagination != -1 and current_pagination >= max_pagination:
        return False
    else:
        return len(_soup.select("ul.pagination li.next")) == 1


def create_doctor(_soup):
    """Helper function to extract information from soup and create the Doctor object"""

    # name_select = _soup.select("div.unified-doctor-header-info div.unified-doctor-header-info__name span")[:2]
    name_select = _soup.select_one("div.unified-doctor-header-info div.unified-doctor-header-info__name")\
        .find(itemprop="name")
    name = name_select.text

    image_select = _soup.select("div.unified-doctor-header-info a.avatar")
    image_link = image_select[0]["href"] if len(image_select) > 0 else ""

    specialization = ", ".join(map(lambda x: x.text, _soup.select("div.unified-doctor-header-info h2 a")))

    experiences_select = _soup.find("span", text='Experiência em:')
    if experiences_select is not None:
        experiences_select = experiences_select.parent.parent.parent.parent.find_all("li")
        experiences = ", ".join(map(lambda x: x.text, experiences_select))
    else:
        experiences = ""

    address_select = _soup.select_one("div.calendar-address")
    if address_select is not None:
        city_select = address_select.select_one("span.city")
        city = city_select['content'] if city_select is not None else ""
        state_select = address_select.select_one("span.region")
        state = state_select['content'] if state_select is not None else ""
        address_select = address_select.select_one("span.street")
        address = address_select.text if address_select is not None else ""
    else:
        city = ""
        state = ""
        address = ""
    telephone_select = soup.select_one("div.calendar-address div.modal i.svg-icon__phone")
    if telephone_select is not None:
        telephone = telephone_select.parent.find("b").text.strip()
    else:
        telephone = ""

    _doctor = Doctor(name=name, image_link=image_link, specialization=specialization, experiences=experiences,
                     city=city, state=state, address=address, telephone=telephone)

    print(_doctor)

    return _doctor


# if __name__ == '__main__':

driver = init_webdriver_config(30)

doctors = []

init_url = "{0}/{1}".format(BASE_DOMAIN, 'especializacoes-medicas')
soup = get_soup_page(driver, init_url)

specialization_list = soup.select("div section div h3 div a.text-muted")

for spe in specialization_list[:SPECIALIZATION_LIST_THRESHOLD]:
    page = 0
    while True:
        page += 1
        next_url = "{0}{1}/{2}".format(BASE_DOMAIN, spe["href"], page)
        soup = get_soup_page(driver, next_url)

        check_next_pagination = has_next_pagination(soup, page, max_pagination=MAX_PAGINATION)
        doctor_list_per_pagination = soup.select("a.rank-element-name__link")

        # get doctor list per page
        for doctor_page in doctor_list_per_pagination[:DOCTOR_LIST_THRESHOLD]:
            url_doctor = doctor_page['href']
            soup = get_soup_page(driver, url_doctor)

            try:
                doctor = create_doctor(soup)
                doctors.append(doctor)
            except Exception as err:
                print("Failed to extract doctor due to {0}".format(err))

        # has_next_pagination
        if not check_next_pagination:
            break


file_name = "{0}_{1}.csv".format('doctoralia_extract', datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S"))
with open(file_name, 'w', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(Doctor.CSV_HEADER)

    for doc in doctors:
        writer.writerow(doc.to_csv())

driver.quit()

print(">> WebCrawler Finished <<")
