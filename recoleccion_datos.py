from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def setup_selenium():
    options = Options()
    options.add_argument("--headless")

    service = Service("C:/chromedriver/chromedriver.exe")

    driver = webdriver.Chrome(
        service=service,
        options=options
    )

    return driver

def collect_data(driver, url):
    driver.get(url)
    time.sleep(5)

    tweets = driver.find_elements(
        By.CSS_SELECTOR,
        "article"
    )

    data = [tweet.text for tweet in tweets]
    return data

if __name__ == "__main__":
    print("Módulo de recolección cargado correctamente")