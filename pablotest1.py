from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import sys
import csv

resultsprojecttitle = []
resultscountry = []
resultsprojectid = []
resultsamount = []
resultsstatus = []
resultsdate = []
url = 'https://projects.worldbank.org/en/projects-operations/projects-list?&status_exact=Active'
chrome_driver_path = '/Users/Miguel/Documents/Estudios/Python/explorePablo/chromedriver'
chrome_options = Options()
chrome_options.add_argument('--headless')
webdriver = webdriver.Chrome(
    executable_path=chrome_driver_path, options=chrome_options
)
with webdriver as driver:
    # Set timeout time
    wait = WebDriverWait(driver, 10)
    # retrive url in headless browser
    driver.get(url)
    for x in range(10, 13):
        wait.until(presence_of_element_located(
            (By.CSS_SELECTOR, "table.project-operation-tab-table")))

        time.sleep(3)
        results = driver.find_elements_by_css_selector(
            "table.project-operation-tab-table tr td:nth-child(1)")
        resultsprojecttitlebypage = driver.find_elements_by_css_selector(
            "table.project-operation-tab-table tr td:nth-child(1)")
        resultscountrybypage = driver.find_elements_by_css_selector(
            "table.project-operation-tab-table tr td:nth-child(2)")
        resultsprojectidbypage = driver.find_elements_by_css_selector(
            "table.project-operation-tab-table tr td:nth-child(3)")
        resultsamountbypage = driver.find_elements_by_css_selector(
            "table.project-operation-tab-table tr td:nth-child(4)")
        resultsstatusbypage = driver.find_elements_by_css_selector(
            "table.project-operation-tab-table tr td:nth-child(5)")
        resultsdatebypage = driver.find_elements_by_css_selector(
            "table.project-operation-tab-table tr td:nth-child(6)")

        i = 0
        for quote in results:
            quoteArr = quote.text.split('\n')
            print(quoteArr)
            print()
            resultsprojecttitle.append(resultsprojecttitlebypage[i].text)
            resultscountry.append(resultscountrybypage[i].text)
            resultsprojectid.append(resultsprojectidbypage[i].text)
            resultsamount.append(resultsamountbypage[i].text)
            resultsstatus.append(resultsstatusbypage[i].text)
            resultsdate.append(resultsdatebypage[i].text)
            i += 1

        # must close the driver after task finished
        selector = 'ul.pagination li:nth-child(' + str(x) + ') a'
        print(selector)
        link = driver.find_element_by_css_selector(selector)
        link.click()
    driver.close()

with open('listing.csv', 'w', newline='') as file:
    fieldnames = ['project_title', 'region', 'project_number',
                  'commitment_amount', 'status', 'ApprovalDate']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    j = 0

    for project in resultsprojecttitle:
        writer.writerow({'project_title': resultsprojecttitle[j],
                         'region': resultscountry[j], 'project_number': resultsprojectid[j], 'commitment_amount': resultsamount[j], 'status': resultsstatus[j], 'ApprovalDate': resultsdate[j]})
        j += 1
#         writer.writerow({'region': 'Magnus Carlsen', 'fide_rating': 2870})
