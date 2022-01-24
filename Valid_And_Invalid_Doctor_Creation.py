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
    def test3_Signup_Button(self):
        driver=self.driver
        driver.get('http://127.0.0.1:8000/accounts/loginpage')
        driver.maximize_window()
        time.sleep(2)
       
        signUp_Button=driver.find_element_by_xpath('/html/body/div/div/div[3]/div/div[2]/button')
        if signUp_Button.is_displayed():
            signUp_Button.click()
        time.sleep(2)
        email_Label=driver.find_element_by_xpath('/html/body/div/div/div[1]/form/input[2]')
        password_Label=driver.find_element_by_xpath('/html/body/div/div/div[1]/form/input[3]')
        signIn_Button=driver.find_element_by_xpath('/html/body/div/div/div[1]/form/button')
        #-------------------------Admin valid credentials------------
        email_Label.send_keys('user')
        time.sleep(1)
        password_Label.send_keys('1234')
        time.sleep(2)
        signIn_Button.click()
        driver.maximize_window()

        time.sleep(3)
        createDoctor_Button=driver.find_element_by_css_selector('#button1')

        createDoctor_Button.click()
        driver.maximize_window()
        time.sleep(2)
        doctor_Name=driver.find_element_by_xpath('/html/body/div/div[1]/form/input[2]')
        doctor_email=driver.find_element_by_xpath('/html/body/div/div[1]/form/input[3]')
        doctor_password1=driver.find_element_by_xpath('/html/body/div/div[1]/form/input[4]')
        doctor_password2=driver.find_element_by_xpath('/html/body/div/div[1]/form/input[5]')
        doctor_regsiter=driver.find_element_by_css_selector('#container > div.form-container.sign-in-container > form > button')
#-------------------------------every time of execution change Here to new name and email---------------------------------------------

        doctor_Name.send_keys('Doctor11')
        time.sleep(1)
        doctor_email.send_keys('Doctor11@gmail.com')
        time.sleep(1)
        doctor_password1.send_keys('User@123')
        time.sleep(1)
        doctor_password2.send_keys('User@123')
        time.sleep(2)
        doctor_regsiter.click()
        time.sleep(2)
        currentPage_Source=driver.page_source
        text='Doctor is created'
        if text in currentPage_Source:
            #print('Doctor is Created')#success message
            assert True
        
        else:
            assert False
    def test4_Signup_Button(self):
        driver=self.driver
        driver.get('http://127.0.0.1:8000/accounts/loginpage')
        driver.maximize_window()
        time.sleep(2)
       
        signUp_Button=driver.find_element_by_xpath('/html/body/div/div/div[3]/div/div[2]/button')
        if signUp_Button.is_displayed():
            signUp_Button.click()
        time.sleep(2)
        email_Label=driver.find_element_by_xpath('/html/body/div/div/div[1]/form/input[2]')
        password_Label=driver.find_element_by_xpath('/html/body/div/div/div[1]/form/input[3]')
        signIn_Button=driver.find_element_by_xpath('/html/body/div/div/div[1]/form/button')
        #---------------------------Admin valid credentials------------
        email_Label.send_keys('user')
        time.sleep(1)
        password_Label.send_keys('1234')
        time.sleep(2)
        signIn_Button.click()
        driver.maximize_window()

        time.sleep(3)
        createDoctor_Button=driver.find_element_by_css_selector('#button1')

        createDoctor_Button.click()
        driver.maximize_window()
        time.sleep(2)
        doctor_Name=driver.find_element_by_xpath('/html/body/div/div[1]/form/input[2]')
        doctor_email=driver.find_element_by_xpath('/html/body/div/div[1]/form/input[3]')
        doctor_password1=driver.find_element_by_xpath('/html/body/div/div[1]/form/input[4]')
        doctor_password2=driver.find_element_by_xpath('/html/body/div/div[1]/form/input[5]')
        doctor_regsiter=driver.find_element_by_css_selector('#container > div.form-container.sign-in-container > form > button')

#---------------------------------Existing Credentials of Doctor Throws an Error------------------------------------------------
        doctor_Name.send_keys('Doctor10')
        time.sleep(1)
        doctor_email.send_keys('Doctor10@gmail.com')
        time.sleep(1)
        doctor_password1.send_keys('User@123')
        time.sleep(1)
        doctor_password2.send_keys('User@123')
        time.sleep(2)
        doctor_regsiter.click()
        time.sleep(2)
        currentPage_Source=driver.page_source
        text='Doctor is created'
        if text in currentPage_Source:
            #print('Doctor is Created')#success message
            assert True
        
        else:
            assert False
   
    def tearDown(self):
        self.driver.close()

       
 
       
   

        
            
        


       
