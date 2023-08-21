from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import yaml
import logging

log = logging.getLogger(__name__)

pytest.driver = None  # global variable
pytest.wait = None
with open(r"dashboard/app_config.yaml") as file:
    config_list = yaml.load(file, Loader=yaml.FullLoader)

TEST_URL = config_list["LOCAL_URL"]
USER = config_list["USER"]
PWD = config_list["PASSWORD"]
COURSE = config_list["COURSE_NAME"]
CHROME_DRIVER_VERSION = config_list["CHROME_DRIVER_VERSION"]


@pytest.fixture(scope="class")
def init_driver(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    pytest.driver = webdriver.Chrome(options=options)
    pytest.driver.maximize_window()
    pytest.wait = WebDriverWait(pytest.driver, 20)
    pytest.driver.get(TEST_URL)


"""def teardown_module(module):
    print("\nChrome web driver closed..")
    pytest.driver.quit()"""


def user_login():
    driver = pytest.driver
    wait = pytest.wait
    try:
        main_page = driver.current_window_handle
        driver.find_element(
            "xpath", "//span[@class='firebaseui-idp-text firebaseui-idp-text-long']"
        ).click()
        for handle in driver.window_handles:
            if handle != main_page:
                login_page = handle
                break
        # change the control to signin pop window
        driver.switch_to.window(login_page)
        wait.until(EC.element_to_be_clickable((By.NAME, "identifier"))).send_keys(USER)
        nextButton = driver.find_elements("xpath", "//span[normalize-space()='Next']")
        nextButton[0].click()
        wait.until(EC.element_to_be_clickable((By.NAME, "Passwd"))).send_keys(PWD)
        # nextButton = driver.find_elements(By.XPATH, "//span[normalize-space()='Next']")
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Next']"))
        ).click()
        # nextButton[0].click()
        driver.switch_to.window(main_page)  # move back from login to main page
        return True
    except Exception as e:
        print(e.message)
        return False


def course_dashboard(course_name):
    try:
        driver = pytest.driver
        wait = pytest.wait
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[normalize-space()='" + course_name + "']")
            )
        ).click()
        return True
    except Exception as e:
        return False


@pytest.mark.usefixtures("init_driver")
class Base_Test:
    def test_user_login(self):
        assert user_login() == True, "User Login test case failed"


class Dashboard_Test(Base_Test):
    def test_course_dashboard(self):
        assert course_dashboard(COURSE) == True, "Course Dashboard test case failed"
