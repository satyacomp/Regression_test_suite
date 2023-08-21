from conftest import *
from time import sleep
from selenium.webdriver.support.ui import Select


# Module stopped from execution because of many instances of VMs created
class Test_Background_Tasks(Dashboard_Test):
    # Test for background tasks
    def test_background_tasks(self):
        pass
        """wait = pytest.wait
        driver = pytest.driver
        try:
            # Code for identification and feature testing
            wait.until(
                EC.element_to_be_clickable((By.ID, "menu-group__analytics"))
            ).click()
            wait.until(
                EC.element_to_be_clickable(
                    (By.ID, "menu-item__analytics__background_jobs")
                )
            ).click()

            Select(driver.find_element(By.NAME, "job_name")).select_by_index(
                0
            )  # select rescore job type
            wait.until(EC.element_to_be_clickable((By.NAME, "Submit"))).click()
            Select(driver.find_element(By.NAME, "unit_id")).select_by_index(
                0
            )  # select unit_id
            wait.until(EC.element_to_be_clickable((By.NAME, "Submit"))).click()
            return True
        except Exception as e:
            return False"""
