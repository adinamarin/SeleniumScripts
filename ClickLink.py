import time

from selenium import webdriver

from config.settings import CHROME_PATH

driver = webdriver.Chrome(executable_path=CHROME_PATH)


class TestClickLink():
    def clickLink(self):
        driver.get("http://demo.guru99.com/test/link.html")
        links = driver.find_elements_by_link_text("click here")

        # driver.find_element_by_link_text("click here").click()

        for onelink in links:
            att = onelink.get_attribute('href')
            if att == "http://www.fb.com/":
                onelink.click()
                title = driver.title
                if "Facebook" in title:
                    print("found")
                break


clickOnLink = TestClickLink()
clickOnLink.clickLink()

driver.quit()
