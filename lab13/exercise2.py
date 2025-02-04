import re

text1 = "Hello, world!"
text2 = "The world"

def find_match(pattern, text):
    print(f"Finding the given pattern in the text: \"{text}\"")
    match = re.match(pattern, text)
    if match:
        print("Match found:", match.group())
    else:
        print("Match not found.")

pattern = r"Hello"

find_match(pattern, text1)
find_match(pattern, text2)