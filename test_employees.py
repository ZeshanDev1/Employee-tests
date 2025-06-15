#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

# Configure headless Chrome
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Use the chromedriver already bundled in the selenium/standalone-chrome image
try:
    driver = webdriver.Chrome(options=options)
except Exception as e:
    print("❌ Could not start Chrome WebDriver:", e)
    sys.exit(1)

base_url = "http://13.218.131.137:3000"

try:
    # Test 1: Homepage loads
    driver.get(base_url)
    time.sleep(2)
    assert "Record List" in driver.title or "React App" in driver.title
    print("✅ Test 1 Passed: Homepage loaded — title is", driver.title)

    # Test 2: Navigate to Create page
    driver.find_element(By.LINK_TEXT, "Create Record").click()
    time.sleep(1)
    assert "Create New Record" in driver.page_source
    print("✅ Test 2 Passed: Navigated to Create Record page")

    # Test 3: Fill out and submit form
    driver.find_element(By.ID, "name").send_keys("Zeeshan QA")
    driver.find_element(By.ID, "position").send_keys("QA Engineer")
    driver.find_element(By.ID, "positionSenior").click()
    driver.find_element(By.XPATH, "//input[@type='submit' and @value='Create person']").click()
    time.sleep(2)
    print("✅ Test 3 Passed: Form submitted")

    # Test 4: New record appears
    rows = driver.find_elements(By.XPATH, "//table/tbody/tr")
    assert any("Zeeshan QA" in r.text for r in rows)
    print("✅ Test 4 Passed: New record visible in list")

    # Grab edit/delete buttons for our created row
    row = next(r for r in rows if "Zeeshan QA" in r.text)
    edit_btn = row.find_element(By.LINK_TEXT, "Edit")
    delete_btn = row.find_element(By.XPATH, ".//button[text()='Delete']")

    # Test 5: Edit record
    edit_btn.click()
    time.sleep(1)
    name_input = driver.find_element(By.ID, "name")
    name_input.clear()
    name_input.send_keys("Zeeshan QA Updated")
    driver.find_element(By.XPATH, "//input[@type='submit' and @value='Update Record']").click()
    time.sleep(2)
    print("✅ Test 5 Passed: Record edited")

    # Test 6: Edited record appears
    rows = driver.find_elements(By.XPATH, "//table/tbody/tr")
    assert any("Zeeshan QA Updated" in r.text for r in rows)
    print("✅ Test 6 Passed: Edited record visible")

    # Test 7: Delete record
    row = next(r for r in rows if "Zeeshan QA Updated" in r.text)
    row.find_element(By.XPATH, ".//button[text()='Delete']").click()
    time.sleep(2)
    print("✅ Test 7 Passed: Delete button clicked")

    # Test 8: Record no longer in list
    rows = driver.find_elements(By.XPATH, "//table/tbody/tr")
    assert all("Zeeshan QA Updated" not in r.text for r in rows)
    print("✅ Test 8 Passed: Record deleted from list")

    # Test 9: Table structure still present
    assert driver.find_element(By.TAG_NAME, "table")
    print("✅ Test 9 Passed: Table still present")

    # Test 10: Navbar present
    assert driver.find_element(By.TAG_NAME, "nav")
    print("✅ Test 10 Passed: Navbar found")

    sys.exit(0)

except AssertionError as ae:
    print("❌ Assertion Failed:", ae)
    sys.exit(2)
except Exception as ex:
    print("❌ Test Error:", ex)
    sys.exit(3)
finally:
    driver.quit()
