from selenium import webdriver

path = "C:\\Users\\aryan\\Downloads\\Compressed\\chromedriver.exe"
driver = webdriver.Chrome(path)
url = "https://www.amazon.in/gp/product/B00SAYCXWG?pf_rd_r=TPY41SEHTE1JMJ0TWVKN&pf_rd_p=649eac15-05ce-45c0-86ac-3e413b8ba3d4"
driver.get(url)

wishlist = driver.find_element_by_xpath('//*[@id="wishListMainButton-announce"]')
wishlist.click()

email_box = driver.find_element_by_id("ap_email")
email_box.send_keys('YOUR EMAIL ID')

continue_btn = driver.find_element_by_xpath('//*[@id="continue"]')
continue_btn.click()

password_inputBox = driver.find_element_by_xpath('//*[@id="ap_password"]')
password_inputBox.send_keys('YOUR PASSWORD')

loginButton = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
loginButton.click()

wishlistButton = driver.find_element_by_xpath('//*[@id="add-to-wishlist-button-submit"]')
wishlistButton.click()
