from datetime import datetime
from datetime import timedelta
import random
import string
import yaml

# Global variables with 15-days
curr_date = datetime.now()
due_date = curr_date + timedelta(days=15)
std_due_date = curr_date + timedelta(days=17)
staff_due_date = curr_date + timedelta(days=19)

# Global variables for exam_info
utc_dt = datetime.utcnow()
exam_from = utc_dt.strftime("%Y-%m-%dT%H:%M:%S.0Z")
utc_dt = datetime.utcnow() + timedelta(days=2)  # add two days due for exam
exam_to = utc_dt.strftime("%Y-%m-%dT%H:%M:%S.0Z")


# Generate random string for question description
def get_random_string():
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = "".join(random.choice(letters) for i in range(8))
    return result_str


# Generate random number for adding new course<no>
def get_random_number():
    return random.randint(1, 1000)


course_number = get_random_number()
NEW_COURSE = {
    "TITLE": "New Course" + str(course_number),
    "URL_COMPONENT": "new_course" + str(course_number),
}

SAMPLE_COURSE = {
    "TITLE": "Sample Course" + str(course_number),
    "URL_COMPONENT": "sample_course" + str(course_number),
}

MULTIPLE_COURSES = {
    "COURSES": "sample_course"
    + str(course_number)
    + ", abc@study.iitm.ac.in, Sample Course"
    + str(course_number)
    + "\n"
    + "temp_course"
    + str(course_number)
    + ", xyz@study.iitm.ac.in, Temporary Course"
    + str(course_number)
    + "\n"
    + "real_course"
    + str(course_number)
    + ", zzz@study.iitm.ac.in, Real Course"
    + str(course_number)
}

COURSE_AVAILABILITY = {
    "COURSE_START_DATE": curr_date.strftime("%m/%d/%Y"),
    "COURSE_END_DATE": due_date.strftime("%m/%d/%Y"),
}

NEW_UNIT = {
    "TITLE": "Unit Title " + get_random_string(),
    "DESCRIPTION": "Unit description " + get_random_string(),
    "TRACKS": False,
    "SHOW_ON_ONE_PAGE": False,
    "ALLOW_MANUAL_COMPLETION": False,
    "HEADER": "Header " + get_random_string(),
    "FOOTER": "Footer " + get_random_string(),
    "SHOW_CORRECT_ANSWER": False,
    "AVAILABILITY": "Private",
}

NEW_VIDEO_LESSON = {
    "TITLE": "Video Lesson " + get_random_string(),
    "VIDEO_ID": "ahCwqrYpIuM",
    "TRANSCRIPT_VTT": "english.vtt",
}

NEW_TEXT_LESSON = {
    "TITLE": "Text Lesson " + get_random_string(),
    "BODY": "Sample text description/notes of the lesson!!",
}

NEW_PDF_LESSON = {
    "TITLE": "PDF Lesson " + get_random_string(),
    "URL": '<gcb-iframe src="https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf" title="Testing pdf" height="400" width="650" instanceid="vA2QBQbXeKO8"></gcb-iframe>',
}

LINK = {
    "TITLE": "Link " + get_random_string(),
    "DESCRIPTION": "Link description " + get_random_string(),
    "URL": "https://www.google.com",
}

MCQ = {
    "QUESTION": "Testing of Multiple Choice Question(MCQ)",
    "CHOICE1": "Choice1",
    "CHOICE2": "Choice2",
    "CHOICE3": "Choice3",
    "CHOICE4": "Choice4",
    "CORRECT_CHOICE": 3,
    "DESCRIPTION": "Test Question : " + get_random_string(),
}

SAQ = {
    "QUESTION": "Testing of Short Answer Question",
    "HINT": "Hint for Short Answer Question",
    "ANSWER": "Answer for Short Answer Question",
    "DESCRIPTION": "Test Short Answer Question : " + get_random_string(),
}

GIFT_QUESTION = {
    "GROUP_DESCRIPTION": "GIFT Group Description " + get_random_string(),
    "QUESTIONS": [
        "::Pointer memory size-"
        + get_random_string()
        + "::What is the memory size double pointer in C {=16 Bits ~8 Bits ~32 Bits ~64 Bits},"
        + "Two plus two equals-"
        + get_random_string()
        + "{=4 =four =Four =FOUR}",
    ],
}


DOWNLOAD_QUESTIONS = {"DESCRIPTION": "Two plus two equals"}

UPLOAD_JSON_FILE = "/src/mcq_json.json"

QUESTION_GROUPS = {
    "DESCRIPTION": "Testing Group : " + get_random_string(),
    "INTRODUCTION": "Sample Introduction",
    "RANDOMIZE": True,
    "RANDOM_QUESTIONS": 3,
    "WEIGHT": 1,
}

BULK_UPLOAD_QUESTION_GROUP = {
    "DESCRIPTION": "Testing Bulk Question Group",
    "QUESTION_DESCRIPTIONS": "This is sample question,1\nTwo plus two equals,1",
}

LABELS = {
    "LABEL_NAME": "Test Label" + get_random_string(),
    "LABEL_DESCRIPTION": "Test Label Description" + get_random_string(),
}
TRACKS = {
    "TRACK_TITLE": "Track Title" + get_random_string(),
    "TRACK_DESCRIPTION": "Track Description" + get_random_string(),
}

SINGLE_ASSESSMENT = {
    "TITLE": "Single submission Assessment",
    "POINTS": 5,
    "CONTENT": "Content of Single submission Assessment",
    "DUE_DATE": due_date.strftime("%m/%d/%Y"),
    "AVAILABILITY": 1,  # 0-Private, 1-Course, 2-Public
}

MULTIPLE_ASSESSMENT = {
    "TITLE": "Multiple submission Assessment",
    "POINTS": 5,
    "CONTENT": "Content of Multiple submission Assessment",
    "DUE_DATE": due_date.strftime("%m/%d/%Y"),
    "AVAILABILITY": 1,  # 0-Private, 1-Course, 2-Public
}

SUBJECTIVE_ASSIGNMENT = {
    "POINTS": 2,
    "PROBLEM": "Subjective Problem Statement",
    "DUE_DATE": due_date.strftime("%m/%d/%Y"),
    "STUD_DUE_DATE": std_due_date.strftime("%m/%d/%Y"),
    "STAFF_DUE_DATE": staff_due_date.strftime("%m/%d/%Y"),
    "RUBRICS": "criteria,weight,Poor(1),Mid(2),Good(3)\n"
    + "Well commented code,20,Has no comments,Has only inline comments,has docstrings as well as inline comments\n"
    + "Does not use GOTO,40,Used,,Not used\n"
    + "Lines of code,40,>21,11-20,<=10",
}


