import json

json_string = '''
{
    "name": "Alice",
    "age": 21,
    "courses": [
        "Math",
        "Science",
        "History"
    ]
}
'''

student_info = json.loads(json_string)

print("Deserialized Python object:")
print(student_info)