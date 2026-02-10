#!/usr/bin/env python3
"""Convert CSV data to JSON format and save to data.json."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file into JSON format and save to data.json.

    Args:
        csv_filename (str): The name of the CSV file to convert.

    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except Exception:
        return False
