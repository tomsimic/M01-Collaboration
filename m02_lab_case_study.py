"""
Program: m02_lab_case_study.py
Author: Tomi Simic
Last date modified: 2024-03-26
This program is to be used for Assignment 2 in Module 2. The program evaluates
student's full name as only a alphabetical entry, student's GPA as a float,
and outputs student's eligebility for Dean's List and Honor roll.
"""
# pseudo code:
# import needed function(s)
# create a function that stores all prompts
# create sentinel constant
# create function to evaluate correct name entry
# create function to evaluate correct gpa entry
# create function to evaluate student GPA against Dean's List vs Honor Roll
# create main function loop:
#   prompt for student's last name and validate
#   prompt for student's first name and validate
#   prompt for GPA and store it as a float after validation
#   display results

# import re
import re

# Setting constants:
SENTINEL = "ZZZ"
QUIT = False


# Prompts function:
def prompts():
    """Provides prompt for use for user interaction"""
    prompts = {
        'first_name': 'Please enter your FIRST name ',
        'last_name': 'Please enter your LAST name ',
        'not_name': 'A name shouldn\'t have a number or characters. ',
        'not_float': 'You have not entered a number as a float \
(i.E. 3.49). ',
        'gpa': 'Please enter your gpa as a float (i.E. 3.49):> ',
        'gpa_range': "Entry not within acceptable range. Please note that \
acceptable range is between 0.1 and 4.0. ",
        'not_gpa': "The GPA cannot be less than 0.1 or more than 4.0. ",
        'exit': "or enter 'ZZZ' to quit the program.>",
        'quit': "You have chosen to quit the program. Goodbye!",
        'retry': "Please try again.",
        'dean': "\nCongratulations! Student made the Dean's List",
        'honor': "\nCongratulations! Student is a member of Honor Roll",
        'average': "This is an average student."
    }
    return prompts


# User input validation:
def name_validation(name_type):
    """This function checks for Sentinel value and user input"""
    entry = ""
    characters = re.compile('[@_!#$%^&*()<>?/|}{~:0123456789]')
    # Student's name validation:
    while entry == "":
        print('\n')
        entry = input(prompts().get(name_type) + prompts().get("exit"))
        # Checking for Sentinel value
        if entry.upper() == SENTINEL:
            return SENTINEL
        # Checking for numbers and special characters in the name:
        elif entry.isnumeric():
            print(prompts().get("not_name") + prompts().get("retry"))
            entry = ""  # resetting input validation to remain in loop
        elif (characters.search(entry) is None):
            print("You have entered:", entry.title())
        else:
            print(prompts().get("not_name") + prompts().get("retry"))
            entry = ""
    return entry.title()


def gpa():
    """Validating user input to confirm it's a float"""
    gpa = 0.0
    while gpa == 0.0:
        gpa = input(prompts().get('gpa'))
        try:
            if isinstance(float(gpa), float):
                gpa = float(gpa)
                # Validating the value is within range:
                if 0.1 < gpa <= 4.0:
                    pass  # passing since the value is correct & returned later
                else:
                    # Resetting loop if entry is outside range
                    print(prompts().get('gpa_range') + prompts().get("retry"))
                    gpa = 0.0
        except ValueError:
            # Validating a number is entered:
            if gpa.isnumeric() is False:
                print(prompts().get('not_float') + prompts().get("retry"))
                gpa = 0.0
    return float(gpa)


def student_type():
    """Checking student's grade standings"""
    gpa_average = gpa()
    # Checking below honor's roll:
    if gpa_average < 3.25:
        return f"{prompts().get('average')} with a gpa average of {gpa_average}."
    # Checking honor's roll:
    elif gpa_average < 3.5:
        return f"{prompts().get('honor')} with a gpa average of {gpa_average}."
    # Returning dean's list:
    else:
        return f"{prompts().get('dean')} with a gpa average of {gpa_average}."


# Main Function:
if __name__ == "__main__":
    # Running main loop:
    while QUIT is False:
        last_name = name_validation('last_name')
        # Checking for sentinel value to exit when needed:
        if last_name == SENTINEL:
            QUIT = True
        # Executing main loop until sentinel is provided:
        else:
            first_name = name_validation('first_name')
            student_standings = student_type()
            print("Student's first name:    ", first_name)
            print("Student's last name:     ", last_name)
            print("Student's GPA standings: ", student_standings)
    print(prompts().get('quit'))
