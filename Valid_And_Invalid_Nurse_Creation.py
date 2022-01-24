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

class Nursecreation(LiveServerTestCase):
    def setUp(self):
        self.driver=webdriver.Chrome('/usr/local/bin/chromedriver')
    def test1_NurseCreation(self):
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
        email_Label.send_keys('user')
        time.sleep(2)
        password_Label.send_keys('1234')
        time.sleep(2)
        signIn_Button.click()
        time.sleep(3)
        getText=driver.page_source
        text='Welcome Back'
        if text in getText:
            createNurse_Button=driver.find_element_by_xpath('/html/body/div[2]/div/div/a[2]')
            if createNurse_Button.is_displayed():
                createNurse_Button.click()
                if driver.current_url == 'http://127.0.0.1:8000/accounts/createnurse/':
                    name=driver.find_element_by_xpath('/html/body/div/div[1]/form/input[2]')
                    email=driver.find_element_by_xpath('/html/body/div/div[1]/form/input[3]')
                    password1=driver.find_element_by_xpath('/html/body/div/div[1]/form/input[4]')
                    password2=driver.find_element_by_xpath('/html/body/div/div[1]/form/input[5]')
                    nurseSignin_Button=driver.find_element_by_xpath('/html/body/div/div[1]/form/button')
#-----------------------------Giving the New Valid Credentials for every execution change name and mail
                    name.send_keys('Nurse5')
                    time.sleep(1)
                    email.send_keys('Nurse5@gmail.com')
                    time.sleep(1)
                    password1.send_keys('User@123')
                    time.sleep(1)
                    password2.send_keys('User@123')
                    time.sleep(2)
                    nurseSignin_Button.click()
                    time.sleep(2)
                    getCurrent_Text=driver.page_source
                    text='Nurse is created'
                    if text in getCurrent_Text:
                        assert True
                    else:
                        assert False

    def test2_NurseCreation(self):

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
        email_Label.send_keys('user')
        time.sleep(2)
        password_Label.send_keys('1234')
        time.sleep(2)
        signIn_Button.click()
        time.sleep(3)
        getText=driver.page_source
        text='Welcome Back'
        if text in getText:
            createNurse_Button=driver.find_element_by_xpath('/html/body/div[2]/div/div/a[2]')
            if createNurse_Button.is_displayed():
                createNurse_Button.click()
                if driver.current_url == 'http://127.0.0.1:8000/accounts/createnurse/':
                    name=driver.find_element_by_xpath('/html/body/div/div[1]/form/input[2]')
                    email=driver.find_element_by_xpath('/html/body/div/div[1]/form/input[3]')
                    password1=driver.find_element_by_xpath('/html/body/div/div[1]/form/input[4]')
                    password2=driver.find_element_by_xpath('/html/body/div/div[1]/form/input[5]')
                    nurseSignin_Button=driver.find_element_by_xpath('/html/body/div/div[1]/form/button')
#-----------------------------Giving the Existing Credentials for every execution change name and mail
                    name.send_keys('Nurse4')
                    time.sleep(1)
                    email.send_keys('Nurse4@gmail.com')
                    time.sleep(1)
                    password1.send_keys('User@123')
                    time.sleep(1)
                    password2.send_keys('User@123')
                    time.sleep(2)
                    nurseSignin_Button.click()
                    time.sleep(2)
                    getCurrent_Text=driver.page_source
                    text='Nurse is created'
                    if text in getCurrent_Text:
                        assert True
                    else:
                        assert False
                    



       
    
    def tearDown(self):
        self.driver.close()
            


        



