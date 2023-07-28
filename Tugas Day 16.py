from selenium import webdriver
import time

# Inisialisasi WebDriver
driver = webdriver.Chrome()

# Kasus Uji 1: Mencari produk di Amazon
def test_amazon_search():
    driver.get("https://www.amazon.com/")
    search_box = driver.find_element_by_id("twotabsearchtextbox")
    search_box.send_keys("laptop")
    search_box.submit()
    time.sleep(3)  # Tunggu beberapa saat untuk memastikan hasilnya muncul
    assert "laptop" in driver.title.lower()
    print("Test case 1: Amazon Search - Passed")

# Kasus Uji 2: Menambahkan produk ke keranjang belanja
def test_amazon_add_to_cart():
    driver.get("https://www.amazon.com/")
    search_box = driver.find_element_by_id("twotabsearchtextbox")
    search_box.send_keys("smartphone")
    search_box.submit()
    time.sleep(3)  # Tunggu beberapa saat untuk memastikan hasilnya muncul

    product = driver.find_element_by_css_selector(".s-result-item h2 a")
    product.click()
    time.sleep(3)  # Tunggu beberapa saat untuk memastikan halaman produk terbuka

    add_to_cart_button = driver.find_element_by_id("add-to-cart-button")
    assert add_to_cart_button.is_displayed() and add_to_cart_button.is_enabled()
    add_to_cart_button.click()
    time.sleep(3)  # Tunggu beberapa saat untuk memastikan produk ditambahkan ke keranjang
    assert "Added to Cart" in driver.page_source
    print("Test case 2: Amazon Add to Cart - Passed")

# Kasus Uji 3: Verifikasi detail produk di keranjang belanja
def test_amazon_cart_details():
    driver.get("https://www.amazon.com/gp/cart/view.html")
    time.sleep(3)  # Tunggu beberapa saat untuk memastikan halaman keranjang terbuka

    cart_items = driver.find_elements_by_css_selector(".sc-product-title")
    assert len(cart_items) > 0
    print("Test case 3: Amazon Cart Details - Passed")

# Menjalankan kasus uji
test_amazon_search()
test_amazon_add_to_cart()
test_amazon_cart_details()

# Tutup browser setelah selesai
driver.quit()
