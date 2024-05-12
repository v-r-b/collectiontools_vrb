"""
Sample usage of CollectionTranslator from collectiontranslator.py
"""

import json
from collectiontools_vrb import CollectionTranslator

######################################
# SAMPLE USAGE: CollectionTranslator
######################################

# with s == "some_key" the entry will be modified as follows:
# "{some_key}" --> "[SOME_KEY]"
def some_func(s: str) -> str: return f"[{s.upper()}]"

with open("tests/collection_translator_sample.json") as fp:
    j = json.load(fp)
print("====== Original Version ================================") 
print(json.dumps(j, indent=4))
t = CollectionTranslator(some_func)
t.translate_dict(j)
print("====== Translated Version ==============================")
print(json.dumps(j, indent=4))

