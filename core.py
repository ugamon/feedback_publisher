from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('./vendor/chromedriver.exe')

driver.get('-----------------')



job_title = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[5]/div[3]/div[27]/form/div/table/tbody/tr[2]/td/input')
job_feedback = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[5]/div[3]/div[27]/form/div/table/tbody/tr[5]/td/textarea')


job_title.clear()
job_title.send_keys("Тамара")

job_feedback.clear()
job_feedback.send_keys("Вы еще их хлев не видели дома!")

driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20)
                      .until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[1]/div[5]/div[3]/div[27]/form/div/table/tbody/tr[3]/td/div/div/div[1]/div/a[5]"))))
