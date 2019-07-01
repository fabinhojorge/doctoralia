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
from Doctor import Doctor


BASE_DOMAIN = "https://www.doctoralia.com.br"


def init_webdriver_config(impl_delay=30):
    """Function to set the configuration of the Selenium web Driver"""

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

    chrome_driver = webdriver.Chrome(chrome_options=chrome_options)
    chrome_driver.implicitly_wait(impl_delay)
    return chrome_driver


def get_soup_page(_driver, url):
    """Helper function that navigates and returns an BeautifulSoup page"""
    time.sleep(1)
    _driver.get(url)
    return BeautifulSoup(driver.page_source, 'html.parser')


def has_next_pagination(_soup, current_pagination, max_pagination=-1):
    """Function to check if has a next pagination. Extra functionality to limit the max_number of paginations"""
    if max_pagination != -1 and current_pagination >= max_pagination:
        return False
    else:
        return len(_soup.select("ul.pagination li.next")) == 1


def create_doctor(_soup):
    """Helper function to extract information from soup and create the Doctor object"""

    name_select = _soup.select("div.unified-doctor-header-info div.unified-doctor-header-info__name span")[:2]
    name = " ".join(map(lambda x: x.text, name_select))

    image_select = _soup.select("div.unified-doctor-header-info a.avatar")
    image_link = image_select[0]["href"] if len(image_select) > 0 else ""

    specialization = ", ".join(map(lambda x: x.text, _soup.select("div.unified-doctor-header-info h2 a")))

    experiences_select = _soup.find("span", text='Experiência em:')
    if experiences_select is not None:
        experiences_select = experiences_select.parent.parent.parent.parent.find_all("li")
        experiences = ", ".join(map(lambda x: x.text, experiences_select))
    else:
        experiences = ""


    # address
    # telephone

    _doctor = Doctor(name, image_link, specialization, experiences)

    print(_doctor)

    return _doctor


# if __name__ == '__main__':

driver = init_webdriver_config(30)

init_url = "{0}/{1}".format(BASE_DOMAIN, 'especializacoes-medicas')
soup = get_soup_page(driver, init_url)

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
        for doctor_page in doctor_list_per_pagination[:2]:
            url_doctor = doctor_page['href']
            soup = get_soup_page(driver, url_doctor)

            doctor = create_doctor(soup)

        # has_next_pagination
        if not check_next_pagination:
            break

# driver.quit()

print(">> WebCrawler Finished <<")
