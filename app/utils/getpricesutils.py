from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import time

def get_webdriver():
    firefox_options = Options()
    firefox_options.add_argument('--headless')
    firefox_options.add_argument('--no-sandbox')
    firefox_options.add_argument('--disable-gpu')
    driver = webdriver.Firefox(options=firefox_options)
    return driver

def c(product_element):
    try:
        product_name = product_element.find_elements(By.CSS_SELECTOR, '[data-qa="caroussel_item_btn_buy"]')[1].text
        price_minor = product_element.find_element(By.CSS_SELECTOR, '[data-qa="price_final_item"]').text
        
        product_info = {
            'product_name': product_name,
            'product_price': price_minor
        }
        
        return product_info
    except Exception as e:
        print(f"Erro ao extrair informações do produto: {str(e)}")
        return None
    
def search_product_araujo(product):
    driver = get_webdriver()
    driver.maximize_window()
    driver.get("https://www.araujo.com.br/")
    driver.execute_script("window.scrollTo(0, 500);")
    
    try:
        time.sleep(10)
        
        input_element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "q")))
        input_element.send_keys(product)
        input_element.send_keys(Keys.ENTER)
        time.sleep(10)
        product_containers = driver.find_elements(By.CLASS_NAME, 'productTile')
        
        # Loop through each product container and extract name and price
        for container in product_containers:
            product_name_element = driver.find_element(By.CLASS_NAME, 'productTile__name')
            product_name = product_name_element.text.strip()

            # Extract product price
            product_price_element = driver.find_element(By.CLASS_NAME, 'productPrice__price')
            product_price = product_price_element.text.strip()
            
            product_info = {
            'product_name': product_name,
            'product_price': product_price
            }
            break
        driver.quit()
        return product_info

    except:
        return "Erro durante a busca"

def search_product_drogal(product, 
                   url,
                   searchHeader):
    driver = get_webdriver()
    driver.maximize_window()
    driver.get(url)
    driver.execute_script("window.scrollTo(0, 1500);")
    
    try:
        input_element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, searchHeader)))

        input_element.send_keys(product)
        input_element.send_keys(Keys.ENTER)
        
        time.sleep(10)
        
        product_containers = driver.find_elements(By.CLASS_NAME, 'item-product')

        # Loop through each product container and extract name and price
        for container in product_containers:
            product_name = container.find_element(By.CLASS_NAME, 'title').text.strip()
            product_price = container.find_element(By.CLASS_NAME, 'sale-price').text.strip()

            product_info = {
            'product_name': product_name,
            'product_price': product_price
            }

            break
        driver.quit()
        return product_info

    except:
        return "Erro durante a busca"
    


def search_product_drogasmil(product):
    driver = get_webdriver()              
    driver.maximize_window()
    driver.get(f"https://www.drogasmil.com.br/{product}")
    driver.execute_script("window.scrollTo(0, 1500);")
    
    try:
        
        time.sleep(10)
        
        product_containers = driver.find_elements(By.CLASS_NAME, 'vtex-search-result-3-x-galleryItem')

        # Loop through each product container and extract name and price
        for container in product_containers:
            product_name = container.find_element(By.CLASS_NAME, 'vtex-product-summary-2-x-productBrand').text.strip()
            product_price = container.find_element(By.CLASS_NAME, 'vtex-product-price-1-x-sellingPriceValue').text.strip()

            product_info = {
            'product_name': product_name,
            'product_price': product_price
            }

            break
        driver.quit()
        return product_info

    except:
        return "Erro durante a busca"
    
