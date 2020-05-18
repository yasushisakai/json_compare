#!/usr/bin/python

import sys
import json

# file_name = sys.argv[1]
file_name = input()

file = open(file_name, 'r')
data = json.loads(file.read())
file.close()

print(json.dumps(data, sort_keys=True, indent=2))
