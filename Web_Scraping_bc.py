import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


def scrape_beauty_creations_section(navegador, section_name, section_xpath, shop_all_xpath, title_selector,
                                    price_selector, pages=3):
    try:
        section_button = WebDriverWait(navegador, 20).until(
            EC.element_to_be_clickable((By.XPATH, section_xpath))
        )
        section_button.click()
        time.sleep(5)

        shop_all_button = WebDriverWait(navegador, 20).until(
            EC.element_to_be_clickable((By.XPATH, shop_all_xpath))
        )
        shop_all_button.click()
        time.sleep(5)
    except Exception as e:
        return

    data = {"Title": [], "Price": []}

    for pag in range(pages):
        time.sleep(3)
        soup = BeautifulSoup(navegador.page_source, "html.parser")
        products = soup.find_all("div", attrs={"class": "content"})

        for item in products:
            title = item.select_one(title_selector)
            if title:
                data["Title"].append(title.text.strip())
            else:
                data["Title"].append("No title")

            price = item.select_one(price_selector)
            if price:
                data["Price"].append(price.text.strip())
            else:
                data["Price"].append("$0.00")

        if pag < pages - 1:
            try:
                next_button = WebDriverWait(navegador, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "a[aria-label='Next page of products']"))
                )
                next_button.click()
                time.sleep(5)
            except Exception as e:
                break

    df = pd.DataFrame(data)
    df.to_csv(f"datasets/beauty_creations_{section_name}.csv", index=False)


def main():
    s = Service(ChromeDriverManager().install())
    opc = Options()
    opc.add_argument("--window-size=1200,800")
    navegador = webdriver.Chrome(service=s, options=opc)

    navegador.get("https://www.beautycreationscosmetics.com/")
    time.sleep(5)

    scrape_beauty_creations_section(
        navegador,
        "collabs",
        "//div[@data-id='collabs']",
        "//a[contains(text(), 'Shop All Collabs')]",
        "div.title",
        "div.price",
        pages=3
    )

    scrape_beauty_creations_section(
        navegador,
        "accessories",
        "//div[@data-id='accessories']",
        "//a[contains(text(), 'shop all accessories')]",
        "div.title",
        "div.price",
        pages=3
    )

    scrape_beauty_creations_section(
        navegador,
        "bundles",
        "//div[@data-id='bundles']",
        "//a[contains(text(), 'Shop All Bundles')]",
        "div.title",
        "div.price",
        pages=4
    )

    navegador.quit()


if __name__ == "__main__":
    main()