PRIVATE_EVAL_SCRIPT_SQL = '''
import json
import os
import sys
import base64
import zipfile
folder_name = './sql'

def b64tozip_student_code():
    os.system(f"base64 --decode {sys.argv[1]} > tmp.zip")
    os.system(f"mkdir {folder_name}")
    os.system(f"unzip tmp.zip -d {folder_name} > out.txt")
    #ss = os.listdir(folder_name)
    #os.popen(f"cp {ss[0]} tmp.sql").read()
    str1 = ""
    with open("./sql/test.txt","r") as f:
        str1 = f.read()
    with open("tmp.sql","w") as k:
        k.write(str1)
    

# --- code evaluation starts here ---

import os
import json
import sys

DEBUG = False

def print_if_debug(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)
# ***************Answer Dictionary *****************************
answer_dict = {
"Q001flisdb":"SELECT city FROM teams WHERE playground = 'City Park'",
"Q002flisdb":"SELECT name FROM teams WHERE jersey_home_color = 'Yellow'",
"Q003flisdb":"SELECT team_id FROM teams WHERE jersey_home_color = 'Pink'",
"Q004flisdb":"SELECT name FROM teams WHERE  city = 'London'",
"Q005flisdb":"SELECT city FROM teams WHERE  jersey_home_color = 'Red'",
"Q006university":"SELECT title FROM course WHERE dept_name = 'Statistics'",
"Q007university":"SELECT building FROM department WHERE dept_name = 'Biology'",
"Q008university":"SELECT name, salary FROM instructor WHERE dept_name = 'Languages'",
"Q009university":"SELECT room_number, building FROM classroom WHERE capacity > 50",
"Q010university":"SELECT dept_name FROM course WHERE title = 'Latin'"}


#******************Find the random question number ****************
# get text from the question.txt
with open('question.txt', 'r') as f:
    question = f.read().strip()
# split the question variable and store in a list
question_element_list = list(question.split(':'))


# *************** change the database name here *******************

database_name = question_element_list[0][4:] 
database_name = database_name + 'pvt'


# *************************************************************

# ****************** change the answer query here ****************

answer_query = answer_dict[question_element_list[0]]
#f"select student_fname, student_lname from students where dob between '05/01/2003' and '05/30/2003' union select student_fname, student_lname from students where dob between '05/01/2002' and '05/30/2002'"



#******************************************************************



db_backup_tar = f"/db_backups/{database_name}.tar"



def inside_pg_virtualenv():
    """This function runs inside the virtualenv"""
    print_if_debug("INSIDE_PG_VIRTUALENV")
    user = os.environ.get('PGUSER')
    os.system(f"pg_ctl start -l logfile")

    def setup():
        """Loads initial data into the database"""
       
        sql1 = f"""
        create database {database_name};
        create role postgres with user {user};
        """

        # Create temporary file sql1
        with open("setup.sql", "w") as f:
            f.write(sql1)

        # Run the sql query
        os.system("psql -f setup.sql")

        # Run the restore
        commd1 = f"pg_restore -d {database_name} /db_backups/{database_name}.tar"
        os.system(commd1)
        os.system(f"pg_ctl start -l logfile")

    def run_student_sql_file():
        """Runs the student supplied sql file against the current database"""
        commd2 = f"psql -d {database_name} -A -f tmp.sql 2>./err1.txt"
        os.system(commd2)
        if os.stat("./err1.txt").st_size == 0:
            evaluate()
        else:
            # extract the error message from err1 file
            with open('err1.txt', 'r') as e:
                  err_msg = e.read().strip()
            score = 0
            message = err_msg #"Error"
            with open("output.json", "w") as f:
                f.write(json.dumps({
                    "score": score,
                    "message": message,
                }))
                 
    def evaluate():
        """Checks whether the student supplied sql file did what it was
        supposed to or not"""
       
        w_sol = open("solutionqueryfile.sql", "w")
        w_sol.write(answer_query)
        w_sol.close()
        
        # following lines will be omitted later
        #w_stu = open("studentqueryfile.sql", "w")
        #w_stu.write("select 123")
        #w_stu.close()
        #-------------------------------------------

        r_student = open("tmp.sql", "r")
        studentquery = r_student.read()
        r_solution = open("solutionqueryfile.sql", "r")
        solutionquery = r_solution.read()
        r_student.close()
        r_solution.close()
        evalquery ="( " + " ( "+studentquery + " ) " + " except " + " ( " + solutionquery + " ) " + " ) " + " union " + " ( " +" ( " + solutionquery + " ) " + " except " + "(" + studentquery + " ) " + " )"

        with open("evalqueryfile.sql", "w") as w_eval:
            w_eval.write(evalquery)
        w_eval.close() 
        commd3 = f"psql -d {database_name} -A -f evalqueryfile.sql 2>./err2.txt"
        os.system(commd3)
        if os.stat("./err2.txt").st_size != 0:
            score = 0
            message = "Wrong attribute set / Not a select statement"
        else:
            command = f"""
            psql -d {database_name} -A -F , -X -t -f evalqueryfile.sql 
            """
            output = os.popen(command).read()
            message = "Incorrect select query"
            score = 0
            if output.strip() == '': 
                score = 100
                message = "Correct select query"
        
        with open("output.json", "w") as f:
            f.write(json.dumps({
                "score": score,
                "message": message,
              }))
            


    print_if_debug(f"PORT: {os.getenv('PGPORT')}, PASSWORD: {os.getenv('PGPASSWORD')}")
    print("Setting up..")
    setup()
   
    print("Running student submitted sql")
    run_student_sql_file()
    print("END_OF_INSIDE_VIRTUALENV")

def outside_virtualenv():
    """This function runs outside the virtualenv"""
    # Unzip the files and run the same file inside the virtualenv
    b64tozip_student_code()
    print_if_debug("OUTSIDE_PG_VIRTUALENV")
    
    score = 0
    message = ""
    pg_virtualenv_output = ""

    try:
        pg_virtualenv_output = os.popen(
            f"pg_virtualenv -t python3 {os.path.abspath(__file__)}"
        ).read().strip()
        if "END_OF_INSIDE_VIRTUALENV" not in pg_virtualenv_output:
            message = '1An unknown error occured'
        else:
            output_json = json.loads(open('output.json').read())
            if ('score' not in output_json.keys() and 'message' not in
                    output_json.keys()):
                message = '2An unknown error occured'
            score = output_json['score']
            message = output_json['message']
    except Exception as e:
        message = 'Error: ' + str(e)
    finally:
        print(json.dumps({
            "score": score,
            "message": pg_virtualenv_output + "\n" + message
        }))

if __name__ == "__main__":
   
    # Check if this is running inside a pg virtualenv
    if os.environ.get("PGHOST") and os.environ.get("PGPORT"):
        
        inside_pg_virtualenv()
    else:
        outside_virtualenv()
'''

PUBLIC_EVAL_SCRIPT_SQL = '''
import json
import os
import sys
import base64
import zipfile
import codecs

folder_name = './sql'

def b64tozip_student_code():
    os.system(f"base64 --decode {sys.argv[1]} > tmp.zip")
    os.system(f"mkdir {folder_name}")
    os.system(f"unzip tmp.zip -d {folder_name} > out.txt")
    #ss = os.listdir(folder_name)
    #os.popen(f"cp {ss[0]} tmp.sql").read()
    str1 = ""
    with open("./sql/test.txt","r") as f:
        str1 = f.read()
    with open("tmp.sql","w") as k:
        k.write(str1)

    
    #print(ss)
    #f = codecs.open(sys.argv[1], "r", "utf-8")
    #str1 = f.read()
    #with open(sys.argv[1], 'r') as file1:
        #print(file1.read())
    #print(sys.argv[1])
    
   
          

# --- code evaluation starts here ---



DEBUG = False

def print_if_debug(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)




# # ***************Answer Dictionary *****************************
answer_dict = {
"Q001flisdb":"SELECT city FROM teams WHERE playground = 'City Park'",
"Q002flisdb":"SELECT name FROM teams WHERE jersey_home_color = 'Yellow'",
"Q003flisdb":"SELECT team_id FROM teams WHERE jersey_home_color = 'Pink'",
"Q004flisdb":"SELECT name FROM teams WHERE  city = 'London'",
"Q005flisdb":"SELECT city FROM teams WHERE  jersey_home_color = 'Red'",
"Q006university":"SELECT title FROM course WHERE dept_name = 'Statistics'",
"Q007university":"SELECT building FROM department WHERE dept_name = 'Biology'",
"Q008university":"SELECT name, salary FROM instructor WHERE dept_name = 'Languages'",
"Q009university":"SELECT room_number, building FROM classroom WHERE capacity > 50",
"Q010university":"SELECT dept_name FROM course WHERE title = 'Latin'"}

#******************Find the random question number ****************
# get text from the question.txt
with open('question.txt', 'r') as f:
    question = f.read().strip()
# split the question variable and store in a list
question_element_list = list(question.split(':'))


# *************** change the database name here *******************

database_name = question_element_list[0][4:] 



# *************************************************************
# ****************** change the answer query here ****************
answer_query = answer_dict[question_element_list[0]]






#******************************************************************



db_backup_tar = f"/db_backups/{database_name}.tar"



def inside_pg_virtualenv():
    """This function runs inside the virtualenv"""
    print_if_debug("INSIDE_PG_VIRTUALENV")
    user = 'postgres'
#os.environ.get('PGUSER')
    os.system(f"pg_ctl start -l logfile")

    def setup():
        """Loads initial data into the database"""
       
        sql1 = f"""
        create database {database_name};
        create role postgres with user {user};
        """
   

        # Create temporary file sql1
        with open("setup.sql", "w") as f:
            f.write(sql1)

        # Run the sql query
        os.system("psql -f setup.sql")

        # Run the restore
        commd1 = f"pg_restore -d {database_name} /db_backups/{database_name}.tar"
        os.system(commd1)
        os.system(f"pg_ctl start -l logfile")

    def run_student_sql_file():
        try: 
            """Runs the student supplied sql file against the current database"""
            commd2 = f"psql -d {database_name} -A -f tmp.sql 2>./err1.txt"
            os.system(commd2)
            if os.stat("./err1.txt").st_size == 0:
                evaluate()
            else:
                # extract the error message from err1 file
                with open('err1.txt', 'r') as e:
                      err_msg = e.read().strip()
                score = 0
                message = err_msg #"Error"
                with open("output.json", "w") as f:
                    f.write(json.dumps({
                        "score": score,
                        "message": message,
                    }))
        except Exception as e:
            message = 'Error2'  
                 
                 
    def evaluate():
        """Checks whether the student supplied sql file did what it was
        supposed to or not"""
       
        w_sol = open("solutionqueryfile.sql", "w")
        w_sol.write(answer_query)
        w_sol.close()
        
        # following lines will be omitted later
        #w_stu = open("studentqueryfile.sql", "w")
        #w_stu.write("select 123")
        #w_stu.close()
        #-------------------------------------------

        r_student = open("tmp.sql", "r")
        studentquery = r_student.read()
        r_solution = open("solutionqueryfile.sql", "r")
        solutionquery = r_solution.read()
        r_student.close()
        r_solution.close()
        evalquery ="( " + " ( "+studentquery + " ) " + " except " + " ( " + solutionquery + " ) " + " ) " + " union " + " ( " +" ( " + solutionquery + " ) " + " except " + "(" + studentquery + " ) " + " )"

        with open("evalqueryfile.sql", "w") as w_eval:
            w_eval.write(evalquery)
        w_eval.close() 
        commd3 = f"psql -d {database_name} -A -f evalqueryfile.sql 2>./err2.txt"
        os.system(commd3)
        if os.stat("./err2.txt").st_size != 0:
            score = 0
            message = "Wrong attribute set / Not a select statement"
        else:
            command = f"""
            psql -d {database_name} -A -F , -X -t -f evalqueryfile.sql 
            """
            output = os.popen(command).read()
            message = "Incorrect select query"
            score = 0
            if output.strip() == '': 
                score = 75
                message = "Correct select query"
        
        with open("output.json", "w") as f:
            f.write(json.dumps({
                "score": score,
                "message": message,
              }))
            


    print_if_debug(f"PORT: {os.getenv('PGPORT')}, PASSWORD: {os.getenv('PGPASSWORD')}")
    print("Setting up..")
    setup()
   
    print("Running student submitted sql")
    run_student_sql_file()
    print("END_OF_INSIDE_VIRTUALENV")

def outside_virtualenv():
    """This function runs outside the virtualenv"""
    # Unzip the files and run the same file inside the virtualenv
    b64tozip_student_code()
    print_if_debug("OUTSIDE_PG_VIRTUALENV")
    
    score = 0
    message = ""
    pg_virtualenv_output = ""

    try:
        pg_virtualenv_output = os.popen(
            f"pg_virtualenv -t python3 {os.path.abspath(__file__)}"
        ).read().strip()
        if "END_OF_INSIDE_VIRTUALENV" not in pg_virtualenv_output:
            message = '1An unknown error occured'
        else:
            output_json = json.loads(open('output.json').read())
            if ('score' not in output_json.keys() and 'message' not in
                    output_json.keys()):
                message = '2An unknown error occured'
            score = output_json['score']
            message = output_json['message']
    except Exception as e:
        message = 'Error: ' + str(e)
    finally:
        print(json.dumps({
            "score": score,
            "message": pg_virtualenv_output + "\n" + message
        }))

if __name__ == "__main__":
   
    # Check if this is running inside a pg virtualenv
    if os.environ.get("PGHOST") and os.environ.get("PGPORT"):
        
        inside_pg_virtualenv()
    else:
        outside_virtualenv()
'''

