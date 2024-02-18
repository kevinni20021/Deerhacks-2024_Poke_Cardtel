from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def name_lookup(name: str, grade: int) -> str:
    if grade <= 5:
        return "Low Grade"
    chrome_options = Options()
    # chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.google.ca/")
    search = driver.find_element(By.NAME, "q")
    search.send_keys(name)
    search.send_keys(Keys.RETURN)

    try:
        # Wait for the search results container to be present in the DOM
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'search'))
        )

        # Assuming you are looking for a link to a specific website in the search results
        # Replace 'Your Target Website' with the actual name or URL of the website you are waiting for
        target_website_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "https://www.pricecharting.com"))
        )
        target_website_link.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="full-prices"]/table/tbody/tr[{grade + 1}]/td[2]'))
        )
        if grade == 10:
            search = driver.find_element(By.XPATH, f'//*[@id="full-prices"]/table/tbody/tr[{grade + 2}]/td[2]')
            return search.text
        search = driver.find_element(By.XPATH, f'//*[@id="full-prices"]/table/tbody/tr[{grade + 1}]/td[2]')
        return search.text

    except TimeoutError:
        return "Does Not Exist"


print(name_lookup("charizard ex 223", 10))

