# Python Data Engineering Utilities

A collection of lightweight Python utility scripts designed for source-to-target data reconciliation, record audits, and file schema validations in data pipelines.

## Scripts Included
* **`reconciliation_utility.py`:** Reconciles count matches and identifies missing primary keys between source extracts (e.g., MySQL, IBM DataStage) and target tables (Snowflake).
* **`schema_validator.py`:** Validates structural column consistency for incoming file drops prior to warehouse execution.

## Tech Stack
* **Language:** Python 3.9+ (Standard Library)