RANDOMIZATION_SCRIPT_SQL = """
#import important libraries
import random


problem_statement = {'flisdb':
'''flisdb:
 <img src = 'https://2022-03-07-22-28-19-dot-seek-ode-prod.el.r.appspot.com/testcourse_1/assets/img/flisdbw.PNG',  width = '800'>

''', 

'lisdb':
'''lisdb: <img src = 'https://pa-randomization-script-2021-10-03-dot-iitmpod-dev.el.r.appspot.com/rishavtest/assets/img/lisdbc.PNG', width = '800'> 

''',

'university':
'''university: <img src = 'https://2022-03-07-22-28-19-dot-seek-ode-prod.el.r.appspot.com/testcourse_1/assets/img/university%20schema.PNG', width = '800'> 

''',
}

# question dictionary
question_dict = {
1: "Q001flisdb:Write an SQL query to find the name of the city where the 'City Park' playground is located. [Database: FLIS]", 
2: "Q002flisdb:Write an SQL query to find the name of the teams whose home jersey color is 'Yellow'. [Database: FLIS]",
3: "Q003flisdb:Write an SQL query to find the ID of the teams whose home jersey color is 'Pink'. [Database: FLIS]",
4: "Q004flisdb:Write an SQL query to find the names of the teams from 'London' city. [Database: FLIS]",
5: "Q005flisdb:Write an SQL query to find the name of the city of teams whose home jersey color is 'Red'. [Database: FLIS]",
6: "Q006university:Write an SQL query to find the title of the courses that belongs to the 'Statistics' department. [Database: University]",
7: "Q007university:Write an SQL query to find the building that belongs to the 'Biology' department. [Database: University]",
8: "Q008university:Write an SQL query to find the names and salaries of those instructors who belong to the 'Languages' department. [Database: University]",
9: "Q009university:Write an SQL query to find the room number and building name of the classroom that has a capacity of more than 50 students. [Database: University]",
10: "Q010university:Write an SQL query to find the name of the department where 'Latin' is the course title. [Database: University]"}

  
# printing random question statement
question_num = question_dict[random.randint(1, 10)]

question_element_list = list(question_num.split(':'))


# *************** change the database name here *******************

database_name = question_element_list[0][4:] 
print(question_num + '\n' + problem_statement[database_name])
"""

