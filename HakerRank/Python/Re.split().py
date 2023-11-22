# Python / Regex and Parsing / Re.split()
# https://www.hackerrank.com/challenges/re-split/problem?isFullScreen=true
regex_pattern = r",|\."	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))