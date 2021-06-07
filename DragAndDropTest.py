import time

from selenium import webdriver

from config.settings import CHROME_PATH

from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(executable_path=CHROME_PATH)

class DragandDrop():

    def testingDragandDrop(self):
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()
        iFrame = driver.find_element_by_xpath("//iframe[@class='demo-frame']")
        driver.switch_to.frame(iFrame)
        fromElement = driver.find_element_by_id("draggable")
        toElement = driver.find_element_by_id("droppable")

        #print("here")
        action = ActionChains(driver)
        action.drag_and_drop(fromElement,toElement)
        time.sleep(10)
        action.perform()
        time.sleep(10)

dragAndDrop = DragandDrop()
dragAndDrop.testingDragandDrop()
driver.quit()