PUBLIC_EVAL_SCRIPT_HTML = """
# This is an evaluation script to be used in the NPTEL Seek framework with the
zip programming language selected in the frontend.

# The b64tozip_student_code function will unzip the uploaded zip file into the
`folder_name` folder - which defaults to the current folder

import logging
import time
import datetime
import subprocess
import io
import unittest
import json
import os
import sys
import base64
import subprocess

folder_name = '.'
global_python_path = os.getenv('SEEK_PA_GLOBAL_PYTHON_PATH',
                               '/usr/bin/python3')
custom_venv_path = os.getenv('SEEK_PA_CUSTOM_VENV_PATH', '')

def use_custom_venv():
    # Initializes a custom virtualenv using the `custom_venv_path` variable

    # Must be the same python version as `global_python_path`
    
    if not custom_venv_path:
        return True

    script_path = os.path.join(
        custom_venv_path,
        'bin/activate_this.py')
    if not os.path.isfile(script_path):
        print(f"activate_this not found {script_path}")
        print("Could not activate custom virtualenv")
        return False

    try:
        exec(open(script_path).read(), { '__file__': script_path })
    except Exception as e:
        logging.exception(e)
        print("Could not activate custom virtualenv - exec error")
        return False

    return True


def b64tozip_student_code():
    os.popen(f"base64 --decode {sys.argv[1]} > tmp.zip").read()
    os.popen(f"mkdir {folder_name}").read()
    os.popen(f"unzip tmp.zip -d {folder_name}").read()

# If you want to use a custom virtualenv, modify the global custom_venv_path
# variable and uncomment the following lines
custom_venv_path = '/virtualenvs/venv_AppDev'
use_custom_venv()

# If you want to change the global python interpreter, modify the
# global_python_path variable
# global_python_path = '/usr/bin/python3'

# If you want to decode the base64 data and unzip the zip file, uncomment the
# following line
try:
    b64tozip_student_code()
except:
    pass

# Your code starts here. Please make sure your code does not output anything to
# stdout, other than printing out the response JSON as shown below.
# print(json.dumps({
#     'score': 100,
#     'message': "Template",
# }))


import re
from bs4 import BeautifulSoup
import json
import sys

#folder_name = 'student_submission'

#def b64tozip_student_code(b64filename,zipfilename):
#    with open(b64filename,"r") as infile:
#        b64data = infile.read()
#        decoded = base64.b64decode(b64data)
#        with open(zipfilename,"wb") as outfile:
#            outfile.write(decoded)
#            outfile.close()
#b64tozip_student_code(sys.argv[1],"tmp.zip")

#with zipfile.ZipFile(sys.argv[1], 'r') as zip_ref:
#    zip_ref.extractall('.')



 

# ********** EVALUATION STARTS HERE **********

score = 0
message = "Evaluation completed"

# Test case to check if the index.html file exists
if os.path.isfile("index.html") :
    score += 1
else :
    message = "\nSubmission doesn't contain all the expected files"

#Test case to check if the academics.html file exists
if os.path.isfile("academics.html") :
    score += 1
else :
    message = "\nSubmission doesn't contain all the expected files"

#Test case to check if the personal.html file exists
if os.path.isfile("personal.html") :
    score += 1
else :
    message = "\nSubmission doesn't contain all the expected files"

#Test case to check if the contact.html file exists
if os.path.isfile("contact.html") :
    score += 1
else :
    message = "\nSubmission doesn't contain all the expected files"

#Test case to check if the resume.html file exists
if os.path.isfile("resume.html") :
    score += 1
else :
    message = "\nSubmission doesn't contain all the expected files"

f = 0

try :
    #Test case to check if there are 3 divs in index.html
    if os.path.isfile("index.html") :
        with open("index.html") as fp:
            soap = BeautifulSoup(fp,"html.parser")
        dvs = soap.find_all("div")
        if len(dvs) == 3 :
            score += 1
        else :
            f = 1
except :
    f = 1
    pass

try :
    #Test case to check if there are 3 divs in academics.html
    if os.path.isfile("academics.html") :
        with open("academics.html") as fp:
            soap = BeautifulSoup(fp,"html.parser")
        dvs = soap.find_all("div")
        if len(dvs) == 3 :
            score += 1
        else :
            f = 1
except :
    f = 1
    pass

try :
    #Test case to check if there are 3 divs in personal.html
    if os.path.isfile("personal.html") :
        with open("personal.html") as fp:
            soap = BeautifulSoup(fp,"html.parser")
        dvs = soap.find_all("div")
        if len(dvs) == 3 :
            score += 1
        else :
            f = 1
except :
    f = 1
    pass

try :
    #Test case to check if there are 3 divs in contact.html
    if os.path.isfile("contact.html") :
        with open("contact.html") as fp:
            soap = BeautifulSoup(fp,"html.parser")
        dvs = soap.find_all("div")
        if len(dvs) == 3 :
            score += 1
        else :
            f = 1
except :
    f = 1
    pass

try :
    #Test case to check if there are 3 divs in resume.html
    if os.path.isfile("resume.html") :
        with open("resume.html") as fp:
            soap = BeautifulSoup(fp,"html.parser")
        dvs = soap.find_all("div")
        if len(dvs) == 3 :
            score += 1
        else :
            f = 1
except :
    f = 1
    pass

if f == 1 :
    message += "\nSome test cases failed"
    f = 0


try :
    #Test case to check if there are unclosed tags in academics.html
    if os.path.isfile("academics.html") :
        with open("academics.html") as fp:
            c = fp.read()
      
        text = c
        text = re.sub("(<!--.*?-->)", "", text, flags=re.DOTALL)
        tag_stack = []
        r = []
        tag_regex = re.compile('<[^>]*>')
        tags = tag_regex.finditer(text)  

        def finds(tag) :
            if re.match('</[^>]*>', tag.group()):
                a = tag.group().replace("/","").replace(" ","")
                top_tag = tag_stack[-1]

                # if re.match(top_tag.group(), a):
                if a[:-1] in top_tag.group().replace(" ","") :
                    tag_stack.pop()
                else:
                    unclosed = tag_stack.pop()
                    if "<br" in unclosed.group() or "<img" in unclosed.group() or "<meta" in unclosed.group() or "<link" in unclosed.group() :
                        pass
                    else :
                        r.append(unclosed.group())
                    finds(tag)
            else:
                tag_stack.append(tag)  

        for tag in tags:
            finds(tag)

        if len(r) >= 4 :
            score -= 3
            f = 1
        elif len(r) >= 2 :
            score -= 2
            f = 1
        elif len(r) > 0 :
            score -= 1
            f = 1
except :
    pass


try :
    #Test case to check if there are unclosed tags in personal.html
    if os.path.isfile("personal.html") :
        with open("personal.html") as fp:
            c = fp.read()
      
        text = c
        text = re.sub("(<!--.*?-->)", "", text, flags=re.DOTALL)
        tag_stack = []
        r = []
        tag_regex = re.compile('<[^>]*>')
        tags = tag_regex.finditer(text)  

        def finds(tag) :
            if re.match('</[^>]*>', tag.group()):
                a = tag.group().replace("/","").replace(" ","")
                top_tag = tag_stack[-1]

                # if re.match(top_tag.group(), a):
                if a[:-1] in top_tag.group().replace(" ","") :
                    tag_stack.pop()
                else:
                    unclosed = tag_stack.pop()
                    if "<br" in unclosed.group() or "<img" in unclosed.group() or "<meta" in unclosed.group() or "<link" in unclosed.group() :
                        pass
                    else :
                        r.append(unclosed.group())
                    finds(tag)
            else:
                tag_stack.append(tag)  

        for tag in tags:
            finds(tag)

        if len(r) >= 4 :
            score -= 3
            f = 1
        elif len(r) >= 2 :
            score -= 2
            f = 1
        elif len(r) > 0 :
            score -= 1
            f = 1
except :
    pass


try : 
    #Test case to check if there are unclosed tags in contact.html
    if os.path.isfile("contact.html") :
        with open("contact.html") as fp:
            c = fp.read()
      
        text = c
        text = re.sub("(<!--.*?-->)", "", text, flags=re.DOTALL)
        tag_stack = []
        r = []
        tag_regex = re.compile('<[^>]*>')
        tags = tag_regex.finditer(text)  

        def finds(tag) :
            if re.match('</[^>]*>', tag.group()):
                a = tag.group().replace("/","").replace(" ","")
                top_tag = tag_stack[-1]

                # if re.match(top_tag.group(), a):
                if a[:-1] in top_tag.group().replace(" ","") :
                    tag_stack.pop()
                else:
                    unclosed = tag_stack.pop()
                    if "<br" in unclosed.group() or "<img" in unclosed.group() or "<meta" in unclosed.group() or "<link" in unclosed.group() :
                        pass
                    else :
                        r.append(unclosed.group())
                    finds(tag)
            else:
                tag_stack.append(tag)  

        for tag in tags:
            finds(tag)

        if len(r) >= 4 :
            score -= 3
            f = 1
        elif len(r) >= 2 :
            score -= 2
            f = 1
        elif len(r) > 0 :
            score -= 1
            f = 1
except :
    pass


try :
    #Test case to check if there are unclosed tags in resume.html
    if os.path.isfile("resume.html") :
        with open("resume.html") as fp:
            c = fp.read()
      
        text = c
        text = re.sub("(<!--.*?-->)", "", text, flags=re.DOTALL)
        tag_stack = []
        r = []
        tag_regex = re.compile('<[^>]*>')
        tags = tag_regex.finditer(text)  

        def finds(tag) :
            if re.match('</[^>]*>', tag.group()):
                a = tag.group().replace("/","").replace(" ","")
                top_tag = tag_stack[-1]

                # if re.match(top_tag.group(), a):
                if a[:-1] in top_tag.group().replace(" ","") :
                    tag_stack.pop()
                else:
                    unclosed = tag_stack.pop()
                    if "<br" in unclosed.group() or "<img" in unclosed.group() or "<meta" in unclosed.group() or "<link" in unclosed.group() :
                        pass
                    else :
                        r.append(unclosed.group())
                    finds(tag)
            else:
                tag_stack.append(tag)  

        for tag in tags:
            finds(tag)

        if len(r) >= 4 :
            score -= 3
            f = 1
        elif len(r) >= 2 :
            score -= 2
            f = 1
        elif len(r) > 0 :
            score -= 1
            f = 1
except :
    pass

if f == 1 :
    message += "\nBad code"
          
output_json = { "score": round(score / 10 * 100, 2), "message": message }
print(json.dumps(output_json))
"""

