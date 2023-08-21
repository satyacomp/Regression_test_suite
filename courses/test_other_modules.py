from conftest import *
from time import sleep
from constant import ANNOUNCEMENTS, COURSE_CATEGORY


class Test_Other_Modules(Dashboard_Test):
    def test_announcements(self):
        wait = pytest.wait
        driver = pytest.driver
        title = ANNOUNCEMENTS["TITLE"]
        description = ANNOUNCEMENTS["BODY"]
        try:
            # Code for identification and feature testing
            wait.until(
                EC.element_to_be_clickable((By.ID, "menu-group__analytics"))
            ).click()
            wait.until(
                EC.element_to_be_clickable(
                    (By.ID, "menu-item__analytics__announcements")
                )
            ).click()
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='Add Announcement']")
                )
            ).click()
            wait.until(EC.element_to_be_clickable((By.NAME, "title"))).clear()
            wait.until(EC.element_to_be_clickable((By.NAME, "title"))).send_keys(title)

            driver.switch_to.frame(1)
            body = driver.find_element("xpath", "//body")
            body.send_keys(description)
            driver.switch_to.default_content()

            chkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
            chkboxes[len(chkboxes) - 2].click()  # checkbox is send email

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

    def test_course_categories(self):
        wait = pytest.wait
        driver = pytest.driver
        name = COURSE_CATEGORY["CATEGORY_NAME"]
        description = COURSE_CATEGORY["CATEGORY_DESCRIPTION"]
        try:
            # Code for identification and feature testing
            wait.until(
                EC.element_to_be_clickable((By.ID, "menu-group__analytics"))
            ).click()
            wait.until(
                EC.element_to_be_clickable(
                    (By.ID, "menu-item__analytics__course_categories")
                )
            ).click()
            wait.until(
                EC.element_to_be_clickable((By.ID, "add_course_category"))
            ).click()
            wait.until(EC.element_to_be_clickable((By.NAME, "category"))).clear()
            wait.until(EC.element_to_be_clickable((By.NAME, "category"))).send_keys(
                name
            )
            wait.until(EC.element_to_be_clickable((By.NAME, "description"))).clear()
            wait.until(EC.element_to_be_clickable((By.NAME, "description"))).send_keys(
                description
            )
            chkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
            chkboxes[0].click()  # checkbox visible is enabled
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[normalize-space()='Add New Course Category']")
                )
            ).click()
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[normalize-space()='Close']")
                )
            ).click()
            return True
        except Exception as e:
            return False

    """def test_course_staff(self):
        pass

    def test_downloads(self):
        pass

    def test_local_chapters(self):
        pass

    def test_mentors(self):
        assert 5 == 5

    def test_offline_assignment_scores(self):
        pass

    def test_reports(self):
        pass"""
    """Types of reports
        Student Scores
        Question Dump
        Question Wise Scores
        Peer Grading dump
        Self Paced Exam Dump"""
