# Day 1 - Python Basics
# Covers variables, data types, conditions, lists, loops, strings, and range()
customer_id = 101
customer_name = "Ravi"
salary = 650000
is_active = True
print(f" customerId: {customer_id} type: {type(customer_id)}")
print(f" customer_name: {customer_name} type: {type(customer_name)}")
print(f" salary: {salary} type:{type(salary)}")
print(f" is_active: {is_active} type:{type(is_active)}")
salary = 75000
if salary > 60000:
    print("High Salary")
else:
    print("normal salary")
files = [
    "customer.csv",
    "orders.csv",
    "products.csv",
    "payments.csv"
]
for file in files:
    print(f"Processing {file}")
records = [100, 250, 0, 500, 1000]
for record in records:
    if record > 200:
        print(record)
name = "  chandrika  "
clean_name = name.strip().upper()
print(clean_name)
for i in range(4):
    print(i)

