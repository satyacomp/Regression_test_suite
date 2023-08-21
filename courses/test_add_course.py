from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest
from constant import NEW_COURSE, MULTIPLE_COURSES, COURSE_AVAILABILITY, SAMPLE_COURSE
from conftest import *
from selenium import webdriver
from time import sleep

title = NEW_COURSE["TITLE"]
url_component = NEW_COURSE["URL_COMPONENT"]
start_due_date = COURSE_AVAILABILITY["COURSE_START_DATE"]
end_due_date = COURSE_AVAILABILITY["COURSE_END_DATE"]
sample_course_title = SAMPLE_COURSE["TITLE"]
sample_course_url_component = SAMPLE_COURSE["URL_COMPONENT"]


class Test_Add_Course_Module(Base_Test):
    def test_add_new_course(self):
        try:
            # Code for identification and feature testing
            wait = pytest.wait
            wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@id='add_course']"))
            ).click()
            wait.until(EC.element_to_be_clickable((By.NAME, "title"))).send_keys(title)
            wait.until(EC.element_to_be_clickable((By.NAME, "name"))).send_keys(
                url_component
            )
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='OK']")
                )
            ).click()
            return True
        except Exception as e:
            return False

    def test_add_multiple_courses(self):
        wait = pytest.wait
        courses = MULTIPLE_COURSES["COURSES"]
        try:
            sleep(3)
            wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@id='add_multiple_course']"))
            ).click()
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//textarea[@placeholder='urlpart, admin email, title']")
                )
            ).send_keys(courses)
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='OK']")
                )
            ).click()
            return True
        except Exception as e:
            return False

    def test_add_sample_course(self):
        wait = pytest.wait
        sleep(4)
        try:
            wait.until(EC.element_to_be_clickable((By.ID, "add_sample_course"))).click()
            wait.until(EC.element_to_be_clickable((By.NAME, "title"))).send_keys(title)
            wait.until(EC.element_to_be_clickable((By.NAME, "name"))).send_keys(
                url_component
            )
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='OK']")
                )
            ).click()
            return True
        except Exception as e:
            return False

    def test_course_availability(self):
        wait = pytest.wait
        driver = pytest.driver
        sleep(3)
        try:
            assert course_dashboard("Manual Course") == True, "Course not found"
            wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//div[@id='menu-group__publish']//a[@class='mdl-navigation__link gcb-collapse__button']",
                    )
                )
            ).click()
            wait.until(
                EC.element_to_be_clickable((By.ID, "menu-item__publish__availability"))
            ).click()
            Select(
                wait.until(EC.element_to_be_clickable((By.NAME, "course_availability")))
            ).select_by_index(
                1
            )  # Choose Lesson Availability to Registration open
            driver.execute_script(
                'document.getElementsByName("course_start[0]group-1[0]")[0].removeAttribute("readonly")'
            )
            driver.find_element("name", "course_start[0]group-1[0]").clear()
            driver.find_element("name", "course_start[0]group-1[0]").send_keys(
                start_due_date
            )

            driver.execute_script(
                'document.getElementsByName("course_end[0]group-1[0]")[0].removeAttribute("readonly")'
            )
            driver.find_element("name", "course_end[0]group-1[0]").clear()
            driver.find_element("name", "course_end[0]group-1[0]").send_keys(
                end_due_date
            )

            Select(
                wait.until(
                    EC.element_to_be_clickable((By.NAME, "course_start[0]availability"))
                )
            ).select_by_index(1)

            Select(
                wait.until(
                    EC.element_to_be_clickable((By.NAME, "course_end[0]availability"))
                )
            ).select_by_index(1)

            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[normalize-space()='Save']")
                )
            ).click()

            return True
        except Exception as e:
            return False
