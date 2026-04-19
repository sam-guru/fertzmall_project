from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pandas as pd



# Configure Chrome options for headless mode
# chrome_options = Options()
# chrome_options.add_argument("--headless") 

# Initialize the WebDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)



# Function to scrape data from a single page
def scrape_page(driver, product_image, product_name, product_price, product_url):
    products = driver.find_elements(By.XPATH,'.//div[contains(@class, "content-product")]')
    for product in products:
        try:
            # Find the image element within the product
            img_element = product.find_element(By.XPATH, './/a[contains(@class, "product-content-image")]//img')
            
            # Get the value of the 'src' attribute of the image
            src_attribute_value = img_element.get_attribute('src')
            product_image.append(src_attribute_value)
            
            product_name.append(product.find_element(By.XPATH, './/h2[contains(@class, "product-title")]//a').text)
            product_price.append(product.find_element(By.XPATH, './/span//span[contains(@class, "amount")]').text)
            
            # Find the link element within the product
            link_element = product.find_element(By.XPATH, './/h2[contains(@class, "product-title")]//a')
            
            # Get the value of the 'href' attribute of the link
            href_attribute_value = link_element.get_attribute('href')
            product_url.append(href_attribute_value)
        except NoSuchElementException:
            pass

# List of URLs to scrape
urls = [
    "https://store.veggieconcept.ng/?s=fertilizer&post_type=product",
    "https://store.veggieconcept.ng/?s=herbicide&post_type=product",
   "https://store.veggieconcept.ng/?s=pesticide&post_type=product",
    "https://store.veggieconcept.ng/?s=fungicide&post_type=product"
]

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
# Initializing the lists to store scraped data
product_image = []
product_name = []
product_price = []
product_url = []

for url in urls:
    driver.get(url)
    while True:
        # Wait for the container to be present
        container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "content-product"))
        )
        # Scrape the current page
        scrape_page(driver, product_image, product_name, product_price, product_url)
        # Check if there is a next page
        try:
            next_page = driver.find_element(By.XPATH, '//a[contains(@class, "next")]')
            next_page_link = next_page.get_attribute('href')
            driver.get(next_page_link)
        except NoSuchElementException:
            break

# Ensure all arrays have the same length
min_length = min(len(product_name), len(product_image), len(product_price), len(product_url))
product_name = product_name[:min_length]
product_image = product_image[:min_length]
product_price = product_price[:min_length]
product_url = product_url[:min_length]

# Create DataFrame
df_books = pd.DataFrame({'Name': product_name, 'Image_URL': product_image, 'Price': product_price, 'URL': product_url })
df_books.to_csv('products.csv', index=False)

driver.quit()
