# This test program should identify the common mistakes
# that you can make, and suggest how you can fix them.
# There are many other things that can be checked, and
# we advise you to add the test cases yourself.

# HOW TO EXECUTE:

# If you are using python shell:
#   import tester
#   tester.run_tests('filename_of_your_script.py')
# If you are using the command line:
#   python tester.py filename_of_your_script.py


import sys
import importlib

# Modified to work for any class name. This allows it to be used with
# Chad Miller's hungergames simulator or otherwise allows the user to
# write multiple players with class names other than Player.
# 
# Modifications by Michael Dickens.
def run_tests(script_name, class_name = 'Player'):
    try:
        user_module = importlib.import_module(script_name[:-3])
        if hasattr(user_module, class_name):
            try:
                user_module = eval("user_module.%s()" % class_name)
            except:
                print("\nPlayer did not instantiate, make sure it is a class. "
                      "Proceeding assuming non OO code.\n")
    except:
        print ("\nCould not import %s\n" % script_name)
        raise
    test_hunt_choices(user_module)
    test_hunt_outcomes(user_module)
    test_round_end(user_module)


def test_hunt_choices(user_module):
    """Checks if hunt_choices runs and returns the correct output"""
    try:
        decisions = user_module.hunt_choices(1, 0, 0, 5,
                                             [0,0,0,0,0,0,0,0,0,0,0,0])
    except AttributeError:
        print("\nFunction hunt_choices is not defined properly.\n")
        raise # shows the exact exception given by python 
    except:
        print("\nError running hunt_choices.\n")
        raise

    #is the output of the correct length
    if not decisions or len(decisions) != 12:
        raise BaseException("The array of decisions from hunt_choices "
                            "does not have a correct length. Please match"
                            "each opponent with a decision.")

    #is the output of the correct format
    for decision in decisions:
        if decision not in 'hs':
            raise BaseException("Incorrect format of the decisions. "
                                "Please use strings \"h\" or \"s\" only.")
    print("\nhunt_choices ran successfully!\n")


def test_hunt_outcomes(user_module):
    """Checks if hunt_outcomes runs"""
    try:
        user_module.hunt_outcomes([0,0,0,0,0,0,0,0,0,0,0,0])
    except AttributeError:
        print("\nFunction hunt_outcomes is not defined properly.\n")
        raise
    except:
        print("\nError running hunt_outcomes.\n")
        raise
    print("\nhunt_outcomes ran successfully!\n")

def test_round_end(user_module):
    """Checks if round_end runs"""
    try:
        user_module.round_end(0,4,3)
    except AttributeError:
        print("\nFunction round_end is not defined properly.\n")
        raise
    except:
        print("\nError running round_end.\n")
        raise
    print("\nround_end ran successfully!\n")

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except IndexError:
        print ("\nYou must include the filename that contains your code "
               "as the only argument to this script.\n\n"
               "Example: python tester.py filename_of_your_script.py\n")
        raise
    else:
        class_name = sys.argv[2] if len(sys.argv) >= 3 else 'Player'
        run_tests(filename, class_name)
