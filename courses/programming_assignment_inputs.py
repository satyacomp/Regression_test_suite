from constant import (
    PYTHON_CODE,
    JAVA_CODE,
    JAVA_SCRIPT_CODE,
    BASH_CODE,
    PROGRAMMING_EVAL_SCRIPT_TYPE_HTML,
    PROGRAMMING_EVAL_SCRIPT_TYPE_SQL,
)


class ProgrammingAssignment:
    # constructor here
    def __init__(self, programming_language):
        self.programming_language = programming_language

    def get_assignment_test_cases_data(self):
        assignment_data = (
            PYTHON_CODE
            if self.programming_language == "Python"
            else JAVA_CODE
            if self.programming_language == "Java"
            else JAVA_SCRIPT_CODE
            if self.programming_language == "Java Script"
            else BASH_CODE
            if self.programming_language == "Bash"
            else None
        )
        return assignment_data

    def get_assignment_eval_script_data(self):
        assignment_data = (
            PROGRAMMING_EVAL_SCRIPT_TYPE_SQL
            if self.programming_language == "SQL"
            else PROGRAMMING_EVAL_SCRIPT_TYPE_HTML
            if self.programming_language == "HTML"
            else None
        )
        return assignment_data
