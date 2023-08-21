from conftest import *
from time import sleep
from selenium.webdriver.support.ui import Select


# Module stopped from execution because of many instances of VMs created
class Test_BigQuery_Import(Dashboard_Test):
    # Test for background tasks
    def test_bigquery_import(self):
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
                    (By.ID, "menu-item__analytics__bigquery_dashboard")
                )
            ).click()

            wait.until(
                EC.element_to_be_clickable(
                    (By.NAME, "namespaces")
                )
            ).send_keys()
            wait.until(
                EC.element_to_be_clickable(
                    (By.NAME, "entity")
                )
            ).send_keys()
            wait.until(
                EC.element_to_be_clickable(
                    (By.NAME, "new_dataset")
                )
            ).send_keys()
            wait.until(
                EC.element_to_be_clickable(
                    (By.NAME, "existing_dataset")
                )
            ).send_keys()
            """
