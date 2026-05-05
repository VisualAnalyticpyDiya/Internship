# Week 1: CSV Sales Analyzer

## Project Description
A Python script that reads sales data from a CSV file and calculates the total revenue per product.

## Technical Features
- **Data Parsing**: Uses the `csv.DictReader` module for structured data handling.
- **Robustness**: Implements `try-except` blocks to handle missing or invalid numeric data (ValueErrors).
- **Aggregation**: Calculates total revenue per product and identifies top-selling items.

## How to Run
1. Ensure you have `sales_data.csv` in the same folder as the script.
2. Run the script using: `data.py`

## Output Report
The script identifies missing data and skips invalid rows to provide:
- Total Revenue per Product
