from atexit import register
from lib2to3.pgen2 import driver
from webbrowser import get
from xml.dom.minidom import Document
from django.test import TestCase
import pytest
from django.test import LiveServerTestCase
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import time
import unittest
import HtmlTestRunner

class NursePage(LiveServerTestCase):
    def setUp(self):
        self.driver=webdriver.Chrome('/usr/local/bin/chromedriver')
    def test1_NurseLogin(self):
        driver=self.driver
        driver.get('http://127.0.0.1:8000/')
        driver.maximize_window()
        time.sleep(2)
        loginButton=driver.find_element_by_xpath('/html/body/header/div/nav/div/div/ul/li[3]/a/button')
        loginButton.click()
        time.sleep(2)
        signUp_Button=driver.find_element_by_xpath('/html/body/div/div/div[3]/div/div[2]/button')
        signUp_Button.click()
        time.sleep(3)
        email_Label=driver.find_element_by_xpath('/html/body/div/div/div[1]/form/input[2]')
        password_Label=driver.find_element_by_xpath('/html/body/div/div/div[1]/form/input[3]')
        signIn_Button=driver.find_element_by_xpath('/html/body/div/div/div[1]/form/button')
        email_Label.send_keys('Nurse3@gmail.com')
        time.sleep(2)
        password_Label.send_keys('User@123')
        time.sleep(2)
        signIn_Button.click()
        time.sleep(2)
        view_Patient_Button=driver.find_element_by_xpath('/html/body/div[2]/div/div/a')
        if view_Patient_Button.is_displayed():
            time.sleep(2)
            view_Patient_Button.click()
            time.sleep(2)
            view_Records=driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[5]/a')
            view_Records.click()
            time.sleep(2)
            current_Page_Source=driver.page_source
            text='Basic Details'
            if text in current_Page_Source:

                medical_History_Button=driver.find_element_by_xpath('/html/body/div/div[1]/div/ul/li[2]/a')
                medical_History_Button.click()
                time.sleep(3)
                #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                #time.sleep(2)
                updatePatientDetails_Button=driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/h1/a')
                updatePatientDetails_Button.click()
                time.sleep(2)
                
                if 'Update Patient Details' in driver.page_source:
                    updateHeight_Label=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[2]/div[1]/input')
                    updateWeight_Label=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[2]/div[2]/input')
                    updatePregnancy_Status=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[2]/div[3]/select/option[2]')
                    expectedDelivery_Date=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[2]/div[4]/input')
                    updateAllergies_Label=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[2]/div[5]/textarea')
                    update_Button=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[3]/input')
                    updateHeight_Label.clear()  
                    updateHeight_Label.send_keys('182')
                    time.sleep(1)
                    updateWeight_Label.clear()
                    updateWeight_Label.send_keys('99')
                    time.sleep(1)
                    updatePregnancy_Status.click()
                    time.sleep(1)
                    expectedDelivery_Date.click()
                    expectedDelivery_Date.send_keys('14021998')
                    time.sleep(1)

                    updateAllergies_Label.clear()
                    updateAllergies_Label.send_keys('Dust Allergy')
                    time.sleep(1)
                    update_Button.click()
                    time.sleep(3)
                    if 'Records Successfully Updated' in driver.page_source:
                        print('Records are successfully Updated')
                        backToHome_Button=driver.find_element_by_xpath('/html/body/div/div/div[1]/input')
                        backToHome_Button.click()
                        time.sleep(3)
                        logOut_Button=driver.find_element_by_xpath('/html/body/header/div/nav/div/div/ul/li[3]/a/button')
                        if logOut_Button.is_displayed():
                            logOut_Button.click()
                            time.sleep(3)
                            if driver.current_url == 'http://127.0.0.1:8000/':
                                print('Successfully logged out !!')
                                assert True
                            else:
                                assert False










    def tearDown(self):
        self.driver.close()



