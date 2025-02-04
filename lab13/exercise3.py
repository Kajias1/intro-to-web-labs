import re

text = "Everest mount elevation is 8849 m, and Nile river length is 6650 km"
pattern = r"\d+"

output = re.sub(pattern, "<NUMBER>", text)

print("Substituted text:", output)