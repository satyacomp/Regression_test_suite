from selenium.webdriver.common.by import By
from time import sleep
import pytest
from constant import EXAM_INFO, CHAT_INFO
from conftest import *


class Test_Exam_Module(Dashboard_Test):
    def test_add_exam_info(self):
        try:
            exam_info = EXAM_INFO["INFO"]
            wait = pytest.wait
            # Code for identification and feature testing
            wait.until(
                EC.element_to_be_clickable((By.ID, "menu-group__analytics"))
            ).click()
            wait.until(
                EC.element_to_be_clickable((By.ID, "menu-item__analytics__exam"))
            ).click()
            wait.until(EC.element_to_be_clickable((By.NAME, "csv_text"))).send_keys(
                exam_info
            )
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[normalize-space()='Save']")
                )
            ).click()
            sleep(2)
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[normalize-space()='Close']")
                )
            ).click()
            return True
        except Exception as e:
            return False

    def test_add_chat_info(self):
        try:
            chat_info = CHAT_INFO["INFO"]
            wait = pytest.wait
            # Code for identification and feature testing
            sleep(3)
            wait.until(EC.element_to_be_clickable((By.NAME, "chat_room"))).send_keys(
                chat_info
            )
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[normalize-space()='Save']")
                )
            ).click()
            sleep(2)
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[normalize-space()='Close']")
                )
            ).click()
            return True
        except Exception as e:
            return False

    def test_enable_exam_mode(self):
        try:
            wait = pytest.wait
            driver = pytest.driver
            # Code for identification and feature testing
            wait.until(
                EC.element_to_be_clickable((By.ID, "menu-group__settings"))
            ).click()

            wait.until(
                EC.element_to_be_clickable((By.ID, "menu-item__settings__homepage"))
            ).click()

            wait.until(
                EC.element_to_be_clickable((By.NAME, "course:google:client_secret"))
            ).click()
            chkboxes = driver.find_elements("xpath", "//input[@type='checkbox']")
            chkboxes[3].click()  # select enable exam mode checkbox

            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[normalize-space()='Save']")
                )
            ).click()
            return True
        except Exception as e:
            return False

    def test_exam_QR_code(self):
        try:
            wait = pytest.wait
            # Code for identification and feature testing
            wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//div[@id='menu-group__analytics']//a[@class='mdl-navigation__link gcb-collapse__button']",
                    )
                )
            ).click()
            wait.until(
                EC.element_to_be_clickable((By.ID, "menu-item__analytics__Exam"))
            ).click()
            wait.until(
                EC.element_to_be_clickable(
                    (By.ID, "//input[@value='Genereate new UUID']")
                )
            ).click()
            return True
        except Exception as e:
            return False
