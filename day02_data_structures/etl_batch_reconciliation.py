# Every morning, several source systems drop files into an incoming folder:
# ORACLE      → customers.csv
# TERADATA    → orders.csv
# SQLSERVER   → products.csv
# MYSQL       → payments.csv
# Before your ETL job starts, Python needs to check:
# 1. Which files arrived?
# 2. Are they valid file types?
# 3. Are they empty?
# 4. How many records are present?
# 5. Is the source system allowed?
# 6. Which files are ready for processing?
# 7.Which files should be rejected?
# 8.How many files came from each source?
# 9.What is the overall batch status?

# input data
files = [
    {
        "file_name": "customers_20260908.csv",
        "source": "ORACLE",
        "file_type": "CSV",
        "records": 125000,
        "expected_records": 125000
    },
    {
        "file_name": "orders_20260908.csv",
        "source": "TERADATA",
        "file_type": "CSV",
        "records": 850000,
        "expected_records": 850000
    },
    {
        "file_name": "payments_20260908.txt",
        "source": "MYSQL",
        "file_type": "TXT",
        "records": 450000,
        "expected_records": 450000
    },
    {
        "file_name": "products_20260908.csv",
        "source": "SQLSERVER",
        "file_type": "CSV",
        "records": 0,
        "expected_records": 25000
    },
    {
        "file_name": "employees_20260908.csv",
        "source": "SAP",
        "file_type": "CSV",
        "records": 15000,
        "expected_records": 15000
    }
]
allowed_sources = {
    "ORACLE",
    "TERADATA",
    "MYSQL",
    "SQLSERVER"
}
total_files = len(files)
source_systems = set()
unsupported_sources = []
source_counts = {}
success_files = 0
failed_files = 0
files_ready = []
files_failed = []
for file in files:
    reasons = []
    source_systems.add(file["source"])
    if file["source"] not in allowed_sources:
        unsupported_sources.append(file["source"])
    source_counts[file["source"]] = source_counts.get(file["source"], 0) + 1
    if file["file_type"] == "CSV" and file["records"] > 0 and file["records"] == file["expected_records"] and file["source"] in allowed_sources:
        status = "SUCCESS"
        success_files = success_files + 1
        files_ready.append(file["file_name"])
    else:
        status = "FAILED"
        failed_files = failed_files + 1
        files_failed.append(file["file_name"])
    if file["file_type"] != "CSV":
        reasons.append("Invalid file type")
    if file["records"] == 0:
        reasons.append("Empty file")
    if file["records"] != file["expected_records"]:
        reasons.append("record count mismatched with expected")
    if file["source"] not in allowed_sources:
        reasons.append("Source is not allowed")
    print("===================================================")
    print("             File Validation                       ")
    print("======================================================")
    print(file["file_name"])
    print(f"status: {status}")
    if status == "FAILED":
        print("Reasons:")
        for reason in reasons:
            print(f"-{reason}")
    print("======================================================")
if failed_files > 0:
    batch_status = "FAILED"
else:
    batch_status = "SUCCESS"

print("=========================================================")
print("                  ETL FILE INTAKE REPORT                 ")
print("==========================================================")
print(f"\nTotal Files       : {total_files}")
print(f"Successful Files  : {success_files}")
print(f"Failed Files      : {failed_files}")
print(f"Unique Sources    : {len(source_systems)}")
print(f"\nFiles ready:")
for file_name in files_ready:
    print(f"- {file_name}")
print(f"\nFiles failed:")
for file_name in files_failed:
    print(f"- {file_name}")
print(f"\n Batch Status   : {batch_status}")
print("=======================================================")