PRIVATE_EVAL_SCRIPT_HTML = """
#This is an evaluation script to be used in the NPTEL Seek framework with the
zip programming language selected in the frontend.

#The b64tozip_student_code function will unzip the uploaded zip file into the
`folder_name` folder - which defaults to the current folder

import logging
import time
import datetime
import subprocess
import io
import unittest
import json
import os
import sys
import base64
import subprocess

folder_name = '.'
global_python_path = os.getenv('SEEK_PA_GLOBAL_PYTHON_PATH',
                               '/usr/bin/python3')
custom_venv_path = os.getenv('SEEK_PA_CUSTOM_VENV_PATH', '')

def use_custom_venv():
    #Initializes a custom virtualenv using the `custom_venv_path` variable

    #Must be the same python version as `global_python_path`
    
    if not custom_venv_path:
        return True

    script_path = os.path.join(
        custom_venv_path,
        'bin/activate_this.py')
    if not os.path.isfile(script_path):
        print(f"activate_this not found {script_path}")
        print("Could not activate custom virtualenv")
        return False

    try:
        exec(open(script_path).read(), { '__file__': script_path })
    except Exception as e:
        logging.exception(e)
        print("Could not activate custom virtualenv - exec error")
        return False

    return True


def b64tozip_student_code():
    os.popen(f"base64 --decode {sys.argv[1]} > tmp.zip").read()
    os.popen(f"mkdir {folder_name}").read()
    os.popen(f"unzip tmp.zip -d {folder_name}").read()

# If you want to use a custom virtualenv, modify the global custom_venv_path
# variable and uncomment the following lines
custom_venv_path = '/virtualenvs/venv_AppDev'
use_custom_venv()

# If you want to change the global python interpreter, modify the
# global_python_path variable
# global_python_path = '/usr/bin/python3'

# If you want to decode the base64 data and unzip the zip file, uncomment the
# following line
try:
    b64tozip_student_code()
except:
    pass

# Your code starts here. Please make sure your code does not output anything to
# stdout, other than printing out the response JSON as shown below.
# print(json.dumps({
#     'score': 100,
#     'message': "Template",
# }))


import re
from bs4 import BeautifulSoup
import json
import sys
import zipfile

#folder_name = 'student_submission'

#def b64tozip_student_code(b64filename,zipfilename):
#    with open(b64filename,"r") as infile:
#        b64data = infile.read()
#        decoded = base64.b64decode(b64data)
#        with open(zipfilename,"wb") as outfile:
#            outfile.write(decoded)
#            outfile.close()
#b64tozip_student_code(sys.argv[1],"tmp.zip")

#with zipfile.ZipFile(sys.argv[1], 'r') as zip_ref:
#    zip_ref.extractall('.')



 

# ********** EVALUATION STARTS HERE **********

score = 0
message = "Evaluation completed. All test cases passed"

# Test case to check if the index.html file exists
if os.path.isfile("index.html") :
    score += 1

#Test case to check if the academics.html file exists
if os.path.isfile("academics.html") :
    score += 1

#Test case to check if the personal.html file exists
if os.path.isfile("personal.html") :
    score += 1

#Test case to check if the contact.html file exists
if os.path.isfile("contact.html") :
    score += 1

#Test case to check if the resume.html file exists
if os.path.isfile("resume.html") :
    score += 1

anchors = {'home' : 'index.html',
               'academics' : 'academics.html',
               'personal' : 'personal.html',
               'contact' : 'contact.html',
               'resume' : 'resume.html'} 

try :
    #Test case to check if there are 3 divs in index.html
    if os.path.isfile("index.html") :
        with open("index.html") as fp:
            soap = BeautifulSoup(fp,"html.parser")
        dvs = soap.find_all("div")
        if len(dvs) == 3 :
            score += 1

        #Test case to check if there are 4 anchors in index.html
        ancs = soap.find_all("a")
        if len(ancs) == 4 :
            score += 1

            #Test case to check if all anchor tags are used correctly
            for anc in ancs :
                if anc.text.strip().lower() in anchors and anchors[anc.text.strip().lower()] in anc['href'].lower() :
                    score += 1

except :
    message = "Evaluation completed. Some test cases failed"
    pass

try :
    #Test case to check if there are 3 divs in academics.html
    if os.path.isfile("academics.html") :
        with open("academics.html") as fp:
            soap = BeautifulSoup(fp,"html.parser")
        dvs = soap.find_all("div")
        if len(dvs) == 3 :
            score += 1

        #Test case to check if there are 4 anchors in academics.html
        ancs = soap.find_all("a")
        if len(ancs) == 4 :
            score += 1

            #Test case to check if all anchor tags are used correctly
            r1 = []
            for anc in ancs :
                if anc.text.strip().lower() in anchors and anchors[anc.text.strip().lower()] in anc['href'].lower() :
                    score += 1


        #Test case to check the headers of the table
        ths = soap.find_all("th")
        r = []
        for th in ths :
            if th.text.strip().lower() in ["subject", "marks"] :
                r.append(True)
            else :
                r. append(False)

        if len(ths) == 2 and all(r) == True :
            score += 2

        #Test case to check number of rows in the table
        trs = soap.find_all("tr")
        if len(trs) == 7 :
            score += 4
except :
    message = "Evaluation completed. Some test cases failed"
    pass


try :
    #Test case to check if there are 3 divs in personal.html
    if os.path.isfile("personal.html") :
        with open("personal.html") as fp:
            soap = BeautifulSoup(fp,"html.parser")
        dvs = soap.find_all("div")
        if len(dvs) == 3 :
            score += 1

        #Test case to check if there are 4 anchors in personal.html
        ancs = soap.find_all("a")
        if len(ancs) == 5 :
            score += 1

            #Test case to check if first 4 anchor tags are used correctly
            r1 = []
            for anc in ancs[:-1] :
                if anc.text.strip().lower() in anchors and anchors[anc.text.strip().lower()] in anc['href'] :
                    score += 1

                
            #Test case to check if last anchor tag is correctly used
            if "onlinedegree.iitm.ac.in" in ancs[-1]['href'].strip().lower() :
                score += 1


        #Test case to check if 2 images are used with correct attributes
        r2 = []
        for img in soap.find_all("img") :
            if "250" in img['width'] and "250" in img['height']:
                r2.append(True)
            else :
                r2.append(False)
        if len(r2) == 2 and all(r2) == True :
            score += 2
except :
    message = "Evaluation completed. Some test cases failed"
    pass


try : 
    #Test case to check if there are 3 divs in contact.html
    if os.path.isfile("contact.html") :
        with open("contact.html") as fp:
            soap = BeautifulSoup(fp,"html.parser")
        dvs = soap.find_all("div")
        if len(dvs) == 3 :
            score += 1

        #Test case to check if there are 4 anchors in contact.html
        ancs = soap.find_all("a")
        if len(ancs) == 4 :
            score += 1

            #Test case to check if all anchor tags are used correctly
            r1 = []
            for anc in ancs :
                if anc.text.strip().lower() in anchors and anchors[anc.text.strip().lower()] in anc['href'] :
                    score += 1

        #Test case to check if address tag is used in the HTML file
        if len(soap.find_all("address")) == 1 :
            score += 1
except :
    message = "Evaluation completed. Some test cases failed"
    pass


try:
    #Test case to check if there are 3 divs in resume.html
    if os.path.isfile("resume.html") :
        with open("resume.html") as fp:
            soap = BeautifulSoup(fp,"html.parser")
        dvs = soap.find_all("div")
        if len(dvs) == 3 :
            score += 1

        #Test case to check if there are 4 anchors in resume.html
        ancs = soap.find_all("a")
        if len(ancs) == 5 :
            score += 1

            #Test case to check if first 4 anchor tags are used correctly
            r1 = []
            for anc in ancs[:-1] :
                if anc.text.strip().lower() in anchors and anchors[anc.text.strip().lower()] in anc['href'] :
                    score += 1
                
except :
    message = "Evaluation completed. Some test cases failed"
    pass

try :
    #Test case to check if there are unclosed tags in index.html
    if os.path.isfile("index.html") :
        with open("index.html") as fp:
            c = fp.read()
      
        text = c
        text = re.sub("(<!--.*?-->)", "", text, flags=re.DOTALL)
        tag_stack = []
        r = []
        tag_regex = re.compile('<[^>]*>')
        tags = tag_regex.finditer(text)  

        def finds(tag) :
            if re.match('</[^>]*>', tag.group()):
                a = tag.group().replace("/","").replace(" ","")
                top_tag = tag_stack[-1]

                # if re.match(top_tag.group(), a):
                if a[:-1] in top_tag.group().replace(" ","") :
                    tag_stack.pop()
                else:
                    unclosed = tag_stack.pop()
                    if "<br" in unclosed.group() or "<img" in unclosed.group() or "<meta" in unclosed.group() or "<link" in unclosed.group() :
                        pass
                    else :
                        r.append(unclosed.group())
                    finds(tag)
            else:
                tag_stack.append(tag)  

        for tag in tags:
            finds(tag)

        if len(r) >= 4 :
            score -= 3
        elif len(r) >= 2 :
            score -= 2
        elif len(r) > 0 :
            score -= 1
except :
    message = "Evaluation completed"
    pass

try :
    #Test case to check if there are unclosed tags in academics.html
    if os.path.isfile("academics.html") :
        with open("academics.html") as fp:
            c = fp.read()
      
        text = c
        text = re.sub("(<!--.*?-->)", "", text, flags=re.DOTALL)
        tag_stack = []
        r = []
        tag_regex = re.compile('<[^>]*>')
        tags = tag_regex.finditer(text)  

        def finds(tag) :
            if re.match('</[^>]*>', tag.group()):
                a = tag.group().replace("/","").replace(" ","")
                top_tag = tag_stack[-1]

                # if re.match(top_tag.group(), a):
                if a[:-1] in top_tag.group().replace(" ","") :
                    tag_stack.pop()
                else:
                    unclosed = tag_stack.pop()
                    if "<br" in unclosed.group() or "<img" in unclosed.group() or "<meta" in unclosed.group() or "<link" in unclosed.group() :
                        pass
                    else :
                        r.append(unclosed.group())
                    finds(tag)
            else:
                tag_stack.append(tag)  

        for tag in tags:
            finds(tag)

        if len(r) >= 4 :
            score -= 3
        elif len(r) >= 2 :
            score -= 2
        elif len(r) > 0 :
            score -= 1
except :
    message = "Evaluation completed"
    pass


try :
    #Test case to check if there are unclosed tags in personal.html
    if os.path.isfile("personal.html") :
        with open("personal.html") as fp:
            c = fp.read()
      
        text = c
        text = re.sub("(<!--.*?-->)", "", text, flags=re.DOTALL)
        tag_stack = []
        r = []
        tag_regex = re.compile('<[^>]*>')
        tags = tag_regex.finditer(text)  

        def finds(tag) :
            if re.match('</[^>]*>', tag.group()):
                a = tag.group().replace("/","").replace(" ","")
                top_tag = tag_stack[-1]

                # if re.match(top_tag.group(), a):
                if a[:-1] in top_tag.group().replace(" ","") :
                    tag_stack.pop()
                else:
                    unclosed = tag_stack.pop()
                    if "<br" in unclosed.group() or "<img" in unclosed.group() or "<meta" in unclosed.group() or "<link" in unclosed.group() :
                        pass
                    else :
                        r.append(unclosed.group())
                    finds(tag)
            else:
                tag_stack.append(tag)  

        for tag in tags:
            finds(tag)

        if len(r) >= 4 :
            score -= 3
        elif len(r) >= 2 :
            score -= 2
        elif len(r) > 0 :
            score -= 1
except :
    message = "Evaluation completed"
    pass


try : 
    #Test case to check if there are unclosed tags in contact.html
    if os.path.isfile("contact.html") :
        with open("contact.html") as fp:
            c = fp.read()
      
        text = c
        text = re.sub("(<!--.*?-->)", "", text, flags=re.DOTALL)
        tag_stack = []
        r = []
        tag_regex = re.compile('<[^>]*>')
        tags = tag_regex.finditer(text)  

        def finds(tag) :
            if re.match('</[^>]*>', tag.group()):
                a = tag.group().replace("/","").replace(" ","")
                top_tag = tag_stack[-1]

                # if re.match(top_tag.group(), a):
                if a[:-1] in top_tag.group().replace(" ","") :
                    tag_stack.pop()
                else:
                    unclosed = tag_stack.pop()
                    if "<br" in unclosed.group() or "<img" in unclosed.group() or "<meta" in unclosed.group() or "<link" in unclosed.group() :
                        pass
                    else :
                        r.append(unclosed.group())
                    finds(tag)
            else:
                tag_stack.append(tag)  

        for tag in tags:
            finds(tag)

        if len(r) >= 4 :
            score -= 3
        elif len(r) >= 2 :
            score -= 2
        elif len(r) > 0 :
            score -= 1
except :
    message = "Evaluation completed"
    pass


try :
    #Test case to check if there are unclosed tags in resume.html
    if os.path.isfile("resume.html") :
        with open("resume.html") as fp:
            c = fp.read()
      
        text = c
        text = re.sub("(<!--.*?-->)", "", text, flags=re.DOTALL)
        tag_stack = []
        r = []
        tag_regex = re.compile('<[^>]*>')
        tags = tag_regex.finditer(text)  

        def finds(tag) :
            if re.match('</[^>]*>', tag.group()):
                a = tag.group().replace("/","").replace(" ","")
                top_tag = tag_stack[-1]

                # if re.match(top_tag.group(), a):
                if a[:-1] in top_tag.group().replace(" ","") :
                    tag_stack.pop()
                else:
                    unclosed = tag_stack.pop()
                    if "<br" in unclosed.group() or "<img" in unclosed.group() or "<meta" in unclosed.group() or "<link" in unclosed.group() :
                        pass
                    else :
                        r.append(unclosed.group())
                    finds(tag)
            else:
                tag_stack.append(tag)  

        for tag in tags:
            finds(tag)

        if len(r) >= 4 :
            score -= 3
        elif len(r) >= 2 :
            score -= 2
        elif len(r) > 0 :
            score -= 1
except :
    message = "Evaluation completed"
    pass
          
output_json = { "score": round(score / 45 * 100, 2), "message": message }
print(json.dumps(output_json))
"""


