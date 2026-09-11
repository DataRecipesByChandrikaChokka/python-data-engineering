# Lists
# Create a  list of Files
files = [
    "customers.csv",
    "orders.csv",
    "payments.csv",
    "products.csv"
]
# print first file
print(files[0])
# print last file
print(files[3])
print(files[-1])
# add "employees.csv" to the list
files.append("employees.csv")
# change "orders.csv" to "orders _2026.csv"
files[1] = "orders_2026.csv"
# print the final list
print(files)

# Tuples
# Create Tuple database_config
database_config = ("ORACLE", "PROD", "customer_db")
# print the first value
print(database_config[0])
# print the last value
print(database_config[-1])
# Try changing "ORACLE" to "TERADATA"
# This will raise TypeError because tuples are immutable
# database_config[0] = "TERADATA"

# SET
source_systems = [
    "ORACLE",
    "MYSQL",
    "TERADATA",
    "ORACLE",
    "SQLSERVER",
    "MYSQL",
    "TERADATA"
]
# print original list
print(source_systems)
# convert into a set
unique_sources = set(source_systems)
print(unique_sources)
print(f"Number of unique source systems:{len(unique_sources)}")

# Dictionary
employee = {
    "employee_id": 101,
    "employee_name": "Chandrika",
    "department": "Data Engineering",
    "experience": 11,
    "is_active": True
}
# print the employee name
print(employee["employee_name"])
# print the department
print(employee["department"])
# Change the experience from 11 to 12
employee["experience"] = 12
# add new key "location": "Bangalore"
employee["location"] = "Bangalore"
# print the dictionary
for key, value in employee.items():
    print(f"{key}: {value}")
# List of Dictionaries
customers = [
    {
        "customer_id": 101,
        "customer_name": "Ravi",
        "source": "ORACLE",
        "salary": 75000
    },
    {
        "customer_id": 102,
        "customer_name": "Chandrika",
        "source": "TERADATA",
        "salary": 850000,
    },
    {
        "customer_id": 103,
        "customer_name": "Arun",
        "source": "MYSQL",
        "salary": 65000
    }

]
print(customers[0])
print(customers[0]["customer_name"])
# print customer names
# in for customer is dictionary not index
for customer in customers:
    print(customer["customer_name"])
# process customers with only salary greater than 70000
for customer in customers:
    if customer["salary"] > 70000:
        print(customer["customer_name"])
employees = [
    {
        "employee_id": 101,
        "name": "Ravi",
        "department": "Data Engineering",
        "salary": 75000
    },
    {
        "employee_id": 102,
        "name": "priya",
        "department": "Testing",
        "salary": 60000
    },
    {
        "employee_id": 103,
        "name": "Arun",
        "department": "Data Engineering",
        "salary": 85000
    }
]
# print each employee's name
# print each employee's department
for employee in employees:
    print(f"employee name: {employee['name']}")
    print(f"department: {employee['department']}")
# print only employees whose salary is grater than 70000
for employee in employees:
    if employee["salary"] > 70000:
       print(employee["name"])

# data from different sources
customers = [
    {
        "customer_id": 101,
        "name": "Ravi",
        "source": "ORACLE",
        "status": "ACTIVE",
        "salary": 75000
    },
    {
        "customer_id": 102,
        "name": "Priya",
        "source": "TERADATA",
        "status": "INACTIVE",
        "salary": 60000
    },
    {
        "customer_id": 103,
        "name": "Arun",
        "source": "ORACLE",
        "status": "ACTIVE",
        "salary": 85000
    },
    {
        "customer_id": 104,
        "name": "Sneha",
        "source": "MYSQL",
        "status": "ACTIVE"
    }
]
sources = []
# print name of every customer
for customer in customers:
    print(customer["name"])
    if customer["status"] == "ACTIVE":
        print(f"{customer['name']} is active")
    salary = customer.get("salary", 0)
    if salary > 70000:
        print(customer["name"])
    sources.append(customer["source"])
    print(sources)
unique_sources = set(sources)
print(unique_sources)
print(len(unique_sources))


