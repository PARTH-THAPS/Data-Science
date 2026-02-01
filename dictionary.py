#
medals = {}

medals = {"USA": 112, "Germany": 36, "China": 100}
print(medals.get("USA"))
medals["Italy"] = 40


# Key, values and items
print(medals.keys())
print(medals.values())
print(medals.items())

employee = {
    "id": 1010,
    "name": "alice",
    "age": 28,
    "department": "IT",
    "salary": 60000,
    "skills": ["python", "SQL", "Django"]
}


for key, value in employee.items():
    print(key, "=>", value)
