#Validate each file and produce a batch-level report
#File validation program that checks incoming ETL files before processing.
#Validations:
# - Record count
# - Expected record count
# - File size
# - File type
# - Source system
# - Processing status
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

expected_records = [
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
source_systems = [
    "ORACLE",
    "TERADATA",
    "MYSQL",
    "SQLSERVER"
]
allowed_source_systems = [
    "ORACLE",
    "TERADATA",
    "SQLSERVER"
]
print("========================================")
print("        ETL BATCH FILE VALIDATION       ")
print("========================================")
success_count = 0
failure_count = 0
for i in range(len(files)):
    file_name = files[i]
    file_type = file_types[i]
    record_count = records[i]
    expected = expected_records[i]
    file_size = file_sizes[i]
    source_system = source_systems[i]
    if file_type != "CSV":
        status = "FAILED"
        message = "Invalid file type"
    elif record_count == 0:
        status = "FAILED"
        message = "Empty File"
    elif record_count > expected:
        status = "FAILED"
        message = "Record count is above expected threshold"
    elif record_count < expected:
        status = "FAILED"
        message = "Record count is below expected threshold"
    elif file_size <= 0:
        status = "FAILED"
        message = "Invalid file size"
    elif source_system not in allowed_source_systems:
        status = "FAILED"
        message = "Invalid source system"
    else:
        status = "SUCCESS"
        message = "File Validation Successful"
    if status == "SUCCESS":
        success_count = success_count + 1
    else:
        failure_count = failure_count + 1

    print("========================================")
    print("         Daily File Validation          ")
    print("========================================")
    print(f"File          : {file_name}")
    print(f"File Type     : {file_type}")
    print(f"Records       : {record_count}")
    print(f"Expected      : {expected}")
    print(f"File Size     : {file_size} MB")
    print(f"Source System : {source_system}")
    print(f"Status        : {status}")
    print(f"Message       : {message}")
    if status == "SUCCESS":
        print(f"Processing {file_name} file")
    else:
        print(f"File {file_name} rejected - ETL Processing Skipped")
    print("========================================")
if failure_count > 0:
    batch_status = "FAILED"
else:
    batch_status = "SUCCESS"
print("========================================")
print("               BATCH SUMMARY            ")
print("========================================")
print(f"Total files  : {len(files)}")
print(f"Successful   : {success_count}")
print(f"Failed       : {failure_count}")
print(f"Batch Status : {batch_status}")
print("========================================")