PROGRAMMING_EVAL_SCRIPT_TYPE_SQL = {
    "PROBLEM": "<h1>Instructions to submit the query:</h1>"
    + "<ol><li>In the dropdown with Choose Language, select Zip.</li>"
    + "<li>Write the query in the editor. There should NOT be any semicolon at the end of the query.</li>"
    + "<li>Click on Test Run.</li>"
    + "<li>If it has run correctly, it will give the message: 'Correct select query' at the bottom.</li>"
    + "<li>If not, it will give an error message or incorrect select query.</li>"
    + "<li>Once you are satisfied that your query works correctly, then click on 'Submit'.</li>"
    "</ol>" + "<br><br>" + "<h2>&nbsp;Problem Statement:&nbsp;</h2>",
    "DUE_DATE": due_date.strftime("%m/%d/%Y"),
    "PRIVATE_EVAL_SCRIPT": PRIVATE_EVAL_SCRIPT_SQL,
    "PUBLIC_EVAL_SCRIPT": PUBLIC_EVAL_SCRIPT_SQL,
    "EVAL_SCRIPT_LANG": "/usr/bin/python3",
    "RANDOMIZATION_SCRIPT": RANDOMIZATION_SCRIPT_SQL,
    "RANDOMIZATION_SCRIPT_LANGUAGE": "/usr/bin/python3",
    "ZIP_EDITOR_LANG": 4,
}

PROGRAMMING_EVAL_SCRIPT_TYPE_HTML = {
    "PROBLEM": "This assignment is meant to assess your understanding of HTML. Detailed instructions for the assignments can be found in the link below. <br><br>HTML Assignment:&nbsp;<a href='https://drive.google.com/file/d/1xZK64-z9pY7J19TmlpK9a_NriBLwpUAN/view'>Week2_LA_HTML.pdf - Google Drive</a><br><br><u>Instructions to submit the assignment:<br></u><br><div>Put all the HTML files and other files (images, docs etc. if any) in a folder.<br><br></div><div>Select all the files (HTML and others if any), right-click one of them, and send to &gt; Compressed (zipped) folder.<br>&nbsp;</div><div>Save the files as '&lt;roll_number&gt;.zip'. (E.g.: 21f1000000.zip)<br><br></div><div>In the dropdown with Choose Language, Select Zip.<br><br></div><div>Click on Choose file and select your zip file.<br><br></div><div>Click on Test Run.<br><br></div><div>It will give you the score evaluated against the public test cases (sometimes feedback message will also be provided).<br><br></div><div>Once you are satisfied that your submission is correct, upload the file and click on 'Submit'.<br><br></div><div>Your submission will be evaluated against private test cases and the result will be published once the deadline is over.</div><br>",
    "DUE_DATE": due_date.strftime("%m/%d/%Y"),
    "PRIVATE_EVAL_SCRIPT": PRIVATE_EVAL_SCRIPT_HTML,
    "PUBLIC_EVAL_SCRIPT": PUBLIC_EVAL_SCRIPT_HTML,
    "EVAL_SCRIPT_LANG": "/usr/bin/python3",
    "RANDOMIZATION_SCRIPT": "",
    "RANDOMIZATION_SCRIPT_LANGUAGE": "/usr/bin/python3",
    "ZIP_EDITOR_LANG": 5,
}

PYTHON_CODE = {
    "PROBLEM": "<p>The range of a list of numbers is the difference between the maximum and minimum values in the list.</p>"
    + "<hr><p>Write a function named <span style='color:red; font-family: monospace;'>get_range</span> that accepts a list of real numbers as argument. It should return the range of the list.</p>"
    + "<hr><p><strong>Note</strong></p>"
    + "<p>(1) Avoid using built-in function such as <span style='color:red; font-family: monospace;'>max</span> and <span style='color:red; font-family: monospace;'>min</span>.</p>"
    + "<p>(2) You do not have to accept input from the user or print output to the console. You just have to write the function definition.</p>",
    "PUBLIC_TEST_CASE_INPUTS": [
        "1.0,2.0,3.0,4.0,5.0",
        "1.0,3.7,8.9,5.5,1.9,6.3,0.1,9.9",
    ],
    "PUBLIC_TEST_CASE_OUTPUTS": ["4.0", "9.8"],
    "PRIVATE_TEST_CASE_INPUTS": [
        "43.26,25.07,19.06,48.65,21.08,32.57,2.82",
        "6.1,16.49,28.23,6.03,38.57,29.81,17.57,26.49,46.96,39.48,6.84,33.44,5.06",
    ],
    "PRIVATE_TEST_CASE_OUTPUTS": ["45.83", "41.9"],
    "PREFIXED_CODE": "",
    "TEMPLATE_CODE": "def get_range(L):"
    + """compute the range of a list L
                    Argument:
                    L: list
                    Return:
                    range: float""",
    "SUFFIXED_CODE": "",
    "INVISIBLE_CODE": "if __name__ == '__main__':\n"
    + "L = [float(x) for x in input().split(',')]\n"
    + "max = ''\n"
    + "min = ''\n"
    + "print(get_range(L))\n",
    "SAMPLE_SOLUTION": """ # get the maximum\n
    def get_max(L):
        maxi = L[0]
        for x in L:
            if x > maxi:
                maxi = x
        return maxi

    # get the minimum\n
    def get_min(L):
        mini = L[0]
        for x in L:
            if x < mini:
                mini = x
        return mini

    # get the range
    def get_range(L):
        maxi = get_max(L)
        mini = get_min(L)
        return maxi - mini  """,
    "SAMPLE_SOLUTION_FILE": "get_range.py",
}

