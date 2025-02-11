import json

person_info = {
    "name": "John",
    "age": 21,
    "courses": ["Math", "Geography", "Computer Science", "History"],
    "gpa": 3.01,
}

json_string = json.dumps(person_info, indent=4)

print("Serialized JSON string:")
print(json_string)