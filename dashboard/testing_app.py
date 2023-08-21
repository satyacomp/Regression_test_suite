from datetime import datetime
import sys
import os
import json
import pandas as pd
import yaml


def read_json_file(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
    test_results = {}
    for test_output in data["tests"]:
        test_results[test_output["nodeid"]] = test_output["outcome"]
    return test_results


def write_results_to_csv(test_results, module_name):
    df = pd.read_csv("logs/test_suite_results_sheet.csv")
    module_start_row = {
        "add_course": 6,
        "course_content": 11,
        "user_management": 22,
        "exam": 29,
        "assessment_assignment": 34,
        "other_modules": 56,
    }
    if module_name in module_start_row:
        i = module_start_row[module_name]
        c = (
            2 if module_name == "add_course" else 1
        )  # add course module doesn't require specific Course dashboard
        for nodeid, outcome in test_results.items():
            if c <= 2:
                c += 1
                continue
            df.loc[i, "Actual Output"] = nodeid
            df.loc[i, "Status(Pass/Fail)"] = outcome
            i += 1
    df.to_csv("logs/test_suite_results_sheet.csv", index=False)


def set_environment(uid, password, url, course_name):
    with open(r"dashboard/app_config.yaml") as file:
        config_list = yaml.load(file, Loader=yaml.FullLoader)
    config_list["USER"] = uid
    config_list["PASSWORD"] = password
    config_list["LOCAL_URL"] = url
    config_list["COURSE_NAME"] = course_name
    with open(r"dashboard/app_config.yaml", "w") as file:
        yaml.dump(config_list, file)


def app():
    n = len(sys.argv)
    base_path = os.getcwd() + "/logs/"
    if n == 1:
        print(
            "List of modules: \n\tadd_course\n\tcourse_content\n\tuser_management\n\texam\n\tassessment_and_assignment\n\tother_modules"
        )
        print(
            "Usage: testing_app [-u <username> -p <password> -url=<testing_url> -c=<course_name>] <module1> <module2> ..."
        )
        print(
            'e.g1: with environment options: testing_app -u abc@gmail.com -p abc123 -url http://localhost:8082/modules/admin -c "Test Course1" exam'
        )
        print("e.g2: without environment options: testing_app exam")
        return
    elif (
        sys.argv[1] == "-u"
        and sys.argv[3] == "-p"
        and sys.argv[5] == "-url"
        and sys.argv[7] == "-c"
    ):
        set_environment(sys.argv[2], sys.argv[4], sys.argv[6], sys.argv[8])
        module_names = sys.argv[9:]  # get testing module names
    else:
        module_names = sys.argv[1:]  # get testing module names
    for module_name in module_names:
        test_file = "courses/test_" + module_name.lower().replace(" ", "_") + ".py"
        timestamp = datetime.strftime(datetime.now(), "%Y-%m-%d_%H-%M-%S")
        json_file = (
            base_path
            + module_name.lower().replace(" ", "_")
            + "_"
            + timestamp
            + ".json"
        )
        with open(json_file, "w") as f:
            pass
        os.system(
            "pytest --json-report --json-report-file=" + json_file + " -v " + test_file
        )

        test_results = read_json_file(json_file)
        write_results_to_csv(test_results, module_name.lower())


if __name__ == "__main__":
    app()
