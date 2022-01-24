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


class HomePage(StaticLiveServerTestCase):
   
    def setUp(self):
       self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')

    #-----------------------------------------------about us Button Functionality--------------------------------------
    def test1_aboutUs_Button(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/')
        driver.maximize_window()
        time.sleep(1)
        aboutUs_Button=driver.find_element_by_xpath('/html/body/header/div/nav/div/div/ul/li[2]/a')
        if aboutUs_Button.is_displayed():
            time.sleep(2)
            aboutUs_Button.click()
        time.sleep(2)
        if driver.current_url == 'http://127.0.0.1:8000/aboutUs':
            time.sleep(2)
            assert True
        else:
            time.sleep(2)
            assert False
        
#---------------------------------------------------Login Button Functionality---------------------------------------------
    
    def test2_Login_Button(self):
        driver=self.driver
        driver.get('http://127.0.0.1:8000/')
        driver.maximize_window()
        time.sleep(2)
        login_Button=driver.find_element_by_xpath('/html/body/header/div/nav/div/div/ul/li[3]/a/button')
        if login_Button.is_displayed():
            time.sleep(2)
            login_Button.click()
        if driver.current_url == 'http://127.0.0.1:8000/accounts/loginpage':
            time.sleep(2)
            assert True
        else:
            time.sleep(2)
            assert False
    


        
    def tearDown(self):
        self.driver.close()
    
    
    
    
    
    
    
    
    
        self.driver.close()

 
