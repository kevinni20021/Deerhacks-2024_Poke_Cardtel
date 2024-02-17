import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, WebDriverException
import csv

from selenium.common import NoSuchElementException, TimeoutException


def save_to_csv(array1, array2, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Images', 'Grades'])  # Write header if needed
        for i in range(min(len(array1), len(array2))):
            writer.writerow([array1[i], array2[i]])


def steal_data(url: str, target: str):
    # want to save every 500
    saved_counter = 500
    saved_counter_url = 0

    # bunch of these are useless
    grades = []
    pokemon_set_urls = []
    table_urls = []
    images = []
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    searches = driver.find_elements(By.XPATH, '//td/a')
    for search in searches:
        if "pokémon" in search.text.lower():
            pokemon_set_urls.append(search.get_attribute("href"))
    for link in pokemon_set_urls:
        driver.get(link)
        # CLICK APR BUTTON
        try:
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "section-icon-apr")))
            element.click()
        except WebDriverException:
            pass
        # WAIT FOR SITE TO LOAD
        try:
            # FIND THE LINKS TO ALL AUCTIONS
            link_elements = driver.find_elements(By.XPATH, "//td/a")
            # APPEND THE LINK TO TABLES
            for link_e in link_elements:
                table_urls.append(link_e.get_attribute("href"))

            for final_url in table_urls:
                # FINAL URL IS URL TO TABLE
                driver.get(final_url)
                # MATCHES GRADES
                WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="itemResults"]/tbody/tr/td[5]')))
                d_searches = driver.find_elements(By.XPATH, '//*[@id="itemResults"]/tbody/tr/td[5]')
                # CHECKS IF IMAGES = NUM GRADED
                grade_check = []
                c_check = []
                for dsearch in d_searches:
                    try:
                        grade_check.append(dsearch.text)
                    except NoSuchElementException:
                        grade_check.append(0)
                c_searches = driver.find_elements(By.XPATH, "//td/a")
                for csearch in c_searches:
                    try:
                        if not csearch.get_attribute("href").startswith('https://www.psacard.com/auctionprices'):
                            c_check.append(csearch.get_attribute("href"))
                    except NoSuchElementException:
                        c_check.append(0)
                if len(c_check) == len(grade_check):
                    grades += grade_check
                    images += c_check
                    if len(images) > saved_counter:
                        saved_counter += 500
                        cwd = os.getcwd()
                        save_to_csv(images, grades, cwd + "/data" + str(saved_counter_url) + ".csv")
                        saved_counter_url += 1
                else:
                    print("some mismatch")
                print(grades, images, len(images), len(images) == len(grades))

        except StaleElementReferenceException:
            images.append(0)
            grades.append(0)
    # dictt = pd.DataFrame({'grade': grades, 'images': images})
    # dictt.to_csv("C:/Users/KAIXI/PycharmProjects/WebScraper2/good.csv")


steal_data("https://www.psacard.com/priceguide/non-sports-tcg-card-values/7", "pokemon")