def search_product_dsp(product):
    
    time.sleep(5)
    driver = get_webdriver()    
    driver.maximize_window()
    driver.get("https://www.drogariasaopaulo.com.br/")

    input_element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/div[1]/div/div/div[3]/form/fieldset/div/input")))
    input_element.send_keys(product)
    input_element.send_keys(Keys.ENTER)
    driver.execute_script("window.scrollTo(0, 500);")
    time.sleep(10)
    product_containers = driver.find_elements(By.CLASS_NAME, 'is-referencia')

    try:
        # Loop through each product container and extract name and price
        for container in product_containers:
            product_name = container.find_element(By.CLASS_NAME, 'collection-link').text.strip()
            product_price = container.find_element(By.CLASS_NAME, 'valor-por').text.strip()

            product_info = {
            'product_name': product_name,
            'product_price': product_price
            }

            break
        driver.quit()
        return product_info

    except:
        time.sleep(5)
        driver.quit()
        return "Erro durante a busca"

   
def search_product_extrafarma(product):
    driver = get_webdriver()           
    driver.maximize_window()
    driver.get(f"https://www.extrafarma.com.br/busca?origin=autocomplete&ranking=1&termo={product}")
    
    try:
        time.sleep(10)
        product_containers = driver.find_elements(By.CLASS_NAME, 'extrafarmav2-store-theme-2-x-search-custom-products-galerryItem')
        for container in product_containers:
            product_name = container.find_element(By.CLASS_NAME, 'extrafarmav2-store-theme-2-x-search-custom-products-name-span').text.strip()
            product_price = container.find_element(By.CLASS_NAME, 'extrafarmav2-store-theme-2-x-price').text.strip()

            product_info = {
            'product_name': product_name,
            'product_price': product_price
            }

            break
        driver.quit()
        return product_info

    except:
        driver.quit()
        return "Erro durante a busca"
    
def search_product_globo(product):
    driver = get_webdriver()           
    driver.maximize_window()
    driver.get(f"https://www.drogariaglobo.com.br/#&search-term={product}")
    
    try:
        
        time.sleep(10)
        
        product_containers = driver.find_elements(By.CLASS_NAME, 'apoio-sh')

        # Loop through each product container and extract name and price
        for container in product_containers:
            product_name = container.find_element(By.CLASS_NAME, 'vtex-product-summary-2-x-productBrand').text.strip()
            product_price = container.find_element(By.CLASS_NAME, 'vtex-product-price-1-x-sellingPriceValue').text.strip()

            product_info = {
            'product_name': product_name,
            'product_price': product_price
            }

            break
        driver.quit()
        return product_info

    except:
        driver.quit()
        return "Erro durante a busca"
  
def search_product_nissei(product):
    driver = get_webdriver()          
    driver.maximize_window()
    driver.get(f"https://www.farmaciasnissei.com.br/pesquisa/{product}")
    
    try:
        time.sleep(10)
        product_containers = driver.find_elements(By.CLASS_NAME, "col-md-3")
        # Loop through each product container and extract name and price
        for container in product_containers:

            product_name = container.find_element(By.CLASS_NAME, 'text-body').text.strip()
            product_price = container.find_element(By.CSS_SELECTOR, "p[style*='var(--textoPrecoPrincipal)']").text.strip()

            product_info = {
            'product_name': product_name,
            'product_price': product_price
            }
            break
        driver.quit()
        return product_info

    except:
        time.sleep(5)
        driver.quit()
        return "Erro durante a busca"

def search_product_pacheco(product):
    time.sleep(5)
    driver = get_webdriver()    
    driver.maximize_window()
    driver.get("https://www.drogariaspacheco.com.br/")

    input_element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/header/div[1]/div/div/div[3]/form/fieldset/div/input")))
    input_element.send_keys(product)
    input_element.send_keys(Keys.ENTER)
    driver.execute_script("window.scrollTo(0, 500);")
    time.sleep(10)
    product_containers = driver.find_elements(By.CLASS_NAME, 'is-similar')

    try:
        # Loop through each product container and extract name and price
        for container in product_containers:
            product_name = container.find_element(By.CLASS_NAME, 'collection-link').text.strip()
            product_price = container.find_element(By.CLASS_NAME, 'valor-por').text.strip()

            product_info = {
            'product_name': product_name,
            'product_price': product_price
            }

            break
        driver.quit()
        return product_info

    except:
        time.sleep(5)
        driver.quit()
        return "Erro durante a busca"

