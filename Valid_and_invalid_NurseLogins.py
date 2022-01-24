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

class NurseLogin(LiveServerTestCase):
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
#----------------------------------Valid Credentials-------------------------------------------
        email_Label.send_keys('Nurse3@gmail.com')
        time.sleep(2)
        password_Label.send_keys('User@123')
        time.sleep(2)
        signIn_Button.click()
        time.sleep(2)
        getText=driver.page_source
        text='Welcome Back'
        if text in getText:
            assert True
        else:
            assert False
        

    def test2_NurseLogin(self):

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
#------------------------Invalid Credentials----------------------------------------
        email_Label.send_keys('Nurse3@gmail.com')
        time.sleep(2)
        password_Label.send_keys('User123')#invalid Password
        time.sleep(2)
        signIn_Button.click()
        time.sleep(2)
        getText=driver.page_source
        text='Invalid credentials'
        if text in getText and driver.current_url == 'http://127.0.0.1:8000/accounts/loginpage':
            assert False
        else:
            assert True
       
                    



       
    
    def tearDown(self):
        self.driver.close()
            


        



