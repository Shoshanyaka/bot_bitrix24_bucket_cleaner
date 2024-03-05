from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from user_profile import USER


def clean_bi_bucket():
    wd = webdriver.Chrome()
    wd.implicitly_wait(30)
    wd.get("https://mygenetics.bitrix24.ru/crm/recyclebin/")

    wd.find_element(By.ID, "login").send_keys(USER.name)
    sleep(1)
    wd.find_element(By.CSS_SELECTOR, ".b24-network-auth-form-btn.ui-btn-success").click()
    wd.find_element(By.ID, "password").send_keys(USER.pwd)
    wd.find_element(By.CSS_SELECTOR, ".b24-network-auth-form-btn.ui-btn-success").click()
    sleep(1)

    i = 0
    while True:
        try:
            wd.find_element(By.ID, "CRM_RECYCLE_BIN_check_all").click()
            sleep(1)
            wd.find_element(By.ID, "group-0-item-1_control").click()
            sleep(1)
            wd.find_element(By.CSS_SELECTOR, ".popup-window-button-accept").click()
            sleep(10)
            i += 1
            print(f'Номер интерации {i}')
        except:
            clean_bi_bucket()

if __name__ == "__main__":
    while True:
        try:
            clean_bi_bucket()
        except:
            exec(clean_bi_bucket())