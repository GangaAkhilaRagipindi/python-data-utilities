def reconcile_records(source_data: list[dict], target_data: list[dict], key_field: str) -> dict:
    source_keys = {row[key_field] for row in source_data}
    target_keys = {row[key_field] for row in target_data}

    return {
        "source_count": len(source_data),
        "target_count": len(target_data),
        "count_match": len(source_data) == len(target_data),
        "missing_in_target": list(source_keys - target_keys),
        "missing_in_source": list(target_keys - source_keys)
    }

if __name__ == "__main__":
    mysql_extract = [{"id": "1", "val": "A"}, {"id": "2", "val": "B"}, {"id": "3", "val": "C"}]
    snowflake_load = [{"id": "1", "val": "A"}, {"id": "2", "val": "B"}]

    report = reconcile_records(mysql_extract, snowflake_load, key_field="id")
    print("Data Validation Audit Results:", report)
