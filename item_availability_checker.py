from selenium import webdriver
from selenium.webdriver.common.by import By

store = ["BestBuy", "Amazon", "Walmart", "GameStop", "The Source"]

urls = ["https://www.bestbuy.ca/en-ca/product/playstation-5-console/15689336",
        "https://www.amazon.ca/Playstation-3006648-PlayStation-Disc-Edition/dp/B09DPJ2TGW/ref=sr_1_1?crid=3491EZ2WDSPKT&keywords=ps5&qid=1642142070&sprefix=p%2Caps%2C197&sr=8-1",
        "https://www.walmart.ca/en/ip/playstation5-console/6000202198562",
        "https://www.gamestop.ca/PS5/Games/877522/playstation-5-only-available-for-purchase-in-a-bundle",
        "https://www.thesource.ca/en-ca/p/108090498"]

xpaths = ["//*[@id='root']/div/div[4]/div[2]/div[1]/div[2]/div[3]/div[1]/div/button", "//*[@id='add-to-cart-button']",
          "/html/body/div[1]/div/div[4]/div/div/div[1]/div[3]/div[2]/div/div[2]/div[2]/div/button[1]",
          "//*[@id='prodMain']/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div[3]/div",
          "//*[@id='addToCartButton']"]

driver = webdriver.Chrome()

for i in range(5):
    driver.get(urls[i])

    try:
        addToCartBtn = driver.find_element(By.XPATH, xpaths[i])
        print(store[i] + " - Item available")
    except:
        print(store[i] + " - Not available")

driver.close()
driver.quit()
