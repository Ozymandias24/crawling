from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

arr = ["https://view.chunjae.co.kr/streamdocs/view/sd;streamdocsId=_VYOCsaUL5QFiqr6JM4t9JD7DAic-G8p6A2yBHEcMB0;isExternal=eQ;printUse=;enableDapSide=;pageView="]
driver.get(arr[0])

input("Press Enter after the document is fully loaded and visible...")

save_dir = "C:\\Users\\user\\Documents\\Coding\\BukBuk\\ComputerScience\\Microbit\\Images\\Mathmetics"
os.makedirs(save_dir, exist_ok=True)

wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "svg")))

captured_ids = set()
scroll_pause = 1.0
max_scrolls = 200
scroll_height = 1000
page_index = 1


svgs = driver.find_elements(By.TAG_NAME, "svg")

for svg in svgs:
    svg_id = svg.get_attribute("id") or f"index_{page_index}"
    if svg_id not in captured_ids:
        time.sleep(1.0)
        file_path = os.path.join(save_dir, f"{page_index:03d}.png")
        try:
            svg.screenshot(file_path)
            print(f"Captured page {page_index}: {file_path}")
            captured_ids.add(svg_id)
            page_index += 1
        except Exception as e:
            print(f"Failed to capture page {page_index}: {e}")

driver.execute_script(f"window.scrollBy(0, {scroll_height});")
time.sleep(scroll_pause)

new_svgs = driver.find_elements(By.TAG_NAME, "svg")
if len(new_svgs) == len(svgs):
    print("No new pages detected. Stopping scroll.")

        

print("All visible pages captured.")
driver.quit()
