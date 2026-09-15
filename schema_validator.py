import csv

def validate_csv_schema(file_path: str, expected_columns: list[str]) -> bool:
    """Validates if an incoming CSV file matches expected data pipeline headers before ingestion."""
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader, None)
        
        if header == expected_columns:
            print("Schema Validation Passed.")
            return True
        else:
            print(f"Schema Mismatch! Expected: {expected_columns}, Found: {header}")
            return False

if __name__ == "__main__":
    expected_headers = ["id", "first_name", "last_name", "email", "signup_date", "status"]
    # Example usage:
    # validate_csv_schema("sample_file.csv", expected_headers)
