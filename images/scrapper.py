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


# def break_apart(index: int):
#     pokemon_set_urls = []
#     chrome_options = Options()
#     chrome_options.add_argument("--headless=new")
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.get("https://www.psacard.com/priceguide/non-sports-tcg-card-values/7")
#     searches = driver.find_elements(By.XPATH, '//td/a')
#     for search in searches:
#         if "pokémon" in search.text.lower():
#             pokemon_set_urls.append(search.get_attribute("href"))
#     return pokemon_set_urls[index:]

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
    searches = driver.find_elements(By.XPATH, '//td/a')[::-1]
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
            link_elements = driver.find_elements(By.XPATH, "//tr/td[6]")

            for index, link_element in enumerate(link_elements, start=1):
                # Get the value of column 6
                try:
                    column_6_value = int(link_element.text.strip())

                    # Check if the value of column 6 is greater than 30
                    if column_6_value > 50:
                        # Find the corresponding link in column 5 using the row index
                        link_element_column_5 = driver.find_element(By.XPATH, f"//tr[{index}]/td[3]/a")
                        link_url = link_element_column_5.get_attribute("href")
                        table_urls.append(link_url)
                except ValueError:
                    pass
            for final_url in table_urls:
                # FINAL URL IS URL TO TABLE
                driver.get(final_url)
                # MATCHES GRADES
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="itemResults"]/tbody/tr'))
                )
                search_table = driver.find_elements(By.XPATH, f'//*[@id="itemResults"]/tbody/tr')
                for index, row in enumerate(search_table, start=1):
                    try:
                        row_grade = driver.find_element(By.XPATH,
                                                        f'//*[@id="itemResults"]/tbody/tr[{index}]/td[5]').text
                        row_image = driver.find_element(
                            By.XPATH, f'//*[@id="itemResults"]/tbody/tr[{index}]/td/a').get_attribute("href")
                        if row_image.startswith("https://"):
                            grades.append(row_grade)
                            images.append(row_image)
                            if len(images) > saved_counter:
                                saved_counter += 500
                                cwd = os.getcwd()
                                save_to_csv(images, grades, cwd + "/data" + str(saved_counter_url) + ".csv")
                                saved_counter_url += 1
                    except NoSuchElementException:
                        pass

                else:
                    print("some mismatch")
                print(grades, images, len(images), len(images) == len(grades))

        except StaleElementReferenceException:
            images.append(0)
            grades.append(0)
    # dictt = pd.DataFrame({'grade': grades, 'images': images})
    # dictt.to_csv("C:/Users/KAIXI/PycharmProjects/WebScraper2/good.csv")


steal_data("https://www.psacard.com/priceguide/non-sports-tcg-card-values/7", "pokemon")