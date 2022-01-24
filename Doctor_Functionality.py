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


class DoctorPage(LiveServerTestCase):
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
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                #time.sleep(2)
                prescription_Button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div/ul/li[3]/a")))
                prescription_Button.click()
                time.sleep(3)

                addPrescription_Button=driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/h1/a')
                addPrescription_Button.click()
                time.sleep(2)
                source=driver.page_source
                text='Diagnose'
                if text in source:

                    Diagons_Name=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[2]/div[1]/input')
                    body_Site=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[2]/div[2]/input')
                    dateOf_Onset=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[2]/div[3]/input')
                    severity=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[2]/div[4]/select/option[2]')
                    dateOf_Abatement=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[2]/div[5]/input')
                    certainity=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[2]/div[6]/select/option[3]')
                    diagnose_Description=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[2]/div[7]/textarea')
                    device_Name=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[3]/div[1]/input')
                    deviceBody_Site=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[3]/div[2]/input')
                    deviceUse=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[3]/div[3]/input')
                    device_Description=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[3]/div[4]/textarea')
                    addDiagnosis_Button=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[3]/div[5]/input')
                    back_Button=driver.find_element_by_xpath('/html/body/div/div/div[1]/input')
                    #-------------------------Passing Values------------------
                    Diagons_Name.send_keys('Diagnose2')
                    time.sleep(1)
                    body_Site.send_keys('Head')
                    time.sleep(1)
                    dateOf_Onset.click()
                    dateOf_Onset.send_keys('12011998')
                    time.sleep(1)
                    severity.click()
                    time.sleep(1)
                    dateOf_Abatement.click()
                    dateOf_Abatement.send_keys('22112004')
                    time.sleep(1)
                    certainity.click()
                    time.sleep(1)
                    diagnose_Description.send_keys('This is description about diagnosis')
                    time.sleep(1)
                    device_Name.send_keys('Device 22')
                    time.sleep(1)
                    deviceBody_Site.send_keys('Head')
                    time.sleep(1)
                    deviceUse.send_keys('Usage of Device')
                    time.sleep(1)
                    device_Description.send_keys('Its an Description about device')
                    time.sleep(1)
                    addDiagnosis_Button.click()
                    time.sleep(3)
                    getDiagnosis_Details=driver.page_source
                    Text_is='Diagnosis Details'
                    if Text_is in getDiagnosis_Details:

                        addMedicine_Button=driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/h1/a[2]')
                        addMedicine_Button.click()
                        time.sleep(2)

                        if 'Add Medicine' in driver.page_source:



                            doseUnit=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[2]/div[1]/input')
                            duration=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[2]/div[2]/input')
                            numberOf_Times=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[2]/div[3]/input')
                            medicine_Name=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[2]/div[4]/select/option[2]')
                            instruction_ofMedcine=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[3]/div[1]/textarea')
                            reason_forMedicine=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[3]/div[2]/textarea')
                            add_Button=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[3]/input')
                            #pass Values--------------------------
                            doseUnit.send_keys('1')
                            time.sleep(1)
                            duration.send_keys('1')
                            time.sleep(1)
                            numberOf_Times.send_keys('3')
                            time.sleep(1)
                            medicine_Name.click()
                            time.sleep(1)
                            instruction_ofMedcine.send_keys('This is an instruction')
                            time.sleep(1)
                            reason_forMedicine.send_keys('its an reason')
                            time.sleep(1)
                            add_Button.click()
                            time.sleep(3)
                            if 'Medicine Added Successfullty' in driver.page_source:

                                back_Button=driver.find_element_by_xpath('/html/body/div/div/div[1]/input')
                                back_Button.click()
                                time.sleep(2)
                                addTest_Button=driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/h1/a[1]')
                                addTest_Button.click()
                                time.sleep(2)
                                if 'Add Laboratory Tests' in driver.page_source:
                                    testName_Label=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[2]/div[1]/input')
                                    testSpecimen_Label=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[2]/div[2]/input')
                                    testBodysite_Label=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[2]/div[3]/input')
                                    testUse_Label=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[3]/div[1]/input')
                                    testDescription_Label=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[3]/div[2]/input')
                                    addT_Button=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div[3]/input')
                                    testName_Label.send_keys('Name')
                                    time.sleep(1)
                                    testSpecimen_Label.send_keys('Specimen')
                                    time.sleep(1)
                                    testBodysite_Label.send_keys('Body')
                                    time.sleep(1)
                                    testUse_Label.send_keys('Test Use')
                                    time.sleep(1)
                                    testDescription_Label.send_keys('test Desc')
                                    time.sleep(2)
                                    addT_Button.click()
                                    time.sleep(3)


                            
                        
                    

            
                    
                
                    
                


            
