from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from ReadTextFile import ReadTextFile

sFileToolAddress = "http://eligibilityfile.extendhealth.com/eligibilityfiletracking/home"
eXpathToTable = '//*[@id="ConfigList"]'
PathToCodes = "C:\\Users\\lawsshe\\Desktop\\Pod3Codes.txt"
ArrayOfFiles = []

words = ReadTextFile.openfile(PathToCodes)
# print(words)

driver = webdriver.Chrome()
driver.get(sFileToolAddress)
# ------------------------------------
# Check if Eligibility is in the title
# ------------------------------------
assert "Eligibility" in driver.title

eFileTable = driver.find_element(By.XPATH, eXpathToTable)
rows = eFileTable.find_elements(By.TAG_NAME, "tr")
for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    if len(cols) >= 3:
        # Check for files that have not been assigned.
        if cols[5].text == "":
            # print(cols[1].text)
            ArrayOfFiles.append(cols[1].text)
# print(ArrayOfFiles)
for eachword in words:
    # print(eachword)
    for i in range(len(ArrayOfFiles)):
        #print(str(ArrayOfFiles[i]))
        if str(ArrayOfFiles[i]).find(eachword) != -1:
            print(ArrayOfFiles[i])
driver.close()

















