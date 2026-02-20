import csv
import os

def extract_data():
    # Simulating data extraction (e.g., from an API or database)
    return [
        {"order_id": 1001, "customer_id": 501, "order_date": "2026-02-01", "region": "north", "quantity": 2, "unit_price": 25.00, "discount_pct": 0.10},
        {"order_id": 1002, "customer_id": 502, "order_date": "2026-02-02", "region": "south", "quantity": 1, "unit_price": 80.00, "discount_pct": 0.00},
        {"order_id": 1003, "customer_id": 503, "order_date": "2026-02-02", "region": "east", "quantity": 4, "unit_price": 12.50, "discount_pct": 0.05},
        {"order_id": 1004, "customer_id": 504, "order_date": "2026-02-03", "region": "west", "quantity": 3, "unit_price": 15.00, "discount_pct": 0.15},
    ]

def transform_data(rows):
    # Basic transformation in Python (optional, as dbt will handle heavy lifting)
    # Here we just pass it through, or we could normalize keys, etc.
    return rows

def load_data(rows, output_path):
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    if not rows:
        print("No data to load.")
        return

    keys = rows[0].keys()
    
    with open(output_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Data loaded to {output_path}")

def run_etl(output_path="etl/data/raw_orders.csv"):
    print("Starting ETL...")
    extracted_rows = extract_data()
    transformed_rows = transform_data(extracted_rows)
    load_data(transformed_rows, output_path)
    return transformed_rows

if __name__ == "__main__":
    run_etl()