C_CODE = {
    "PREFIXED_CODE": "//Create a C function takes parameters and returns sum\n",
    "SUFFIXED_CODE": "\n//Call the function with parameters from main\n",
    "SAMPLE_SOLUTION": 'int sum(int a,int b){\n\treturn a+b;\n}\n\nint main(){\n\tprintf("%d",sum(5,6));\n\treturn 0;\n}\n',
    "SAMPLE_SOLUTION_FILE": "sum.c",
}

CPP_CODE = {
    "PREFIXED_CODE": "//Create a CPP function takes parameters and returns sum\n",
    "SUFFIXED_CODE": "\n//Call the function with parameters from main\n",
    "SAMPLE_SOLUTION": "int sum(int a,int b){\n\treturn a+b;\n}\n\nint main(){\n\tcout<<sum(5,6);\n\treturn 0;\n}\n",
    "SAMPLE_SOLUTION_FILE": "sum.cpp",
}

JAVA_CODE = {
    "PROBLEM": "Given as input two integers <i>n_1,n_2</i> and two double values <i>d_1,d_2</i>&nbsp;complete the Java code to form two complex numbers <i>c_1</i> and <i>c_2</i>, as described below, and print their sum.<br><ul><li>The real parts of <i>c_1</i> and <i>c_2</i> are<i> n_1</i> and <i>d_1</i> respectively, whereas their imaginary parts are<i> n_2 </i>and <i>d_2</i>, respectively.<br></li><li>Define a generic class <span style='font-family: &quot;Courier New&quot;;'><b>ComplexNum</b></span> with the following members.</li><ul><li>Instance variables <i>r</i> and <i>i</i></li><li>A constructor to initialize <i>r</i> and <i>i</i><span style='white-space:pre'>	</span></li><li>A method <span style='font-family: &quot;Courier New&quot;;'><b>add()</b></span>to return the sum of the two instances of generic type <span style='font-family: &quot;Courier New&quot;;'><b>ComplexNum</b></span><br></li><li><span style='font-family: Arial;'>A method that overrides the </span><span style='font-family: &quot;Courier New&quot;;'><b>toString()</b></span><span style='font-family: Arial;'> method in the </span><b style='font-family: &quot;Courier New&quot;;'>Object</b><span style='font-family: Arial;'> class so that the format of the output is in accordance with those in the test cases.</span><br></li></ul></ul>",
    "PUBLIC_TEST_CASE_INPUTS": ["10 20\n13.3 5.12", "6 10\n10.3 15.6"],
    "PUBLIC_TEST_CASE_OUTPUTS": [
        "10.0 + 20.0i + 13.3 + 5.12i = 23.3 + 25.12i",
        "6.0 + 10.0i + 10.3 + 15.6i = 16.3 + 25.6i",
    ],
    "PRIVATE_TEST_CASE_INPUTS": ["10 15\n5.4 1.6"],
    "PRIVATE_TEST_CASE_OUTPUTS": ["10.0 + 15.0i + 5.4 + 1.6i = 15.4 + 16.6i"],
    "PREFIXED_CODE": "import java.util.*;",
    "TEMPLATE_CODE": "//Add your code for ComplexNum here",
    "SUFFIXED_CODE": "class FClass{ public static void main(String[] args) {"
    + "Scanner sc = new Scanner(System.in);"
    + "int n1, n2;"
    + "double d1, d2;"
    + "n1 = sc.nextInt();"
    + "n2 = sc.nextInt();"
    + "d1 = sc.nextDouble();"
    + "d2 = sc.nextDouble();"
    + "ComplexNum<Integer> c1 = new ComplexNum<Integer>(n1, n2);"
    + "ComplexNum<Double> c2 = new ComplexNum<Double>(d1, d2);"
    + "ComplexNum<Double> c3 = c1.add(c2);"
    + "System.out.println(c1 + "
    + " + c2 + "
    + "="
    + " + c3);}}",
    "INVISIBLE_CODE": "",
    "SAMPLE_SOLUTION": "class ComplexNum<T extends Number>{"
    + "private T r, i;"
    + "public ComplexNum(T r, T i) {"
    + "this.r = r;"
    + "this.i = i;}"
    + "public ComplexNum<Double> add(ComplexNum<?> c){"
    + "ComplexNum<Double> dc = new ComplexNum<Double>(0.0, 0.0);"
    + "dc.r = this.r.doubleValue() + c.r.doubleValue();"
    + "dc.i = this.i.doubleValue() + c.i.doubleValue();"
    + "return dc;}"
    + "public String toString() {"
    + "return r.doubleValue() + "
    + " + i.doubleValue() + "
    + "i"
    + ";}}",
    "SAMPLE_SOLUTION_FILE": "FClass.java",
}

BASH_CODE = {
    "PROBLEM": """ We created some directories and change our current working directory using the <code>cd</code> command as given by the sequence of commands below. Write a bash command to make the directory "<code>level2"</code>&nbsp;as your current working directory. i.e. after executing your solution, if we execute the command <code>"pwd"</code> it should return the path of the directory <code>"level2"</code>.<br>Write your solution as a single line bash command.<br><span style="white-space:pre">	</span>
                <pre><code>cd /
                mkdir level1
                cd level1
                mkdir level2
                cd level2
                mkdir level3
                cd ..
                cd ..</code></pre><br> """,
    "PUBLIC_TEST_CASE_INPUTS": ["1"],
    "PUBLIC_TEST_CASE_OUTPUTS": ["/level1/level2"],
    "PRIVATE_TEST_CASE_INPUTS": ["112"],
    "PRIVATE_TEST_CASE_OUTPUTS": ["/level1/level2\nPrivate"],
    "PREFIXED_CODE": "script() { echo '\n",
    "TEMPLATE_CODE": "",
    "SUFFIXED_CODE": "pwd'}",
    "INVISIBLE_CODE": "mkdir -p /level1/level2/level3"
    + "cd /"
    + "script | col > /script.sh"
    + "bash /script.sh 2>&1"
    + "read var"
    + "[[ $var == 112 ]] && echo Private",
    "SAMPLE_SOLUTION": "cd /level1/level2",
    "SAMPLE_SOLUTION_FILE": "sample.sh",
}

