# Data Structures
# List,Tuple,Set,Dictionary
# LIST-- Multiple values, ordered, can change
# TUPLE -- Multiple values, ordered, can not change
# SET -- Unique values, Duplicates removed
# DICTIONARY -- key --> value, Describes an object / record

# Lists []
# Lists (Ordered Collection) list stores multiple values and can be changed
# in List we can have another list or dictionary but in real data engineering we keep
# list logically consistent unless there is good reason not to
# List is useful when we have a collection of similar things

files = [
    "customers.csv",
    "orders.csv",
    "payments.csv"
]
print(files[0], files[1], files[2])
files[1] = "orders_2026.csv" # changing the list
print(files[1])
files.append("products.csv") # appending new values to the list
print(files[3])
files = ["customers.csv", "payments.csv", "orders.csv", "products.csv"]
source_systems = ["ORACLE", "TERADATA", "MYSQL", "SQLSERVER"]
records = [1000, 2500, 3000]

# Tuples(similar to list)()
# ordered but can not be changed
# This is useful when we have information like configration  that should be remain fixed
source_details = ("ORACLE", "CUSTOMER", "PROD")
print(source_details[1])
# Can not change or add to tuple source_details[3] = "TERADATA"
# When You do not want someone accidentally changing these values while your program is running
database_config = ("ORACLE", "PROD", 1521)

# SET -- Unique values
# When you want only unique values
# python removes duplicate values automatically
# This is very useful in Data engineering if we receive duplicates in source systems
# we can not use normal indexing for set because it is designed around uniqueness not positional order
source_systems = {
    "ORACLE",
    "TERADATA",
    "ORACLE",
    "MYSQL",
    "TERADATA"
}
print(source_systems) # will result {'ORACLE', 'MYSQL', 'TERADATA'}
source_systems = [
    "ORACLE",
    "TERADATA",
    "ORACLE",
    "MYSQL",
    "TERADATA"
]

unique_sources = set(source_systems)
print(unique_sources)

# Dictionary
# dictionary stored as key - value
# key identifies the information  and the value contains the information
# Think of it is a database row
# can be changed and append
customer = {
    "customer_id": 101,
    "customer_name": "Ravi",
    "salary": 75000,
    "is_active": True
}
print(customer["customer_id"])
print(customer["salary"])
# if we create different list for each information we need to use indexes
files = [
    "customers_20260902.csv",
    "orders_20260902.csv",
    "payments_20260902.txt",
    "products_20260902.csv"
]
file_types = [
    "CSV",
    "CSV",
    "TXT",
    "CSV"
]
records = [
    125000,
    850000,
    450000,
    25000
]

file_sizes = [
    85,
    250,
    120,
    20
]

print(files[1])
print(file_types[1])
print(records[1])
print(file_sizes[1])

# But A dictionary let us keep the information together
file = {
    "name": "orders_20260902.csv",
    "type": "CSV",
    "records": 850000,
    "size_mb": 85,
    "source": "ORACLE"
}
print(file["name"])
print(file["size_mb"])

# get()
# if any key that not exists and if we want to process python will through error
# but with get we get none so get() is safer when a field might be missing
# very useful in data engineering because real world source data can have missing columns / attributes
# print(file["environment"])
print(file.get("environment"))
# get() with default value
employee = {
    "employee_id": 101,
    "employee_name": "Ravi",
    "department": "Data Engineering"
}
print(employee.get("employee_name"))
print(employee.get("department"))
print(employee.get("salary"))
print(employee.get("salary", 0))
employee["salary"] = 75000
print(employee.get("salary"))

# nested dictionaries
# Real world JSON like data
customer = {
    "customer_id": 101,
    "name": "Ravi",
    "address": {
        "city": "Bangalore",
        "state": "Karnataka",
        "country": "India"
    }
}
# print customer name
print(customer["name"])
# print city

print(customer["address"]["city"])
print(customer["address"].get("city"))
# print state
print(customer["address"].get("state"))
# print country
print(customer["address"].get("country"))
# dictionary methods
# .keys()-- gives you all the Keys
# .values() -- gives you all the values
# .items() -- gives keys + values
# .get() -- value safely

employee = {
    "employee_id": 101,
    "name": "Ravi",
    "department": "Data Engineering",
    "salary": 75000
}
# print all the keys
print(employee.keys())
# print all the values
print(employee.values())
# loop through .items()
for key, value in employee.items():
    print(f"{key}--> {value}")
print(employee.get("salary"))
print(employee.get("location","Unknown"))
