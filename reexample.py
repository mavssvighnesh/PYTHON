import re
str="vamsi and satish are my bestfriends"
print(re.findall("s",str))
print(re.split("",str,5))
print(re.search("are",str))
print(re.sub("satish","vighnesh" ,str))
