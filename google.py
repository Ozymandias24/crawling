from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import time
import os

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)


arr = ["https://view.chunjae.co.kr/streamdocs/view/sd;streamdocsId=_VYOCsaUL5QFiqr6JM4t9JD7DAic-G8p6A2yBHEcMB0;isExternal=eQ;printUse=;enableDapSide=;pageView="]
input("준비되었으면 엔터를 눌러주세요.")

for url in arr:
    
    driver.get(url)
    wait = WebDriverWait(driver, 15)
    wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "canvas")))
    pages = driver.find_elements(By.TAG_NAME, "canvas")
    

    cnt = 1
    # 저장 경로 설정
    save_dir = "C:\\Users\\user\\Documents\\Coding\\BukBuk\\ComputerScience\\Microbit\\Images\\Mathmetics"
    os.makedirs(save_dir, exist_ok=True)
    # 이전 URL 추적 변수 제거 (모든 이미지를 저장하려는 경우)
    # preurl = str()
    for i, canvas in enumerate(pages, 1):
        file_path = os.path.join(save_dir, f"{i}.png")
        canvas.screenshot(file_path)
        print(f"Saved page {i}: {file_path}")

    driver.quit()

    