def search_product_paguemenos(product):
    driver = get_webdriver()          
    driver.maximize_window()
    driver.get(f"https://www.paguemenos.com.br/busca?termo={product}")
    
    try:
        time.sleep(10)
        
        product_containers = driver.find_elements(By.CLASS_NAME, 'paguemenos-store-theme-2-x-search-custom-products-galerryItem')

        # Loop through each product container and extract name and price
        for container in product_containers:
            product_name = container.find_element(By.CLASS_NAME, 'paguemenos-store-theme-2-x-search-custom-products-name-span').text.strip()
            product_price = container.find_element(By.CLASS_NAME, 'paguemenos-store-theme-2-x-price').text.strip()

            product_info = {
            'product_name': product_name,
            'product_price': product_price
            }

            break
        driver.quit()
        return product_info

    except:
        driver.quit()
        return "Erro durante a busca"


def search_product_panvel(product):
    driver = get_webdriver()        
    driver.maximize_window()
    driver.get(f"https://www.panvel.com/panvel/buscarProduto.do?termoPesquisa={product}")
    
    try:
        time.sleep(10)
        
        product_containers = driver.find_elements(By.CLASS_NAME, 'ng-star-inserted')

        # Loop through each product container and extract name and price
        for container in product_containers:
            product_name = container.find_element(By.CLASS_NAME, 'item-name').text.strip()
            product_price = container.find_element(By.CLASS_NAME, 'price').text.strip()

            product_info = {
            'product_name': product_name,
            'product_price': product_price
            }

            break
        driver.quit()
        return product_info

    except:
        driver.quit()
        return "Erro durante a busca"
    
def search_product_rosario(product):
    try:
        driver = get_webdriver()  
        driver.get("https://www.drogariarosario.com.br/")
        input_element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "downshift-0-input")))

        input_element.send_keys(product)
        input_element.send_keys(Keys.ENTER)
        time.sleep(10)
        
        product_containers = driver.find_elements(By.CLASS_NAME, 'vtex-search-result-3-x-galleryItem')
        # Loop through each product container and extract name and price
        for container in product_containers:#
            product_name = container.find_element(By.CLASS_NAME, 'vtex-product-summary-2-x-productBrand').text.strip()
            product_price = container.find_element(By.CLASS_NAME, 'vtex-product-price-1-x-sellingPriceValue--shelf-default').text.strip()

            product_info = {
            'product_name': product_name,
            'product_price': product_price
            }
            break
        driver.quit()
        return product_info

    except:
        print("Erro durante a busca")
        return "erro"
    

def search_product_tamoio(product):
    driver = get_webdriver()          
    driver.get("https://www.drogariastamoio.com.br/")
    input_element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "downshift-0-input")))

    input_element.send_keys(product)
    input_element.send_keys(Keys.ENTER)
    time.sleep(5)
    
    try:
        time.sleep(10)
        
        product_containers = driver.find_elements(By.CLASS_NAME, 'vtex-search-result-3-x-galleryItem')

        # Loop through each product container and extract name and price
        for container in product_containers:#
            product_name = container.find_element(By.CLASS_NAME, 'vtex-product-summary-2-x-productBrand').text.strip()
            product_price = container.find_element(By.CLASS_NAME, 'vtex-product-price-1-x-sellingPriceValue--shelf-default').text.strip()

            product_info = {
            'product_name': product_name,
            'product_price': product_price
            }

            break
        driver.quit()
        return product_info

    except:
        driver.quit()
        return "Erro durante a busca"
    
 
def search_product_indiana(product):
    driver = get_webdriver()   
    driver.maximize_window()
    driver.get(f"https://www.farmaciaindiana.com.br/{product}")
    
    try:
        time.sleep(10)
        product_containers = driver.find_elements(By.CLASS_NAME, "vtex-search-result-3-x-galleryItem")
        for container in product_containers:
            product_name = container.find_element(By.CLASS_NAME, "vtex-product-summary-2-x-productBrand").text.strip()
            product_price = container.find_element(By.CLASS_NAME, "vtex-product-price-1-x-spotPrice").text.strip()

            product_info = {
            'product_name': product_name,
            'product_price': product_price
            }

            break
        driver.quit()
        return product_info

    except:
        driver.quit()
        return "Erro durante a busca"
    


