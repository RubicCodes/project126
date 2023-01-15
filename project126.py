from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time

start_url = 'https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
browser_url = webdriver.Chrome('chromedriver.exe')
browser_url.get(start_url)

time.sleep(10)


def scrape():
    headers = ["name","light_years_from_earth","planet_mass","stellar_magnitude","discovery_data"]
    planet_data = []

    for i in range(0,428):
        soup = BeautifulSoup(browser_url.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attra = ["class","exoplanet"]): 
            li_tag in soup.find_all("11")
            temp_list = []
            for index, li_tag in enumerate(li_tag):
                if index == 0:
                    temp_list.append(li_tag.content[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
        browser_url.find_elemet_by_xpath('//*[@id="primary_column"]/footer/div/span/a').click()
    with open("scrapper_2.csv","w")as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csv.writer.writerows(planet_data)
scrape()

