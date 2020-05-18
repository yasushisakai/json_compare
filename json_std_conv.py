#!/usr/bin/python3

import sys
import json


inp = input()
print(inp)

file = open(inp, 'r')
data = json.loads(file.read())
file.close()

print(json.dumps(data, sort_keys=True, indent=2))
