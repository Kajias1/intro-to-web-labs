import re

text = "apple, watermelon, blackberry, onion"

vowels = "AEIOU"

pattern = r"\b[aeiouAEIOU]\w*\b"

matches = re.findall(pattern, text)
print("Matches found:", matches)