from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8989")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=opt)



def channel(yt, komen, jumlah, waktu):
    driver.get(yt)
    for x in range(1, jumlah):
       rpl = "/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[%s]/ytd-comment-renderer/div[3]/div[2]/ytd-comment-action-buttons-renderer/div[1]/div[4]"%(x)
       bls = "/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[%s]/ytd-comment-renderer/div[3]/div[2]/ytd-comment-action-buttons-renderer/div[2]/ytd-comment-reply-dialog-renderer/ytd-commentbox/div[2]/div/div[2]/tp-yt-paper-input-container/div[2]/div/div[1]/ytd-emoji-input/yt-user-mention-autosuggest-input/yt-formatted-string/div"%(x)
       btn = "/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/ytd-comments/ytd-item-section-renderer/div[3]/ytd-comment-thread-renderer[%s]/ytd-comment-renderer/div[3]/div[2]/ytd-comment-action-buttons-renderer/div[2]/ytd-comment-reply-dialog-renderer/ytd-commentbox/div[2]/div/div[4]/div[5]/ytd-button-renderer[2]/a/tp-yt-paper-button/yt-formatted-string"%(x)
       WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, rpl))).click()  
       WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, bls))).send_keys(komen)
       WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, btn))).click()
       time.sleep(waktu)  
    

ch = input("masukan link video dan komen: ")
kom = input("masukan komen: ")
jmlh = int(input("masukan jumlah: "))
wkt = int(input("masukan delay untuk komen: "))
channel(ch, kom, jmlh, wkt)
