from selenium import webdriver
from selenium.webdriver.common.keys import keys
from time import sleep

driver = webdriver.Chrome(executable_path="/Users/61497/Downloads/chromedriver")

driver.get("https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27")
sleep(5)
driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
driver.find_element_by_xpath('//input[@type="email"]').send_keys("email here")
driver.find_element_by_xpath('//*[id@="identifierNext"]').click()
sleep(5)
driver.find_element_by_xpath('//input[@type="password"]').send_keys("password here")
driver.find_element_by_xpath('//*[id@="passwordNext"]').click()
sleep(5)
driver.get("https://mail.google.com")
sleep(5)
for i  in range(20):
    driver.get("https://mail.google.com/mail/u/0/#inbox?compose=new")
    sleep(2)
    driver.find_element_by_class_name("v0").send_keys("recipient here")
    driver.find_element_by_class_name("aoT").send_keys("subject here")
    driver.find_element_by_css_selector("div[aria=label='Message Body']").send_keys("Text Here")
    driver.find_element_by_xpath("//div[text()='Send']").click()
    sleep(3)