JAVA_SCRIPT_CODE = {
    "PROBLEM": "Write the definitions of the functions given below with the help of given information.",
    "PUBLIC_TEST_CASE_INPUTS": [
        "20000\n1\n2020-12-27\n2021-08-27",
        "22000\n2.5\n2020-12-27\n2021-06-27",
        "40000\n2\n30\n2021-09-25",
    ],
    "PUBLIC_TEST_CASE_OUTPUTS": [
        "48600\n204452\n320",
        "100100\n1946639\n1844",
        "-1\n-1\n-1",
    ],
    "PRIVATE_TEST_CASE_INPUTS": [
        "34000\n1.8\n2020-11-22\n2021-03-25",
        "39000\n1.8\n2021-02-11\n2021-03-13",
    ],
    "PRIVATE_TEST_CASE_OUTPUTS": ["75276\n271109\n260", "21060\n27603\n31"],
    "PREFIXED_CODE": """ /*
                    * calculateSimpleInterest calculates and returns the simple interest
                    * (floor value) for a fixed deposit. Formula used is,

                    * calculateSimpleInterest calculates and returns the simple interest
                    * for a fixed deposit. Formula used is,
                    * Simple Interest: P X R X T / 100
                    *   where:
                    *   P = Principal
                    *   I = Daily interest rate
                    *   N = Number of days
                    *
                    *  In case of any input error (wrong date format, alphabets in daily interest etc.), return -1
                    *
                    * @param {number} principal  - Principal amount
                    * @param {number} dailyInterest  - daily interest rate
                    * @param {string} startingDate  - Starting date of the fixed deposit in "YYYY-MM-DD" format, example "2015-03-25"
                    * @param {string} endingDate  - Ending date of the fixed deposit in "YYYY-MM-DD" format, example "2015-03-25"
                    * @return {number} interest
                    */

                    /*
                    * calculateCompoundInterest calculates and returns the compound interest
                    * (floor value) for a fixed deposit. Formula used is,
                    *   Compound Interest=P[(1+I/100)^N - 1]
                    *   where:
                    *   P = Principal
                    *   I = Daily interest rate
                    *   N = Number of days
                    *
                    *  In case of any input error (wrong date format, alphabets in daily interest etc.), return -1
                    *
                    * @param {number} principal  - Principal amount
                    * @param {number} dailyInterest  - daily interest rate
                    * @param {string} startingDate  - Starting date of the fixed deposit in "YYYY-MM-DD" format, example "2015-03-25"
                    * @param {string} endingDate  - Ending date of the fixed deposit in "YYYY-MM-DD" format, example "2015-03-25"
                    * @return {number} interest
                    */

                    /*
                    * extraAmountPercentage calculates and returns the extra amount percentage borrower will have to pay in case of
                    * compound interest (floor value) in comparison to the simple interest for a fixed deposit.

                    *  In case of any input error (wrong date format, alphabets in daily interest etc.), return -1
                    *
                    * @param {number} principal  - Principal amount
                    * @param {number} dailyInterest  - Daily interest rate.
                    * @param {string} startingDate  - Starting date of the fixed deposit in "YYYY-MM-DD" format, example "2015-03-25"
                    * @param {string} endingDate  - Ending date of the fixed deposit in "YYYY-MM-DD" format, example "2015-03-25"
                    * @return {number} percentage
                    */ """,
    "TEMPLATE_CODE": """ function calculateSimpleInterest(
                    principal,
                    dailyInterest,
                    startingDate,
                    endingDate
                    ) {

                    // Add your code here

                    return Math.floor(interest);

                    }

                    function calculateCompoundInterest(
                    principal,
                    dailyInterest,
                    startingDate,
                    endingDate
                    ) {

                    // Add your code here

                    return Math.floor(interest);

                    }

                    function extraAmountPercentage(
                    principal,
                    dailyInterest,
                    startingDate,
                    endingDate
                    ) {

                    // Add your code here

                    return Math.floor(percentage);

                    }
                    """,
    "SUFFIXED_CODE": "",
    "INVISIBLE_CODE": """ var x1;
                        var x2;
                        var x3;
                        var x4;

                        function read_number_inputs(){
                            var fs = require("fs");
                            var stdinBuffer = fs.readFileSync(0); // STDIN_FILENO = 0
                            var lines = stdinBuffer.toString().split(/\r?\n/)
                            x1 = Number(lines[0]);
                            x2 = Number(lines[1]);
                            x3 = lines[2];
                            x4 = lines[3];
                        }
                        read_number_inputs();
                        console.log(calculateSimpleInterest(x1, x2, x3, x4));
                        console.log(calculateCompoundInterest(x1, x2, x3, x4));
                        console.log(extraAmountPercentage(x1, x2, x3, x4)); """,
    "SAMPLE_SOLUTION": """ function calculateSimpleInterest(
                            principal,
                            dailyInterest,
                            startingDate,
                            endingDate
                            ) {

                            s = new Date(startingDate);
                            e = new Date(endingDate);
                            //console.log(s, "\n", e);
                            if (s == "Invalid Date") {return -1;}
                            if (e == "Invalid Date") {return -1;}
                            diff = (e.getTime() - s.getTime()) / (1000 * 60 * 60 * 24);

                            result = Number(principal) * Number(dailyInterest) * Number(diff) / 100;
                            return Math.floor(result);

                            }

                            function calculateCompoundInterest(
                            principal,
                            dailyInterest,
                            startingDate,
                            endingDate
                            ) {
                                
                            s = new Date(startingDate);
                            e = new Date(endingDate);
                            if (s == "Invalid Date") {return -1;}
                            if (e == "Invalid Date") {return -1;}

                            diff = (e.getTime() - s.getTime()) / (1000 * 60 * 60 * 24);

                            result = principal * (Math.pow((1 + dailyInterest / 100), diff) - 1);
                                
                            return Math.floor(result);
                            }

                            function extraAmountPercentage(principal, dailyInterest, startingDate, endingDate) {
                                
                                compound = calculateCompoundInterest(
                            principal,
                            dailyInterest,
                            startingDate,
                            endingDate
                            );
                                simple = calculateSimpleInterest(
                            principal,
                            dailyInterest,
                            startingDate,
                            endingDate
                            );
                            if (compound == -1) {return -1;}
                            if (simple == -1) {return -1;}
                                return Math.floor((compound - simple) / simple * 100);
                            }""",
    "SAMPLE_SOLUTION_FILENAME": "sample1.txt",
}

PROGRAMMING_ASSIGNMENT_TEST_CASES = {
    "WEIGHT": 5,
    "DUE_DATE": due_date.strftime("%m/%d/%Y"),
}


BULK_ENROLLMENT_SINGLE = {
    "ENROLL_INFO": "satyacomp@gmail.com, ns_data_structures\nsatyanarayana@onlinedegree.iitm.ac.in, ns_data_structures"
}

BULK_ENROLLMENT_MULTIPLE = {
    "ENROLL_INFO": "satyacomp@gmail.com, ns_data_structures\n"
    + "satyacomp@gmail.com, ns_test_course\n"
    + "satyanarayana@onlinedegree.iitm.ac.in, ns_data_structures\n"
    + "satyanarayana@onlinedegree.iitm.ac.in, ns_test_course"
}

ENROLL_STUDENT = {
    "MAIL_IDs": "satyacomp@gmail.com\nsatyanarayana@onlinedegree.iitm.ac.in\nsivakoti.satyacomp@gmail.com"
}

STUDENT_PROFILE = {
    "EXISTED_MAIL": "satyacomp@gmail.com",
    "NOT_EXISTED_MAIL": "abc@gmail.com",
}


# All the Testing data below, modify or add as per your requirements

EXAM_INFO = {
    "INFO": [
        "84b596cfb7ed4259b3724d3a2f96e4fe,14,"
        + exam_from
        + ","
        + exam_to
        + "\n"
        + "962a547bc57f4e6999eb1a76492c54aa,17,"
        + exam_from
        + ","
        + exam_to
        + "\n"
        + "08e2afb5d82d4571830d4ae022de45b8,18,"
        + exam_from
        + ","
        + exam_to
    ]
}

CHAT_INFO = {
    "INFO": "84b596cfb7ed4259b3724d3a2f96e4fe,1,FALSE\n"
    + "962a547bc57f4e6999eb1a76492c54aa,1,TRUE\n"
    + "08e2afb5d82d4571830d4ae022de45b8,1,FALSE"
}

LIST_MODULES = {}

STUDENT_INFO = {
    "SEARCHING_MAIL": "student5940@mail.com",
    "STUDENT_MAILS": "san_india@gmail.com, ram_sethu_bombay@gmail.com, xyz@gmail.com",
    "UPDATE_INFO": "08e2afb5d82d4571830d4ae022de45b8,Mike Joe, assets/img/joe.jpg\n84b596cfb7ed4259b3724d3a2f96e4fe,Ravi Kumar,assets/img/kumar.jpg",
    "UNENROLL_MAIL": "abc_student@gmail.com",
    "STUDENT_GROUP_NAME": "Student Group " + str(get_random_number()),
    "GROUP_DESCRIPTION": "Student Group Description",
}


with open(r"dashboard/app_config.yaml") as file:
    config_list = yaml.load(file, Loader=yaml.FullLoader)

BIG_QUERY = {
    "NAMESPACE": "ns_test_namespace",
    "TABLE_NAME": "ns_test_table",
    "NEW_DATA_SET": "ns_test_data_set",
}

SYNC_SCORES = {
    "LEVEL": "FOUNDATION",
    "TERM_CODE": "F1-2023",
    "COURSE_CODE": "MA1001",
    "TEST_CODE": "ASSIGNMENT-1",
    "CALCULATION_TYPE": "SCORED",
    "MAX_MARKS": "100",
}


ANNOUNCEMENTS = {
    "TITLE": "Test Announcement " + get_random_string(),
    "BODY": "Test Announcement Body here",
}

COURSE_CATEGORY = {
    "CATEGORY_NAME": "Test Category " + get_random_string(),
    "CATEGORY_DESCRIPTION": "Test Category Description",
}
