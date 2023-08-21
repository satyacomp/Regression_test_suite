from conftest import *
from constant import (
    NEW_UNIT,
    NEW_TEXT_LESSON,
    NEW_VIDEO_LESSON,
    NEW_PDF_LESSON,
    LINK,
    SINGLE_ASSESSMENT,
    SUBJECTIVE_ASSIGNMENT,
    PROGRAMMING_EVAL_SCRIPT_TYPE_HTML,
    PROGRAMMING_ASSIGNMENT_TEST_CASES,
)
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from programming_assignment_inputs import ProgrammingAssignment


class Test_Asssesment_Assignment_Content(Dashboard_Test):
    # Test for open the course dashboard
    def test_add_unit(self):
        driver = pytest.driver
        wait = pytest.wait
        title = NEW_UNIT["TITLE"]
        description = NEW_UNIT["DESCRIPTION"]
        header = NEW_UNIT["HEADER"]
        footer = NEW_UNIT["FOOTER"]
        try:
            # Code for identification of elements
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='Add Unit']")
                )
            ).click()
            wait.until(EC.element_to_be_clickable((By.NAME, "title"))).clear()
            wait.until(EC.element_to_be_clickable((By.NAME, "title"))).send_keys(title)
            wait.until(EC.element_to_be_clickable((By.NAME, "description"))).send_keys(
                description
            )
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//iframe[@id='yui-gen2000000_editor']")
                )
            ).send_keys(header)
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//iframe[@id='yui-gen2000003_editor']")
                )
            ).send_keys(footer)
            js_code = "arguments[0].scrollIntoView();"
            element = driver.find_element(By.XPATH, "//span[normalize-space()='Save']")
            driver.execute_script(js_code, element)
            element.click()
            sleep(2)
            element = driver.find_element(By.XPATH, "//span[normalize-space()='Close']")
            driver.execute_script(js_code, element)
            element.click()
            return True
        except Exception as e:
            return False

    def test_add_text_lesson(self):
        driver = pytest.driver
        wait = pytest.wait
        title = NEW_TEXT_LESSON["TITLE"]
        lesson_body = NEW_TEXT_LESSON["BODY"]
        try:
            # Code for identification of elements
            lessons_lst = driver.find_elements(
                "xpath", "//*[contains(text(), '+Lesson')]"
            )
            lessons_lst[
                len(lessons_lst) - 1
            ].click()  # add text lesson to recent added unit
            wait.until(EC.element_to_be_clickable((By.NAME, "title"))).clear()
            wait.until(EC.element_to_be_clickable((By.NAME, "title"))).send_keys(title)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//html"))).click()
            iframes = driver.find_elements("xpath", "//iframe")
            for index, iframe in enumerate(iframes):
                driver.switch_to.frame(index)
                body = driver.find_element("xpath", "//body")
                if body != []:
                    break
            body.send_keys(lesson_body)
            driver.switch_to.default_content()  # Continue with default content
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

    def test_add_video_lesson(self):
        driver = pytest.driver
        wait = pytest.wait
        title = NEW_VIDEO_LESSON["TITLE"]
        video_id = NEW_VIDEO_LESSON["VIDEO_ID"]
        transcipt_vtt = NEW_VIDEO_LESSON["TRANSCRIPT_VTT"]
        try:
            # Code for identification of elements
            lessons_lst = driver.find_elements(
                "xpath", "//*[contains(text(), '+Lesson')]"
            )
            lessons_lst[
                len(lessons_lst) - 1
            ].click()  # add text lesson to recent added unit
            wait.until(EC.element_to_be_clickable((By.NAME, "title"))).clear()
            wait.until(EC.element_to_be_clickable((By.NAME, "title"))).send_keys(title)
            wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//label[@class='gcb-toggle-button gcb-toggle-button--alone settings md md-settings']",
                    )
                )
            ).click()
            wait.until(EC.element_to_be_clickable((By.NAME, "video"))).send_keys(
                video_id
            )
            wait.until(
                EC.element_to_be_clickable((By.NAME, "transcript_vtt_url"))
            ).send_keys(transcipt_vtt)
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

    # Not working
    def test_add_pdf_lesson(self):
        driver = pytest.driver
        wait = pytest.wait
        title = NEW_PDF_LESSON["TITLE"]
        url = NEW_PDF_LESSON["URL"]
        try:
            # Code for identification of elements
            lessons_lst = driver.find_elements(
                "xpath", "//*[contains(text(), '+Lesson')]"
            )
            lessons_lst[
                len(lessons_lst) - 1
            ].click()  # add text lesson to recent added unit
            wait.until(EC.element_to_be_clickable((By.NAME, "title"))).clear()
            wait.until(EC.element_to_be_clickable((By.NAME, "title"))).send_keys(title)
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='code']")
                )
            ).click()
            iframes = driver.find_elements("xpath", "//iframe")
            for index, iframe in enumerate(iframes):
                driver.switch_to.frame(index)
                body = driver.find_element("xpath", "//body")
                if body != []:
                    break
            body.send_keys(url)
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

    def test_add_link(self):
        driver = pytest.driver
        wait = pytest.wait
        title = LINK["TITLE"]
        description = LINK["DESCRIPTION"]
        url = LINK["URL"]
        try:
            # Code for identification of elements
            links_lst = driver.find_elements(
                "xpath", "//button[normalize-space()='+Link']"
            )
            links_lst[len(links_lst) - 1].click()  # add text link to recent added unit
            wait.until(EC.element_to_be_clickable((By.NAME, "title"))).clear()
            wait.until(EC.element_to_be_clickable((By.NAME, "title"))).send_keys(title)
            wait.until(EC.element_to_be_clickable((By.NAME, "description"))).send_keys(
                description
            )
            wait.until(EC.element_to_be_clickable((By.NAME, "url"))).send_keys(url)
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

    # Unit Test for adding new Graded assessment(single/multiple submission)
    @pytest.mark.parametrize(
        "assessment_type",
        [
            ("GRADED_SINGLE_ASSESSMENT"),
            ("GRADED_MULTIPLE_ASSESSMENT"),
            ("PRACTICE_SINGLE_ASSESSMENT"),
            ("PRACTICE_MULTIPLE_ASSESSMENT"),
        ],
    )
    def test_add_graded_and_practice_assessment(self, assessment_type):
        driver = pytest.driver
        wait = pytest.wait
        title = assessment_type
        points = SINGLE_ASSESSMENT["POINTS"]
        content = SINGLE_ASSESSMENT["CONTENT"]
        due_date = SINGLE_ASSESSMENT["DUE_DATE"]
        availability = SINGLE_ASSESSMENT["AVAILABILITY"]
        try:
            # Code for identification and feature testing
            assignment_lst = driver.find_elements(
                "xpath", "//*[contains(text(), '+Assessment')]"
            )
            assignment_lst[
                len(assignment_lst) - 1
            ].click()  # add assignment to recent added unit
            wait.until(EC.element_to_be_clickable((By.NAME, "title"))).clear()
            wait.until(EC.element_to_be_clickable((By.NAME, "title"))).send_keys(title)
            wait.until(EC.element_to_be_clickable((By.NAME, "weight"))).clear()
            wait.until(EC.element_to_be_clickable((By.NAME, "weight"))).send_keys(
                points
            )

            driver.switch_to.frame(1)
            body = driver.find_element("xpath", "//body")
            body.send_keys(content)
            driver.switch_to.default_content()

            if (
                assessment_type == "PRACTICE_SINGLE_ASSESSMENT"
                or assessment_type == "PRACTICE_MULTIPLE_ASSESSMENT"
            ):
                wait.until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//label[normalize-space()='Practice Question']")
                    )
                ).click()

            # Identify checkbox for single submission
            if (
                assessment_type == "GRADED_SINGLE_ASSESSMENT"
                or assessment_type == "PRACTICE_SINGLE_ASSESSMENT"
            ):
                chkboxes = driver.find_elements("xpath", "//input[@type='checkbox']")
                chkboxes[len(chkboxes) - 4].click()  # checkbox is single submission

            driver.execute_script(
                'document.getElementsByName("workflow:submission_due_date[0]")[0].removeAttribute("readonly");'
            )
            wait.until(
                EC.element_to_be_clickable((By.NAME, "workflow:submission_due_date[0]"))
            ).send_keys(due_date)
            Select(
                wait.until(EC.element_to_be_clickable((By.NAME, "availability")))
            ).select_by_index(
                availability
            )  # Choose Availability to Course
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

    # Unit Test for adding new Subjective assignment(Essay or file - single/multiple submission)
    @pytest.mark.parametrize(
        "assignment_type,evaluation_type,grading_method,submission_type",
        [
            ("ESSAY", "COURSE STAFF", "CRITERIA", "MUTLITPLE"),
            ("ESSAY", "COURSE STAFF", "RUBRICS", "SINGLE"),
            ("ESSAY", "PEER GRADE", "CRITERIA", "MUTLITPLE"),
            ("FILE UPLOAD", "PEER GRADE", "RUBRICS", "SINGLE"),
            ("FILE UPLOAD", "COURSE STAFF", "CRITERIA", "SINGLE"),
            ("FILE UPLOAD", "COURSE STAFF", "RUBRICS", "MULTIPLE"),
        ],
    )
    def test_add_subjective_assignment(
        self, assignment_type, evaluation_type, grading_method, submission_type
    ):
        driver = pytest.driver
        wait = pytest.wait
        title = (
            assignment_type
            + "-"
            + evaluation_type
            + "-"
            + grading_method
            + "-"
            + submission_type
        )
        points = SUBJECTIVE_ASSIGNMENT["POINTS"]
        problem = SUBJECTIVE_ASSIGNMENT["PROBLEM"]
        due_date = SUBJECTIVE_ASSIGNMENT["DUE_DATE"]
        std_due_date = SUBJECTIVE_ASSIGNMENT["STUD_DUE_DATE"]
        staff_due_date = SUBJECTIVE_ASSIGNMENT["STAFF_DUE_DATE"]
        rubrics = SUBJECTIVE_ASSIGNMENT["RUBRICS"]
        try:
            assignment_lst = driver.find_elements(
                "xpath", "//*[contains(text(), '+Subjective Assignment')]"
            )
            assignment_lst[
                len(assignment_lst) - 1
            ].click()  # add subjective assignment to recent added unit
            wait.until(EC.element_to_be_clickable((By.NAME, "title"))).clear()
            wait.until(EC.element_to_be_clickable((By.NAME, "title"))).send_keys(title)
            wait.until(EC.element_to_be_clickable((By.NAME, "weight"))).clear()
            wait.until(EC.element_to_be_clickable((By.NAME, "weight"))).send_keys(
                points
            )
            driver.switch_to.frame(1)
            body = driver.find_element("xpath", "//body")
            body.send_keys(problem)
            sleep(2)
            driver.switch_to.default_content()

            driver.execute_script(
                'document.getElementsByName("workflow:submission_due_date[0]")[0].removeAttribute("readonly")'
            )
            wait.until(
                EC.element_to_be_clickable((By.NAME, "workflow:submission_due_date[0]"))
            ).send_keys(due_date)

            if assignment_type == "FILE UPLOAD":
                # Selecting Assignment type File upload
                Select(driver.find_element("name", "content:type")).select_by_index(1)

            if evaluation_type == "PEER GRADE":
                # Selecting peer-grade evaluation type drop-down
                Select(
                    driver.find_element("name", "workflow:evaluation_type")
                ).select_by_index(1)
                driver.execute_script(
                    'document.getElementsByName("workflow:student_eval_due_date[0]")[0].removeAttribute("readonly")'
                )
                wait.until(
                    EC.element_to_be_clickable(
                        (By.NAME, "workflow:student_eval_due_date[0]")
                    )
                ).send_keys(std_due_date)
                driver.execute_script(
                    'document.getElementsByName("workflow:course_staff_eval_due_date[0]")[0].removeAttribute("readonly")'
                )
                wait.until(
                    EC.element_to_be_clickable(
                        (By.NAME, "workflow:course_staff_eval_due_date[0]")
                    )
                ).send_keys(staff_due_date)

            if grading_method == "RUBRICS":
                # Choose option Grading method Rubrics
                Select(
                    driver.find_element("name", "content:grading_method")
                ).select_by_index(1)
                wait.until(
                    EC.element_to_be_clickable((By.NAME, "content:rubrics"))
                ).send_keys(rubrics)

            if submission_type == "SINGLE":
                Select(
                    driver.find_element("name", "workflow:submit_only_once")
                ).select_by_index(1)

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

    @pytest.mark.parametrize(
        "program_evaluator,evaluation_script,randomization_mode",
        [
            ("ns_jail", "SQL", "graded"),
            ("ns_jail", "HTML", "practice"),
        ],
    )
    def test_add_programming_assignment_evaluation_script(
        self, program_evaluator, evaluation_script, randomization_mode
    ):
        driver = pytest.driver
        wait = pytest.wait
        title = (
            "Programming Assignment(Evaluation Script)-"
            + program_evaluator
            + "-"
            + evaluation_script
            + "-"
            + randomization_mode
        )
        weight = 2
        prog_assignment = ProgrammingAssignment(evaluation_script)
        eval_script_data = prog_assignment.get_assignment_eval_script_data()
        due_date = PROGRAMMING_EVAL_SCRIPT_TYPE_HTML["DUE_DATE"]
        try:
            assignment_lst = driver.find_elements(
                "xpath", "//*[contains(text(), '+Programming Assignment')]"
            )
            assignment_lst[
                len(assignment_lst) - 1
            ].click()  # add programming assignment to recent added unit

            wait.until(EC.element_to_be_clickable((By.NAME, "title"))).clear()
            wait.until(EC.element_to_be_clickable((By.NAME, "title"))).send_keys(title)
            wait.until(EC.element_to_be_clickable((By.NAME, "weight"))).clear()
            wait.until(EC.element_to_be_clickable((By.NAME, "weight"))).send_keys(
                weight
            )
            # Exclusive implementation for Code Mirror element
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//div[@class='gcb-toggle-button-bar']")
                )
            ).click()
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='code']")
                )
            ).click()
            codeMirror = driver.find_element(
                By.XPATH, "//div[@class='CodeMirror-scroll']"
            )
            actions = ActionChains(driver)
            actions.move_to_element(codeMirror)
            actions.click()
            actions.send_keys(eval_script_data["PROBLEM"])
            actions.perform()
            sleep(2)
            driver.switch_to.default_content()
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//label[normalize-space()='Allow \"Compile & Run\"']")
                )
            ).click()
            wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//label[normalize-space()='Ignore Presentation Errors']",
                    )
                )
            ).click()

            Select(driver.find_element("name", "content:evaluator")).select_by_index(
                2
            )  # Choose nsjail as evaluator
            Select(
                driver.find_element("name", "workflow:evaluation_type")
            ).select_by_index(
                1
            )  # Choose evaluation type script

            driver.execute_script(
                'document.getElementsByName("workflow:submission_due_date[0]")[0].removeAttribute("readonly")'
            )
            driver.find_element("name", "workflow:submission_due_date[0]").send_keys(
                due_date
            )

            # Private and public evaluation script
            wait.until(
                EC.element_to_be_clickable(
                    (By.NAME, "content:private_evaluation_script")
                )
            ).send_keys(eval_script_data["PRIVATE_EVAL_SCRIPT"])
            wait.until(
                EC.element_to_be_clickable(
                    (By.NAME, "content:private_evaluation_script_lang")
                )
            ).send_keys(eval_script_data["EVAL_SCRIPT_LANG"])

            wait.until(
                EC.element_to_be_clickable(
                    (By.NAME, "content:public_evaluation_script")
                )
            ).send_keys(eval_script_data["PUBLIC_EVAL_SCRIPT"])
            wait.until(
                EC.element_to_be_clickable(
                    (By.NAME, "content:public_evaluation_script_lang")
                )
            ).send_keys(eval_script_data["EVAL_SCRIPT_LANG"])
            wait.until(
                EC.element_to_be_clickable((By.NAME, "content:randomization_script"))
            ).send_keys(eval_script_data["RANDOMIZATION_SCRIPT"])
            wait.until(
                EC.element_to_be_clickable(
                    (By.NAME, "content:randomization_script_lang")
                )
            ).send_keys(eval_script_data["RANDOMIZATION_SCRIPT_LANGUAGE"])
            # Zip editor language
            Select(
                driver.find_element("name", "content:zip_editor_lang")
            ).select_by_index(
                eval_script_data["ZIP_EDITOR_LANG"]
            )  # Choose option SQL

            if randomization_mode == "practice":
                wait.until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//label[normalize-space()='Practice']")
                    )
                ).click()  # select Practice type of randomization

            driver.switch_to.default_content()
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

    @pytest.mark.parametrize(
        "programming_language", ["Python", "Bash", "Java", "Java Script"]
    )
    def test_add_programming_assignment_testcases(self, programming_language):
        driver = pytest.driver
        wait = pytest.wait
        title = "Programming Assignment(Test Cases)-" + programming_language
        weight = PROGRAMMING_ASSIGNMENT_TEST_CASES["WEIGHT"]
        due_date = PROGRAMMING_ASSIGNMENT_TEST_CASES["DUE_DATE"]
        prog_assignment = ProgrammingAssignment(programming_language)
        assignment_data = prog_assignment.get_assignment_test_cases_data()
        try:
            assignment_lst = driver.find_elements(
                "xpath", "//*[contains(text(), '+Programming Assignment')]"
            )
            assignment_lst[
                len(assignment_lst) - 1
            ].click()  # add programming assignment to recent added unit
            wait.until(EC.element_to_be_clickable((By.NAME, "title"))).clear()
            wait.until(EC.element_to_be_clickable((By.NAME, "title"))).send_keys(title)
            wait.until(EC.element_to_be_clickable((By.NAME, "weight"))).clear()
            wait.until(EC.element_to_be_clickable((By.NAME, "weight"))).send_keys(
                weight
            )
            # Exclusive implementation for Code Mirror element
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//div[@class='gcb-toggle-button-bar']")
                )
            ).click()
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[normalize-space()='code']")
                )
            ).click()
            codeMirror = driver.find_element(
                By.XPATH, "//div[@class='CodeMirror-scroll']"
            )
            actions = ActionChains(driver)
            actions.move_to_element(codeMirror)
            actions.click()
            actions.send_keys(assignment_data["PROBLEM"])
            actions.perform()
            sleep(2)
            driver.switch_to.default_content()
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//label[normalize-space()='Allow \"Compile & Run\"']")
                )
            ).click()
            wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//label[normalize-space()='Ignore Presentation Errors']",
                    )
                )
            ).click()

            Select(driver.find_element("name", "content:evaluator")).select_by_index(
                2
            )  # Choose nsjail as evaluator

            driver.execute_script(
                'document.getElementsByName("workflow:submission_due_date[0]")[0].removeAttribute("readonly")'
            )
            driver.find_element("name", "workflow:submission_due_date[0]").send_keys(
                due_date
            )

            i = 0
            for public_test_input in assignment_data["PUBLIC_TEST_CASE_INPUTS"]:
                # Adding each  public test case
                wait.until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//a[normalize-space()='Add Public Test Case']")
                    )
                ).click()
                wait.until(
                    EC.element_to_be_clickable(
                        (By.NAME, "content:public_testcase[" + str(i) + "]input")
                    )
                ).send_keys(public_test_input)
                i = i + 1

            i = 0  # reset index
            for public_test_output in assignment_data["PUBLIC_TEST_CASE_OUTPUTS"]:
                wait.until(
                    EC.element_to_be_clickable(
                        (By.NAME, "content:public_testcase[" + str(i) + "]output")
                    )
                ).send_keys(public_test_output)
                i = i + 1

            i = 0
            for private_test_input in assignment_data["PRIVATE_TEST_CASE_INPUTS"]:
                # Add private test cases
                wait.until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//a[normalize-space()='Add Private Test Case']")
                    )
                ).click()
                wait.until(
                    EC.element_to_be_clickable(
                        (By.NAME, "content:private_testcase[" + str(i) + "]input")
                    )
                ).send_keys(private_test_input)
                i = i + 1

            i = 0  # reset index
            for private_test_output in assignment_data["PRIVATE_TEST_CASE_OUTPUTS"]:
                wait.until(
                    EC.element_to_be_clickable(
                        (By.NAME, "content:private_testcase[" + str(i) + "]output")
                    )
                ).send_keys(private_test_output)
                i = i + 1

            wait.until(
                EC.element_to_be_clickable(
                    (By.NAME, "content:allowed_languages[0]code_template")
                )
            ).send_keys(assignment_data["TEMPLATE_CODE"])
            wait.until(
                EC.element_to_be_clickable(
                    (By.NAME, "content:allowed_languages[0]suffixed_invisible_code")
                )
            ).send_keys(assignment_data["INVISIBLE_CODE"])
            wait.until(
                EC.element_to_be_clickable(
                    (By.NAME, "content:allowed_languages[0]sample_solution")
                )
            ).send_keys(assignment_data["SAMPLE_SOLUTION"])
            wait.until(
                EC.element_to_be_clickable(
                    (By.NAME, "content:allowed_languages[0]filename")
                )
            ).send_keys(assignment_data["SAMPLE_SOLUTION_FILE"])

            wait.until(
                EC.element_to_be_clickable(
                    (
                        By.NAME,
                        "content:allowed_languages[0]prefixed_code",
                    )
                )
            ).send_keys(assignment_data["PREFIXED_CODE"])
            wait.until(
                EC.element_to_be_clickable(
                    (
                        By.NAME,
                        "content:allowed_languages[0]uneditable_code",
                    )
                )
            ).send_keys(assignment_data["SUFFIXED_CODE"])
            driver.switch_to.default_content()
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
