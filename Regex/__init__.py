import re

a = "-123*10^"

print(re.findall("-?[0-9]+(\*10\^)?[1-9]*", a))

# -?[0-9]+(\*10\^)?[1-9]*