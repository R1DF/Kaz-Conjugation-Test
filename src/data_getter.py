# Imports
import os
import json

# Returning file contents
tenses_file_data = json.load(open(os.getcwd() + "\\tenses.json", "r", encoding="utf-8"))
verbs_list = json.load(open(os.getcwd() + "\\verbs.json", "r", encoding="utf-8"))
