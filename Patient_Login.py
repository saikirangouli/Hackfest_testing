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

class Patient(LiveServerTestCase):
    def setUp(self):
        self.driver=webdriver.Chrome('/usr/local/bin/chromedriver')
    def test1_PatientLogin(self):
        driver=self.driver
        driver.get('http://127.0.0.1:8000/')
        driver.maximize_window()
        time.sleep(2)
        viewPrescription_Button=driver.find_element_by_xpath('/html/body/div[1]/div/div/a')
        if viewPrescription_Button.is_displayed():
            viewPrescription_Button.click()
            time.sleep(2)
            if driver.current_url == 'http://127.0.0.1:8000/registrationNo':
                registration_Number=driver.find_element_by_xpath('/html/body/div/div[1]/form/input[2]')
                registration_Number.send_keys('Saikirandf0b58bcd290841')#recieved to the mail
                getReport_Button=driver.find_element_by_xpath('/html/body/div/div[1]/form/button')
                getReport_Button.click()
                time.sleep(2)
                if 'Basic Details' in driver.page_source:
                    medicalHistory_Button=driver.find_element_by_xpath('/html/body/div/div[1]/div/ul/li[2]/a')
                    medicalHistory_Button.click()
                    time.sleep(2)
                    prescription_Button=driver.find_element_by_xpath('/html/body/div/div[1]/div/ul/li[3]/a')
                    prescription_Button.click()
                    time.sleep(2)
                    downloadPrescription_Button=driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/table/tbody/tr[1]/td[3]/a[2]')
                    downloadPrescription_Button.click()
                    time.sleep(2)
                    
       










    def tearDown(self):
        self.driver.close()



