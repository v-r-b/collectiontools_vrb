"""
Sample usage of functions from __init__.py
"""

import json, sys
from collectiontools_vrb import *

print("""
###########################################################
# SAMPLE USAGE: silent update_dict_from_url
###########################################################
""")

some_dict: dict = {}
some_URL = "https://raw.githubusercontent.com/v-r-b/"\
            "collectiontools_vrb/main/tests/sample.properties"
# Update existing dict "some_dict" with contents of URL.
r = update_dict_from_url(some_dict, some_URL)
assert r, f"Error reading URL {some_URL}"
# pretty print dict
print("dict read from URL", some_URL)
print(json.dumps(some_dict, indent=4))

print("""
###########################################################
# SAMPLE USAGE: update_dict_from_key_value_file w/ error output
###########################################################
""")

some_dict = {}
some_file = "tests/sample.properties"
# Update existing dict "some_dict" with contents of key-value file.
# In case of errors, print them to stderr.
r = update_dict_from_key_value_file(some_dict, some_file, 
                                    print_errors_to=sys.stderr)
assert r, f"Error reading file {some_file}"
print("dict read from file", some_file)
print(json.dumps(some_dict, indent=4))

print("""
###########################################################
# SAMPLE USAGE: update_dict_from_json_file w/ reraise exc
###########################################################
""")

# Update existing dict "some_dict" with contents of JSON file,
# here: combine them with the previously read contents of the properties file.
# In case of an exception, catch and show it, but terminate test.
additional_data_file = "tests/sample_data.json"
try:
    r = update_dict_from_json_file(some_dict, additional_data_file,
                                   reraise_exc=True)
    assert r, f"error reading file {additional_data_file}"
    print("dict replenished from file", additional_data_file)
    print(json.dumps(some_dict, indent=4))
except BaseException as exc:
    print(f"Got exception {exc} when reading json file")
    sys.exit()
# variant: update and test existance of mandatory keys (will fail)
r = update_dict_from_json_file(some_dict, additional_data_file, 
                               mandatory_keys=["abc", "test.x.y"], 
                               print_errors_to=sys.stderr)
assert not r, "Mandatory keys should be missing, but were found!"

# but: update and test existance of mandatory keys (will succeed)
r = update_dict_from_json_file(some_dict, additional_data_file,
                               mandatory_keys=["SecondLine", "SecondLine.Part2"], 
                               print_errors_to=sys.stderr)
assert r, "Mandatory keys should be found, but are missing!"

print("""
###########################################################
# SAMPLE USAGE: dict_contains_path
###########################################################
""")

# Some tests for the existence of some paths within a dict.
# For these tests, use some_dict, which has been updated above.
print(f"FirstLinePart2 exists: {dict_contains_path(some_dict, 'FirstLinePart2')}") # True
assert dict_contains_path(some_dict, 'FirstLinePart2')
print(f"FirstLinePart5 exists: {dict_contains_path(some_dict, 'FirstLinePart5')}") # False
assert not dict_contains_path(some_dict, 'FirstLinePart5')
print(f"SecondLine.Part1 exists: {dict_contains_path(some_dict, 'SecondLine.Part1')}") # True
assert dict_contains_path(some_dict, 'SecondLine.Part1')
print(f"SecondLine.Part1.Word2 exists: {dict_contains_path(some_dict, 'SecondLine.Part1.Word2')}") # False
assert not dict_contains_path(some_dict, 'SecondLine.Part1.Word2')

print("""
###########################################################
# ALL TESTS SUCCEEDED
###########################################################
""")

