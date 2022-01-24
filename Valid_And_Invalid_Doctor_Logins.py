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





#-----------------------------------------------------------------------------
    
class SignUp_Page(LiveServerTestCase):
    def setUp(self):
        self.driver=webdriver.Chrome('/usr/local/bin/chromedriver')
    def test1_doctor_Login(self):
        driver=self.driver
        driver.get('http://127.0.0.1:8000/accounts/loginpage')
        driver.maximize_window()
        time.sleep(2)
        signIn_Button=driver.find_element_by_xpath('/html/body/div/div/div[3]/div/div[2]/button')
        signIn_Button.click()
        driver.maximize_window()
        email_Label=driver.find_element_by_xpath('/html/body/div/div/div[1]/form/input[2]')
        password_Label=driver.find_element_by_xpath('/html/body/div/div/div[1]/form/input[3]')
        doctor_signIn_Button=driver.find_element_by_xpath('/html/body/div/div/div[1]/form/button')
        #----------Valid Doctor Credentials For Login--------------------
        email_Label.send_keys('Doctor1@gmail.com')
        time.sleep(2)
        password_Label.send_keys('User@123')
        time.sleep(2)
        doctor_signIn_Button.click()
        time.sleep(3)
        view_Patient_Button=driver.find_element_by_xpath('/html/body/div[2]/div/div/a')
        if view_Patient_Button.is_displayed():
            time.sleep(2)
            view_Patient_Button.click()
            time.sleep(3)
            if driver.current_url == 'http://127.0.0.1:8000/doctor/patient-list/':
                assert True
            else:
                assert False
    def test2_doctor_Login(self):

        driver=self.driver
        driver.get('http://127.0.0.1:8000/accounts/loginpage')
        driver.maximize_window()
        time.sleep(2)
        signIn_Button=driver.find_element_by_xpath('/html/body/div/div/div[3]/div/div[2]/button')
        signIn_Button.click()
        driver.maximize_window()
        email_Label=driver.find_element_by_xpath('/html/body/div/div/div[1]/form/input[2]')
        password_Label=driver.find_element_by_xpath('/html/body/div/div/div[1]/form/input[3]')
        doctor_signIn_Button=driver.find_element_by_xpath('/html/body/div/div/div[1]/form/button')
        #------------------------------------Invalid Doctor Credentials For Login-------------------
        email_Label.send_keys('Doctor1@gmail.com')
        time.sleep(2)
        password_Label.send_keys('User123')
        time.sleep(2)
        doctor_signIn_Button.click()
        time.sleep(3)
        view_Patient_Button=driver.find_element_by_xpath('/html/body/div[2]/div/div/a')
        if view_Patient_Button.is_displayed():
            time.sleep(2)
            view_Patient_Button.click()
            time.sleep(3)
            if driver.current_url == 'http://127.0.0.1:8000/doctor/patient-list/':
                assert True
            else:
                assert False
              
              
#--------------------------------------------------------Doctor Logout ------------------------------------------
    
    def test_Doctor_Logout(self):
        driver=self.driver
        driver.get('http://127.0.0.1:8000/accounts/loginpage')
        driver.maximize_window()
        time.sleep(2)
        signIn_Button=driver.find_element_by_xpath('/html/body/div/div/div[3]/div/div[2]/button')
        signIn_Button.click()
        driver.maximize_window()
        email_Label=driver.find_element_by_xpath('/html/body/div/div/div[1]/form/input[2]')
        password_Label=driver.find_element_by_xpath('/html/body/div/div/div[1]/form/input[3]')
        signUp_Button=driver.find_element_by_xpath('/html/body/div/div/div[1]/form/button')
        email_Label.send_keys('Doctor1@gmail.com')
        time.sleep(2)
        password_Label.send_keys('User@123')
        time.sleep(2)
        signUp_Button.click()
        time.sleep(3)
        logout_Button=driver.find_element_by_xpath('/html/body/header/div/nav/div/div/ul/li[3]/a/button')
        time.sleep(2)
        if logout_Button.is_displayed():
            logout_Button.click()
            assert True
        else:
            assert False




    def tearDown(self):
        self.driver.close()
        
        
        
        
        
        
        
        
        
        
        
        
















