from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

def init():
    global lyric

    name = input("노래제목을 입력하세요: ")
    url = f"https://www.melon.com/search/total/index.htm?q={name}"
    
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    
    driver = webdriver.Chrome(options = options)
    driver.get(url)
    time.sleep(3)
    
    try:
        driver.find_element(By.CSS_SELECTOR, "#frm_searchSong > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > div > a.btn.btn_icon_detail > span").click()
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, "#lyricArea > button > span").click()
        time.sleep(3)
        lyric = driver.find_element(By.CSS_SELECTOR, "#d_video_summary").text
    except NoSuchElementException:
        lyric = "노래가 없습니다."
        
    driver.quit()