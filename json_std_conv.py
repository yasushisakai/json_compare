#!/usr/bin/python3

import sys
import json

inp = sys.stdin

data = json.loads(inp.read())

print(json.dumps(data, sort_keys=True, indent=2))
