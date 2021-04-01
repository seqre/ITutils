from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CVS_LINK = 'https://www.cvs.com/immunizations/covid-19-vaccine'
INDIANA_STATE_XPATH = '/html/body/content/div/div/div/div[3]/div/div/div[2]/div/div[5]/div/div/div/div/div/div[1]/div[2]/div/div[2]/div/div/div/div/div[1]/ul/li[14]/div/a'
FORT_WAYNE_XPATH = '/html/body/div[2]/div/div[4]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div[6]/div/div/table/tbody/tr[4]'

driver = webdriver.Firefox()
driver.get(CVS_LINK)

indiana_state = driver.find_element_by_xpath(INDIANA_STATE_XPATH)
indiana_state.click()

try:
    fort_wayne = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, FORT_WAYNE_XPATH)))
    print(fort_wayne.text)
finally:
    driver.quit()
