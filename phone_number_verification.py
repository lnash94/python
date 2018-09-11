import re

#regular expression phone number veryfication

# \w [a-zA-Z0-9]
# \w [^a-zA-Z0-9]

phone_number = "412-555-1212"


if re.search("\w{3}-\w{3}-\w{4}", phone_number):
	print("it is phone number")

