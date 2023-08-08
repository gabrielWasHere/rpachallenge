from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd



def mainBot():
    #print("Cheguei no webdriver")
    driver = webdriver.Chrome()

    # print("Cheguei no carregar URL")
    driver.get("https://rpachallenge.com/")

    planilha = pd.read_excel('C:\\Users\\User\\PycharmProjects\\RPAchallenge\\challenge (1).xlsx')
    # print(planilha)
    botao_start = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button")
    botao_start.click()
    time.sleep(3)

    # print(planilha.columns)
    for index, linhas in planilha.iterrows():
        first_name = linhas["First Name"]
        last_name = linhas["Last Name "]
        company_name = linhas["Company Name"]
        role_in_company = linhas["Role in Company"]
        address = linhas["Address"]
        email = linhas["Email"]
        phone_number = linhas["Phone Number"]

        campo_firstname = driver.find_element(By.CSS_SELECTOR, "input[ng-reflect-name='labelFirstName']")
        campo_firstname.send_keys(first_name)

        campo_lastname = driver.find_element(By.CSS_SELECTOR, "input[ng-reflect-name='labelLastName']")
        campo_lastname.send_keys(last_name)

        campo_companyname = driver.find_element(By.CSS_SELECTOR, "input[ng-reflect-name='labelCompanyName']")
        campo_companyname.send_keys(company_name)

        campo_role = driver.find_element(By.CSS_SELECTOR, "input[ng-reflect-name='labelRole']")
        campo_role.send_keys(role_in_company)

        campo_address = driver.find_element(By.CSS_SELECTOR, "input[ng-reflect-name='labelAddress']")
        campo_address.send_keys(address)

        campo_email = driver.find_element(By.CSS_SELECTOR, "input[ng-reflect-name='labelEmail']")
        campo_email.send_keys(email)

        campo_phone = driver.find_element(By.CSS_SELECTOR, "input[ng-reflect-name='labelPhone']")
        campo_phone.send_keys(phone_number)

        botao_submit = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input")
        botao_submit.click()
        time.sleep(2)

mainBot()

