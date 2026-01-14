import re #regular expression library

p = re.compile("ab*")

if p.match("a") :
    print("match")
else
    print("not match")