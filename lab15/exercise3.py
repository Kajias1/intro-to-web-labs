filename = "sample_text.txt"
additional_text = "\nThis line is appended to the file."

with open(filename, 'a') as file:
    file.write(additional_text)
print(f"Additional text has been appended to {filename}")

with open(filename, 'r') as file:
    updated_content = file.read()
    print("Updated_content of the file:")
    print(updated_content)