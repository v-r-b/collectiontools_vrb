"""
Sample usage of functions from __init__.py
"""

import json
from collectiontools_vrb import *

###########################################################
# SAMPLE USAGE: update_dict_from_url
###########################################################

some_dict: dict = {}
# Update existing dict "some_dict" with contents of URL.
r = update_dict_from_url(some_dict,
            "https://raw.githubusercontent.com/v-r-b/"\
            "collectiontools_vrb/main/tests/sample.18n.properties")
if r:
    # pretty print dict
    print(json.dumps(some_dict, indent=4))
else:
    print("error reading URL")

###########################################################
# SAMPLE USAGE: update_dict_from_key_value_file
###########################################################

some_dict = {}
# Update existing dict "some_dict" with contents of key-value file.
# In case of errors, print them to stderr.
r = update_dict_from_key_value_file(some_dict, "tests/sample.properties", 
                                    print_errors_to=sys.stderr)
if r:
    print(json.dumps(some_dict, indent=4))
else:
    print("error reading file")

###########################################################
# SAMPLE USAGE: update_dict_from_json_file
###########################################################

# Update existing dict "some_dict" with contents of JSON file,
# here: combine them with the previously read contents of the properties file.
# In case of an exception, catch it.
try:
    r = update_dict_from_json_file(some_dict, "tests/sample_data.json",
                                   reraise_exc=True)
    if r:
        print(json.dumps(some_dict, indent=4))
    else:
        print("error reading file")
except BaseException as exc:
    print(f"Got exception {exc} when reading json file")
# variant: update and test existance of mandatory keys
r = update_dict_from_json_file(some_dict, 
                               "tests/sample_data.json", 
                               mandatory_keys=["abc", "test.x.y"], 
                               print_errors_to=sys.stderr)
if r:
    print(json.dumps(some_dict, indent=4))
else:
    print("error reading file")

###########################################################
# SAMPLE USAGE: dict_contains_path
###########################################################

# Some tests for the existence of some paths within a dict.
# For these tests, use some_dict, which has been updated above.
print(f"FirstLinePart2: {dict_contains_path(some_dict, 'FirstLinePart2')}") # True
print(f"FirstLinePart5: {dict_contains_path(some_dict, 'FirstLinePart5')}") # False
print(f"SecondLine.Part1: {dict_contains_path(some_dict, 'SecondLine.Part1')}") # True
print(f"SecondLine.Part1.Word2: {dict_contains_path(some_dict, 'SecondLine.Part1.Word2')}") # False

