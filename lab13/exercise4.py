import re

text = "His email is some_person@example.com, My email is my_email@example.com"

pattern = r"\b\w+@\w+\.\w+\b"

emails = re.findall(pattern, text)
print("Emails found:", emails)