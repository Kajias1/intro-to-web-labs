import re

# Search and replace

text = "My phone number is 1234567890 and my office number is 9876543210"
pattern = r"\d+"
replacement = "NUMBER"

result = re.sub(pattern, replacement, text)
print(result)

# Basic functions
# re.search()

text = "The rain in Spain falls mainly on the plain."
pattern = r"Spain"

match = re.search(pattern, text)
if match:
    print("Found:", match.group())
else:
    print("Not found.")

# re.match

text = "Hello, world!"
pattern = r"Hello"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match.")

# re.findall()

text = "John's number is 555-1234, and Marry's number is 555-5678."
pattern = r"\d{3}-\d{4}"

matches = re.findall(pattern, text)
print("Phone numbers found:", matches)

# Raw strings, pattern complexity and flags

match = re.search(r"python", "I love python", re.IGNORECASE)
if match:
    print("Match found:", match.group())
