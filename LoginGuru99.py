import time

from selenium import webdriver

from config.settings import USERNAME,PASSWORD,CHROME_PATH


driver = webdriver.Chrome(executable_path = CHROME_PATH)


class TestLoginClass():
        def testLoginOK(self,username,password):
            driver.get("http://www.demo.guru99.com/V4")
            userBox = driver.find_element_by_name("uid")
            #userBox = driver.find_element_by_xpath("//input[@name='uid']")
            #userBox = driver.find_element(By.NAME, "uid")
            userBox.send_keys(username)
            #passBox = driver.find_element_by_name("password")
            passBox = driver.find_element_by_xpath("//input[@name='password']")
            passBox.send_keys(password)
            loginButton = driver.find_element_by_name("btnLogin")
            #loginButton.submit()
            loginButton.click()


            try:
                actualTitle = driver.title
                print(actualTitle)
                if (actualTitle == "Guru99 Bank Manager HomePage"):
                    print("Test Case Login PASS")
                else:
                    ("Test Case Login FAILED")
            except:
                print("Test Case Login FAILED")


            time.sleep(5)

        def testLoginNotOk(self,username,password,testcase):
            driver.get("http://www.demo.guru99.com/V4")
            userBox = driver.find_element_by_name("uid")
            userBox.send_keys(username)

            passBox = driver.find_element_by_xpath("//input[@name='password']")
            passBox.send_keys(password)

            loginButton = driver.find_element_by_name("btnLogin")
            loginButton.click()

            time.sleep(5)
            try:
                actualTitle = driver.title
                print(actualTitle)
                if (actualTitle == "Guru99 Bank Manager HomePage"):
                    print("Test Case Login NOK "+testcase+" FAILED")
                else:
                    print("Test Case Login NOK "+testcase+" PASS")
            except:
                print("Test Case Login NOK "+testcase+" PASS")



test_login = TestLoginClass()
test_login.testLoginOK(USERNAME,PASSWORD)
#user ok, pass nok
#username = "mngr327352"
#password = "passwordNOk"
#test_login.testLoginNotOk(username,password)
test_login.testLoginNotOk(USERNAME,"passwordNOk","user ok ,pass nok")

#user Nok passOk
test_login.testLoginNotOk("usernok",PASSWORD,"user nok,pass ok")

#user nok, pass nok
test_login.testLoginNotOk("usernok","passnok","user nok,pass nok")

# user empty
test_login.testLoginNotOk("",PASSWORD,"user empty,pass ok")

#userok pass empty
test_login.testLoginNotOk(USERNAME,"","user ok,pass empty")

driver.quit()