def search_product_sj(product):
    driver = get_webdriver()              
    driver.maximize_window()
    driver.get(f"https://www.saojoaofarmacias.com.br/{product}")
    time.sleep(10)
    
    try:
        product_containers = driver.find_elements(By.CLASS_NAME, 'vtex-search-result-3-x-galleryItem')

        # Loop through each product container and extract name and price
        for container in product_containers:#
            product_name = container.find_element(By.CLASS_NAME, 'vtex-product-summary-2-x-productBrand').text.strip()
            product_price = container.find_element(By.CLASS_NAME, 'sjdigital-custom-apps-0-x-sellingPrice').text.strip()

            product_info = {
            'product_name': product_name,
            'product_price': product_price
            }

            break
        driver.quit()
        return product_info

    except:
        driver.quit()
        return "Erro durante a busca"
    

def search_product_catarinense(product):
    driver = get_webdriver()  
    driver.maximize_window()
    driver.get(f"https://www.drogariacatarinense.com.br/search?q={product}")
    
    try:
        time.sleep(10)
        shadow_host2 = driver.find_element(By.CSS_SELECTOR, "#main > impulse-search:nth-child(1)")
        shadow_root2 = driver.execute_script('return arguments[0].shadowRoot', shadow_host2)
        product_containers = shadow_root2.find_elements(By.CSS_SELECTOR, ".content")
        
        for container in product_containers:
            description = container.find_element(By.CLASS_NAME, "impulse-title").text.strip()
            price_element = container.find_element(By.CLASS_NAME, "impulse-currency").text.strip()
            
            product_info = {
            'product_name': description,
            'product_price': price_element
            }
            break
        driver.quit()
        return product_info

    except:
        driver.quit()
        return "Erro durante a busca"
    
def search_product_precopopular(product):
    driver = get_webdriver()  
    driver.maximize_window()
    driver.get(f"https://www.precopopular.com.br/search?q={product}")
    
    try:
        time.sleep(10)
        shadow_host2 = driver.find_element(By.CSS_SELECTOR, "#main > impulse-search:nth-child(1)")
        shadow_root2 = driver.execute_script('return arguments[0].shadowRoot', shadow_host2)
        product_containers = shadow_root2.find_elements(By.CSS_SELECTOR, ".content")
        
        for container in product_containers:
            description = container.find_element(By.CLASS_NAME, "impulse-title").text.strip()
            price_element = container.find_element(By.CLASS_NAME, "impulse-currency").text.strip()
            
            product_info = {
            'product_name': description,
            'product_price': price_element
            }
            break
        driver.quit()
        return product_info

    except:
        driver.quit()
        return "Erro durante a busca"
    

def search_product_venancio(product):
    driver = get_webdriver() 
    driver.maximize_window()
    driver.get(f"https://www.drogariavenancio.com.br/search?q={product}")
    
    try:
        time.sleep(10)
        shadow_host2 = driver.find_element(By.CSS_SELECTOR, ".vtex-flex-layout-0-x-flexRowContent--blank-template > div:nth-child(1) > impulse-search:nth-child(1)")
        shadow_root2 = driver.execute_script('return arguments[0].shadowRoot', shadow_host2)
        product_containers = shadow_root2.find_elements(By.CSS_SELECTOR, "#products > div:nth-child(1) > div > div")
        
        for container in product_containers:
            description = container.find_element(By.CLASS_NAME, "impulse-title").text.strip()
            price_element = container.find_element(By.CLASS_NAME, "impulse-currency").text.strip()
            
            product_info = {
            'product_name': description,
            'product_price': price_element
            }
            break
        driver.quit()
        return product_info

    except:
        driver.quit()
        return "Erro durante a busca"











