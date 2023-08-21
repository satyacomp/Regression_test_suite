from selenium.webdriver.common.by import By
import pytest
from constant import STUDENT_INFO, SYNC_SCORES
from conftest import *
from time import sleep
import os


class Test_User_Module(Dashboard_Test):
    def test_student_profiles_info(self):
        try:
            search_mail = STUDENT_INFO["SEARCHING_MAIL"]
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
                EC.element_to_be_clickable(
                    (By.ID, "menu-item__analytics__student_list_admin")
                )
            ).click()
            wait.until(EC.element_to_be_clickable((By.ID, "search-email"))).send_keys(
                search_mail
            )
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='Search']")
                )
            ).click()
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='Clear']")
                )
            ).click()
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[normalize-space()='student5940@mail.com']")
                )
            ).click()
            return True
        except Exception as e:
            return False

    def test_enroll_students(self):
        try:
            enroll_mails = STUDENT_INFO["STUDENT_MAILS"]
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
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[@id='menu-item__analytics__enrollment']")
                )
            ).click()
            wait.until(EC.element_to_be_clickable((By.NAME, "csv_text"))).send_keys(
                enroll_mails
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

    def test_bulk_enrollment(self):
        students_json_file = os.getcwd() + "/src/bulk_enroll.csv"
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
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[@id='menu-item__analytics__student_list']")
                )
            ).click()
            wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@id='bulk_enroll']"))
            ).click()
            wait.until(
                EC.presence_of_element_located((By.NAME, "enrollment_file"))
            ).send_keys(students_json_file)
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

    def test_update_student_info(self):
        try:
            student_update_info = STUDENT_INFO["UPDATE_INFO"]
            wait = pytest.wait
            # Code for identification and feature testing
            wait.until(
                EC.element_to_be_clickable((By.ID, "menu-group__analytics"))
            ).click()
            wait.until(
                EC.element_to_be_clickable(
                    (By.ID, "menu-item__analytics__student_list")
                )
            ).click()
            wait.until(
                EC.element_to_be_clickable((By.ID, "update_student_data"))
            ).click()
            wait.until(EC.element_to_be_clickable((By.NAME, "csv_text"))).send_keys(
                student_update_info
            )
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[normalize-space()='Save']")
                )
            ).click()
            sleep(4)
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[normalize-space()='Close']")
                )
            ).click()
            return True
        except Exception as e:
            return False

    def test_student_groups(self):
        student_group_name = STUDENT_INFO["STUDENT_GROUP_NAME"]
        group_description = STUDENT_INFO["GROUP_DESCRIPTION"]
        try:
            wait = pytest.wait
            # Code for identification and feature testing
            wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//div[@id='menu-group__settings']//a[@class='mdl-navigation__link gcb-collapse__button']",
                    )
                )
            ).click()
            wait.until(
                EC.element_to_be_clickable(
                    (By.ID, "menu-item__settings__student_groups")
                )
            ).click()
            wait.until(
                EC.element_to_be_clickable((By.ID, "edit_student_group"))
            ).click()
            wait.until(EC.element_to_be_clickable((By.NAME, "name"))).send_keys(
                student_group_name
            )
            wait.until(EC.element_to_be_clickable((By.NAME, "description"))).send_keys(
                group_description
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

    def test_sync_scores(self):
        level = SYNC_SCORES["LEVEL"]
        term_code = SYNC_SCORES["TERM_CODE"]
        course_code = SYNC_SCORES["COURSE_CODE"]
        test_code = SYNC_SCORES["TEST_CODE"]
        calculation_type = SYNC_SCORES["CALCULATION_TYPE"]
        max_marks = SYNC_SCORES["MAX_MARKS"]
        driver = pytest.driver
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
                EC.element_to_be_clickable(
                    (By.ID, "menu-item__analytics__student_list")
                )
            ).click()
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='Sync Scores']")
                )
            ).click()
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[normalize-space()='Add Assignment']")
                )
            ).click()
            wait.until(EC.element_to_be_clickable((By.NAME, "level"))).send_keys(level)

            wait.until(EC.element_to_be_clickable((By.NAME, "term_code"))).send_keys(
                term_code
            )
            wait.until(EC.element_to_be_clickable((By.NAME, "course_code"))).send_keys(
                course_code
            )
            wait.until(EC.element_to_be_clickable((By.NAME, "test_code"))).send_keys(
                test_code
            )
            wait.until(
                EC.element_to_be_clickable((By.NAME, "marks_calculation_type"))
            ).send_keys(calculation_type)
            wait.until(EC.element_to_be_clickable((By.NAME, "marks_max"))).clear()
            wait.until(EC.element_to_be_clickable((By.NAME, "marks_max"))).send_keys(
                max_marks
            )
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[normalize-space()='Sync scores']")
                )
            ).click()
            element = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[normalize-space()='Close']")
                )
            )
            element.click()
            driver.switch_to.alert.accept()
            return True
        except Exception as e:
            return False
