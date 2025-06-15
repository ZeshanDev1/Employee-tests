#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

try:
    base_url = "http://13.218.131.137:3000"
    driver.get(base_url)
    time.sleep(2)
    print("✅ Test 1 Passed: Homepage loaded")

    driver.find_element(By.LINK_TEXT, "Create Record").click()
    time.sleep(2)
    print("✅ Test 2 Passed: Navigated to Create Record page")

    driver.find_element(By.ID, "name").send_keys("Zeshan Khan")
    driver.find_element(By.ID, "position").send_keys("QA Engineer")
    driver.find_element(By.ID, "positionSenior").click()
    time.sleep(1)
    print("✅ Test 3 Passed: Form fields filled")

    driver.find_element(By.XPATH, "//input[@type='submit' and @value='Create person']").click()
    time.sleep(3)
    print("✅ Test 4 Passed: Form submitted")

    rows = driver.find_elements(By.XPATH, "//table/tbody/tr")
    found = False
    for row in rows:
        if "Zeshan Khan" in row.text and "QA Engineer" in row.text and "Senior" in row.text:
            found = True
            edit_button = row.find_element(By.LINK_TEXT, "Edit")
            delete_button = row.find_element(By.XPATH, ".//button[text()='Delete']")
            break

    assert found, "❌ Record not found after creation"
    print("✅ Test 5 Passed: Record found on homepage")

    edit_button.click()
    time.sleep(2)
    name_field = driver.find_element(By.ID, "name")
    name_field.clear()
    name_field.send_keys("Zeshan Ali")
    driver.find_element(By.XPATH, "//input[@type='submit' and @value='Update Record']").click()
    time.sleep(3)
    print("✅ Test 6 Passed: Record edited")

    rows = driver.find_elements(By.XPATH, "//table/tbody/tr")
    edited = any("Zeshan Ali" in row.text for row in rows)
    assert edited, "❌ Edited record not visible"
    print("✅ Test 7 Passed: Edited record confirmed")

    for row in rows:
        if "Zeshan Ali" in row.text:
            delete_button = row.find_element(By.XPATH, ".//button[text()='Delete']")
            delete_button.click()
            break
    time.sleep(2)
    print("✅ Test 8 Passed: Delete button clicked")

    driver.refresh()
    time.sleep(2)
    rows = driver.find_elements(By.XPATH, "//table/tbody/tr")
    deleted = all("Zeshan Ali" not in row.text for row in rows)
    assert deleted, "❌ Record still exists after deletion"
    print("✅ Test 9 Passed: Record deleted successfully")

except Exception as e:
    print("❌ Test Failed:", e)

finally:
    driver.quit()

