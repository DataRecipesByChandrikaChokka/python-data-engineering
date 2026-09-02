
#file validation program that checks incoming ETL files before processing.
#The project validates:
#Record count
#Expected record count
#File size
#File type
#Source system
#Processing status
file = "customer_20260813.csv"
environment = "PROD"
source = "ORACLE"
file_type = "CSV"
records = 125000
expected = 125000
file_size_mb = 85

if records == 0:
    status = "FAILED"
    message = "Empty file"
elif records > expected:
    status = "FAILED"
    message = "Record count above expected threshold"
elif records < expected:
    status = "FAILED"
    message = "Record count below expected threshold"
elif file_size_mb <= 0:
    status = "FAILED"
    message = "Invalid file size"
elif file_type != "CSV":
    status = "FAILED"
    message = "Invalid file type"
else:
    status = "SUCCESS"
    message = "File Validation Successful"

print("========================================")
print("         Daily File Validation          ")
print("========================================")
print(f"Environment : {environment}")
print(f"File        : {file}")
print(f"Source      : {source}")
print(f"File Type   : {file_type}")
print(f"Records     : {records}")
print(f"Expected    : {expected}")
print(f"File Size   : {file_size_mb} MB")
print(f"Status      : {status}")
print(f"Message     : {message}")
print("========================================")

