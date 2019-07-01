
# Doctolaria Web Crawler 

It is a web Crawler and Scraper to extract data from doctolaria site.

The informations collected are:
- Name
- Image_link
- Address
- Address_telephone
- Specializations
- Experiences


## How to install and Run
After activate your Python Virtual Environment (_venv_) run the below command to install the dependencies:

```
pip install -r requirements.txt
```

## Libraries and files
* __chromedriver.exe__ - Web driver used by Selenium to call Chrome. This executable is for Windows x64. ___If you are not confident to use this .exe file, OR have another Operation System___, you can download the correct version at [Selenium Chrome webdriver](http://chromedriver.chromium.org/downloads) 


## How to use
```
python DoctoraliaWebCrawler.py
```



 
## Observations about the target site
* The pagination are limited to 100 pages and locked to 20 doctors per page
* A doctor can have multiple addresses. In this project we are only extracting the __First__ Address and the Telephones for this address 