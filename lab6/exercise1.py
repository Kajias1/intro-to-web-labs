#1 Variable types
int_input = int(input("Enter an integer: "))
float_input = float(input("Enter a float: "))
string_input = input("Enter a string: ")
print(type(int_input))
print(type(float_input))
print(type(string_input))

#2 Data conversion
text_data = "1000"
int_data = int(text_data)
float_data = float(int_data)
print("Text data: ", text_data)
print("Integer data: ", int_data)
print("Float data: ", float_data)

dictionary = {"name": "John", "age": 25, "job": "Teacher"}
print(dictionary["name"])
print(dictionary["age"])
print(dictionary["job"])

#3 Operations on sets
myset = {0, 5, 10}
myset.add(15)
myset.remove(0)
print(10 in myset)