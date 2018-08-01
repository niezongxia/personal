#websphere.py coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By

#调用iewebdriver
driver=webdriver.Ie()#Chrome
#登录
driver.get("https://22.188.24.249:9043/ibm/console/logon.jsp")
#driver.get("https://22.188.181.102:9043/ibm/console/logon.jsp")
#driver.get("https://22.188.192.162:9043/ibm/console/logon.jsp")
driver.find_element_by_id("overridelink").click()
driver.find_element_by_id("j_username").send_keys("wasoper")
driver.find_element_by_id("j_password").send_keys("oper#7890")
driver.find_element_by_id("other").click()
#driver.find_element_by_xpath('/html/frameset/frameset/frame/html/body/div/div/table/tbody/tr[2]/td/div[6]/a/span').click()
#driver.find_element_by_xpath('/html/frameset/frameset/frame/html/body/div/div/table/tbody/tr[2]/td/div[7]/div/a/span').click()
#driver.find_element(By.LINK_TEXT,"WebSphere企业应用程序")
#driver.quit()
