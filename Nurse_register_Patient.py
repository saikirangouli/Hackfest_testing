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




    def test_RegisterPatient(self):
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
        registerPatient_Button=driver.find_element_by_xpath('/html/body/div[2]/div/div/a[2]')
        registerPatient_Button.click()
        time.sleep(2)
        patientName_Label=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[2]/div[1]/input')
        patientGender_Label=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[2]/div[2]/select/option[3]')
        patientDob_Label=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[2]/div[3]/input')
        patientEmail_Label=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[3]/div[1]/input')
        patientPhone_label=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[3]/div[2]/input')
        patientBloodgroup_Label=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[3]/div[3]/select/option[5]')
        patientRegister_Button=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[3]/input')
        patientName_Label.send_keys('C')
        time.sleep(1)
        patientGender_Label.click()
        time.sleep(1)
        patientDob_Label.click()
        patientDob_Label.send_keys('12011999')
        time.sleep(1)
        #please enter a valid email since you will recieve an registration id to this mail and change this one
        patientEmail_Label.send_keys('dharamtej3@gmail.com.com')
        time.sleep(1)
        patientPhone_label.send_keys('9603896042')#Enter a 10 digit number only
        time.sleep(1)
        patientBloodgroup_Label.click()
        time.sleep(2)
        patientRegister_Button.click()
        time.sleep(3)
        addMedical_Details=driver.find_element_by_css_selector('#home > form > div > div.col-md-12 > div > a')
        if addMedical_Details.is_displayed():

            addMedical_Details.click()
        time.sleep(2)
        if driver.title == 'Add Patient Record':


            height=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[2]/div[1]/input')
            weight=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[2]/div[2]/input')
            pregnancy_Status=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[2]/div[3]/select/option[2]')
            delivery_Date=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[2]/div[4]/input')
            allergies=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[2]/div[5]/textarea')
            bloodPressure=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[2]/div[6]/input')
            pulseRate=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[2]/div[7]/input')
            bodyTemperature=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[2]/div[8]/input')
            isAlcoholic=driver.find_element_by_xpath('//*[@id="home"]/form/div/div[3]/div[1]/select/option[3]')
            isSmoker=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[3]/div[2]/select/option[3]')
            isDiabetic=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[3]/div[3]/select/option[2]')
            insuranceName=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[3]/div[4]/input')
            insuranceNumber=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[3]/div[5]/input')
            previousSurgery=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[3]/div[6]/textarea')
            status=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[3]/div[7]/select/option[3]')
            submit_Button=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[3]/input')
            #please Provide valid nd unique values an existing user cant ablr to register
            height.send_keys('199')
            time.sleep(1)
            weight.send_keys('88')
            time.sleep(1)
            pregnancy_Status.click()
            time.sleep(1)
            delivery_Date.click()
            time.sleep(1)
            delivery_Date.send_keys('12011999')
            time.sleep(1)
            allergies.send_keys('NA')
            time.sleep(1)
            bloodPressure.send_keys('120')#must be numeric
            time.sleep(1)
            pulseRate.send_keys('775')#must be numeric
            time.sleep(1)
            bodyTemperature.send_keys('122')#must be numeric
            time.sleep(1)
            isAlcoholic.click()
            time.sleep(1)
            isSmoker.click()
            time.sleep(1)
            isDiabetic.click()
            time.sleep(1)
            insuranceName.send_keys('NA')
            time.sleep(1)
            insuranceNumber.send_keys('NA')
            time.sleep(1)
            previousSurgery.send_keys('No')
            time.sleep(1)
            status.click()
            time.sleep(2)
            submit_Button.click()
            time.sleep(3)
            logOut_Button=driver.find_element_by_xpath('/html/body/header/div/nav/div/div/ul/li[3]/a/button')
            logOut_Button.click()
            time.sleep(3)
            if driver.current_url == 'http://127.0.0.1:8000/':
                print('Successfully logged out !!!')
                assert True
            else:
                assert False





    
    







    def tearDown(self):
        self.driver.close()



