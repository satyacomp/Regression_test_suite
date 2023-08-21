from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pytest
import os
from time import sleep
from constant import (
    NEW_UNIT,
    MCQ,
    SAQ,
    GIFT_QUESTION,
    DOWNLOAD_QUESTIONS,
    UPLOAD_JSON_FILE,
    QUESTION_GROUPS,
    BULK_UPLOAD_QUESTION_GROUP,
    LABELS,
    TRACKS,
)
from conftest import *
from selenium.webdriver.support.ui import Select


class Test_Add_Course_Content(Dashboard_Test):
    # Test for open the course dashboard
    def test_addUnit(self):
        try:
            # Code for identification of elements
            sleep(2)
            wait = pytest.wait
            title = NEW_UNIT["TITLE"]
            description = NEW_UNIT["DESCRIPTION"]
            header = NEW_UNIT["HEADER"]
            footer = NEW_UNIT["FOOTER"]
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='Add Unit']")
                )
            ).click()
            wait.until(EC.element_to_be_clickable(By.NAME, "title")).clear()
            wait.until(EC.element_to_be_clickable(By.NAME, "title")).send_keys(title)
            wait.until(EC.element_to_be_clickable(By.NAME, "description")).send_keys(
                description
            )
            wait.until(
                EC.element_to_be_clickable(
                    By.XPATH, "//iframe[@id='yui-gen2000000_editor']"
                )
            ).send_keys(header)
            wait.until(
                EC.element_to_be_clickable(
                    By.XPATH, "//iframe[@id='yui-gen2000003_editor']"
                )
            ).send_keys(footer)
            wait.until(
                EC.element_tobe_clickable(By.XPATH, "//span[normalize-space()='Save']")
            ).click()
            wait.until(
                EC.element_to_be_clickable(
                    By.XPATH, "//span[normalize-space()='Close']"
                )
            ).click()
            return True
        except Exception as e:
            return False

    def test_add_MCQs(self):
        driver = pytest.driver
        wait = pytest.wait
        question = MCQ["QUESTION"]
        choice1 = MCQ["CHOICE1"]
        choice2 = MCQ["CHOICE2"]
        choice3 = MCQ["CHOICE3"]
        choice4 = MCQ["CHOICE4"]
        correct_choice = MCQ["CORRECT_CHOICE"]
        description = MCQ["DESCRIPTION"]
        # Test for adding new Multiple Choice Question
        try:
            # Code for identification and feature testing
            sleep(2)
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[@id='menu-item__edit__questions']")
                )
            ).click()

            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[normalize-space()='Add Multiple Choice']")
                )
            ).click()
            for i in range(0, 3):
                wait.until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//a[normalize-space()='Add a choice']")
                    )
                ).click()

            # Frame-1
            driver.switch_to.frame(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//body"))).send_keys(
                question
            )

            driver.switch_to.default_content()

            # Frame-5
            driver.switch_to.frame(5)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//body"))).send_keys(
                choice1
            )

            driver.switch_to.default_content()

            # Frame-9
            driver.switch_to.frame(9)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//body"))).send_keys(
                choice2
            )

            driver.switch_to.default_content()

            # Frame-13
            driver.switch_to.frame(13)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//body"))).send_keys(
                choice3
            )

            driver.switch_to.default_content()

            # Frame-17
            driver.switch_to.frame(17)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//body"))).send_keys(
                choice4
            )

            driver.switch_to.default_content()
            rdobuttons = driver.find_elements("xpath", "//input[@type='radio']")
            rdobuttons[6].click()  # select 3rd choice as correct answer

            driver.switch_to.default_content()  # Continue with default content
            wait.until(EC.element_to_be_clickable((By.NAME, "description"))).send_keys(
                description
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

    def test_add_SAQs(self):
        wait = pytest.wait
        question = SAQ["QUESTION"]
        hint = SAQ["HINT"]
        answer = SAQ["ANSWER"]
        description = SAQ["DESCRIPTION"]
        try:
            sleep(2)
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[@id='menu-item__edit__questions']")
                )
            ).click()

            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[normalize-space()='Add Short Answer']")
                )
            ).click()

            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//iframe[@id='yui-gen2000000_editor']")
                )
            ).send_keys(question)

            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//iframe[@id='yui-gen2000003_editor']")
                )
            ).send_keys(hint)

            wait.until(
                EC.element_to_be_clickable((By.NAME, "graders[0]response"))
            ).send_keys(answer)

            wait.until(EC.element_to_be_clickable((By.NAME, "description"))).send_keys(
                description
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

    def test_add_GIFT(self):
        wait = pytest.wait
        description = GIFT_QUESTION["GROUP_DESCRIPTION"]
        questions = GIFT_QUESTION["QUESTIONS"]
        driver = pytest.driver
        try:
            sleep(2)
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[@id='menu-item__edit__questions']")
                )
            ).click()
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[normalize-space()='Add GIFT Questions']")
                )
            ).click()
            wait.until(EC.element_to_be_clickable((By.NAME, "description"))).send_keys(
                description
            )

            wait.until(EC.element_to_be_clickable((By.NAME, "questions"))).send_keys(
                questions
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
            driver.switch_to.alert.accept()
            return True
        except Exception as e:
            return False

    def test_bulk_download_questions(self):
        wait = pytest.wait
        description = DOWNLOAD_QUESTIONS["DESCRIPTION"]
        try:
            sleep(2)
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[@id='menu-item__edit__questions']")
                )
            ).click()
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[normalize-space()='Bulk Download']")
                )
            ).click()

            wait.until(EC.element_to_be_clickable((By.NAME, "csv_text"))).send_keys(
                description
            )

            wait.until(
                EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox']"))
            ).click()
            Select(
                wait.until(EC.element_to_be_clickable((By.NAME, "location")))
            ).select_by_index(
                1
            )  # Choose save location to cloud storage

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

    def test_bulk_upload_questions(self):
        wait = pytest.wait
        json_file = os.getcwd() + UPLOAD_JSON_FILE
        driver = pytest.driver
        try:
            sleep(2)
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[@id='menu-item__edit__questions']")
                )
            ).click()
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[normalize-space()='Bulk Upload Questions']")
                )
            ).click()
            sleep(2)
            wait.until(EC.presence_of_element_located((By.NAME, "file"))).send_keys(
                json_file
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

    def test_add_question_groups(self):
        wait = pytest.wait
        driver = pytest.driver
        description = QUESTION_GROUPS["DESCRIPTION"]
        introduction = QUESTION_GROUPS["INTRODUCTION"]
        try:
            sleep(4)
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[@id='menu-item__edit__groups']")
                )
            ).click()
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[normalize-space()='Add Question Group']")
                )
            ).click()

            wait.until(EC.element_to_be_clickable((By.NAME, "description"))).send_keys(
                description
            )

            driver.switch_to.frame(1)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//body"))).send_keys(
                introduction
            )

            driver.switch_to.default_content()  # Continue with default frame
            # Adding first question into group
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[normalize-space()='Add a question']")
                )
            ).click()

            wait.until(
                EC.element_to_be_clickable((By.NAME, "items[0]weight"))
            ).send_keys("1")

            Select(driver.find_element(By.NAME, "items[0]question")).select_by_index(0)

            # Adding 2nd question into group
            driver.switch_to.default_content()  # Continue with default frame
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[normalize-space()='Add a question']")
                )
            ).click()

            wait.until(
                EC.element_to_be_clickable((By.NAME, "items[1]weight"))
            ).send_keys("1")
            Select(driver.find_element(By.NAME, "items[1]question")).select_by_index(1)

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

    def test_bulk_upload_question_groups(
        self,
    ):  # Server did not respond. Please reload the page to try again.
        wait = pytest.wait
        description = BULK_UPLOAD_QUESTION_GROUP["DESCRIPTION"]
        questions = BULK_UPLOAD_QUESTION_GROUP["QUESTION_DESCRIPTIONS"]
        try:
            sleep(2)
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[@id='menu-item__edit__groups']")
                )
            ).click()
            wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//a[normalize-space()='Bulk Upload Question Group']",
                    )
                )
            ).click()
            wait.until(
                EC.element_to_be_clickable(
                    (
                        By.NAME,
                        "question_group_description",
                    )
                )
            ).send_keys(description)

            wait.until(
                EC.element_to_be_clickable(
                    (
                        By.NAME,
                        "csv_text",
                    )
                )
            ).send_keys(questions)

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

    def test_upload_html_img_files(self):
        wait = pytest.wait
        htmlfilepath = os.getcwd() + "/src/sample.html"
        imgfilepath = os.getcwd() + "/src/spider.png"
        driver = pytest.driver
        try:
            sleep(2)
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[@id='menu-item__edit__questions']")
                )
            ).click()
            # Issue with uploading html files
            """wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[@id='menu-item__edit__html']")
                )
            ).click()
            wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@id='upload-button']"))
            ).click()
            wait.until(EC.presence_of_element_located((By.NAME, "file"))).send_keys(
                htmlfilepath
            )
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[normalize-space()='Upload']")
                )
            ).click()
            sleep(2)
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[normalize-space()='Close']")
                )
            ).click()"""
            # upload image files
            wait.until(
                EC.element_to_be_clickable((By.ID, "menu-item__edit__images"))
            ).click()
            wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@id='upload-button']"))
            ).click()
            wait.until(EC.presence_of_element_located((By.NAME, "file"))).send_keys(
                imgfilepath
            )
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[normalize-space()='Upload']")
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

    def test_add_labels_tracks(self):
        wait = pytest.wait
        label_name = LABELS["LABEL_NAME"]
        description = LABELS["LABEL_DESCRIPTION"]
        track_title = TRACKS["TRACK_TITLE"]
        track_description = TRACKS["TRACK_DESCRIPTION"]
        try:
            sleep(2)
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[@id='menu-item__edit__questions']")
                )
            ).click()
            wait.until(
                EC.element_to_be_clickable((By.ID, "menu-item__edit__labels"))
            ).click()
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[normalize-space()='Add Label']")
                )
            ).click()
            wait.until(EC.element_to_be_clickable((By.NAME, "title"))).clear()
            wait.until(EC.element_to_be_clickable((By.NAME, "title"))).send_keys(
                label_name
            )
            wait.until(EC.element_to_be_clickable((By.NAME, "description"))).send_keys(
                description
            )
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[normalize-space()='Save']")
                )
            ).click()

            sleep(2)
            wait.until(
                EC.element_to_be_clickable((By.ID, "menu-item__edit__tracks"))
            ).click()

            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[normalize-space()='Add Track']")
                )
            ).click()

            wait.until(EC.element_to_be_clickable((By.NAME, "title"))).clear()
            wait.until(EC.element_to_be_clickable((By.NAME, "title"))).send_keys(
                track_title
            )
            wait.until(EC.element_to_be_clickable((By.NAME, "description"))).send_keys(
                track_description
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
