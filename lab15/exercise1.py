
filename = 'sample_text.txt'
content = """Hello, world!
This is a sample text file.
It contains multiple lines of text for testing file operations."""

with open(filename, 'w') as file:
    file.write(content)
print(f"Content has been written to {filename}")

with open(filename, 'r') as file:
    read_content = file.read()
print("Content read from the file:")
print(read_content)