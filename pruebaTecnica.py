# Automatización 

import json 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


 

driver= webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com")

time.sleep(5)

#Paso 1 — Login

usuario= driver.find_element(By.NAME,"username")
usuario.send_keys("Admin")
time.sleep(3)
contraseña=driver.find_element(By.NAME,"password")
contraseña.send_keys("admin123")
time.sleep(3)
enviar=driver.find_element(By.XPATH,"//button[@type='submit']")
enviar.click()
time.sleep(2)

# Paso 2 — Crear empleado 
moduloPIM=driver.find_element(By.XPATH,"//a[@class='oxd-main-menu-item active']")
moduloPIM.click()
time.sleep(3)
addEmployed=driver.find_element(By.XPATH,"driver.find_element(By.XPATH,")
addEmployed.click()
time.sleep(2)