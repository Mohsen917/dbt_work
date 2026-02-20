import unittest
import os
import shutil
import tempfile
import csv
import sys

# Add the directory containing etl.py to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from etl import extract_data, transform_data, load_data, run_etl

class TestETL(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_extract_data(self):
        """Test that data extraction returns a list of dictionaries with expected keys."""
        data = extract_data()
        self.assertIsInstance(data, list)
        self.assertTrue(len(data) > 0)
        first_row = data[0]
        expected_keys = {"order_id", "customer_id", "order_date", "region", "quantity", "unit_price", "discount_pct"}
        self.assertEqual(set(first_row.keys()), expected_keys)
        self.assertEqual(first_row["order_id"], 1001)

    def test_transform_data(self):
        """Test that transformation logic works (currently pass-through)."""
        input_data = [{"id": 1, "val": "test"}]
        output_data = transform_data(input_data)
        self.assertEqual(output_data, input_data)

    def test_load_data(self):
        """Test that data is correctly written to a CSV file."""
        p = os.path.join(self.test_dir, "test_output.csv")
        
        test_data = [
            {"col1": "val1", "col2": 10},
            {"col1": "val2", "col2": 20}
        ]
        
        load_data(test_data, p)
        
        # Check if file exists
        self.assertTrue(os.path.exists(p))
        
        # Check content
        with open(p, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[0]["col1"], "val1")
            self.assertEqual(rows[0]["col2"], "10")  # CSV reads as string
            self.assertEqual(rows[1]["col1"], "val2")

    def test_run_etl(self):
        """Test the full ETL pipeline."""
        output_file = os.path.join(self.test_dir, "final_output.csv")
        
        result = run_etl(output_path=output_file)
        
        self.assertEqual(len(result), 4)  # Based on current extract_data implementation
        self.assertTrue(os.path.exists(output_file))
        
        with open(output_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            self.assertEqual(len(rows), 4)

if __name__ == "__main__":
    unittest.main()
