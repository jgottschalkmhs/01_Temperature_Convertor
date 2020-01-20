# checks if something is valid

import re

filename = input("Enter a filename: ")
has_error = "no"

valid_char = "[A-Za-z0-9_]"
for letter in filename:
    if re.match(valid_char, letter):
        print("ok")

    else:
        print("nope")
        has_error = "yes"

if has_error == "yes":
    print("Invalid filename")
else:
    print("good to go")
