import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from config.settings import CHROME_PATH

driver = webdriver.Chrome(executable_path=CHROME_PATH)

class TestRadioButton():
    #def getDriver(self):
    driver.get("http://demo.guru99.com/test/radio.html")

    def selectElements(self, list):
        #self.getDriver()

        for i in list:
            if i.is_selected():
                print(i.get_attribute("value") + " checked")
            else:
                i.click()
                print(i.get_attribute("value") + " was checked")
                time.sleep(5)

    def radioButton(self):
        #self.getDriver()
        radio = driver.find_elements_by_xpath("//input[@type='radio']")

        self.selectElements(radio)


    def testcheckBox(self):
        #self.getDriver()
        #driver.get("http://demo.guru99.com/test/radio.html")
        checkbox = driver.find_elements_by_xpath("//input[@type='checkbox']")
        self.selectElements(checkbox)






radioBtn = TestRadioButton()
radioBtn.radioButton()

checkboxbtn = TestRadioButton()
checkboxbtn.testcheckBox()
driver.quit()