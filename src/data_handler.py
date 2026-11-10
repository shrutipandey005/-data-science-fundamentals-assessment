"""
Data Handler - Ingestion, Type Classification, and Cleansing Pipeline
Demonstrates handling of diverse data structures and types in Data Science.
"""

import csv
import json
from datetime import datetime
from typing import List, Dict, Any, Tuple, Optional


class DataSchemaValidator:
    """
    Classifies, cleanses, and transforms raw tabular/JSON records into
    properly typed structures for analysis.
    """

    ORDINAL_MAPPINGS = {
        "satisfaction_tier": {
            "Low": 1,
            "Medium": 2,
            "High": 3,
            "Very High": 4
        }
    }

    @staticmethod
    def load_csv_data(filepath: str) -> List[Dict[str, Any]]:
        """Reads CSV file and returns list of dictionaries with raw string values."""
        records = []
        with open(filepath, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                records.append(dict(row))
        return records

    @staticmethod
    def load_json_data(filepath: str) -> List[Dict[str, Any]]:
        """Reads JSON file containing structured hierarchical objects."""
        with open(filepath, mode="r", encoding="utf-8") as f:
            return json.load(f)

    @classmethod
    def transform_churn_record(cls, raw: Dict[str, str]) -> Dict[str, Any]:
        """
        Parses and casts each column in the raw customer churn record into
        its appropriate statistical data type:
        - customer_id: Key / Identifier (str)
        - signup_date: Datetime (datetime.date)
        - tenure_months: Numerical Discrete (int)
        - monthly_charges: Numerical Continuous (float)
        - total_charges: Numerical Continuous (float)
        - contract_type: Categorical Nominal (str)
        - satisfaction_tier: Ordinal (str + mapped int rank)
        - support_tickets: Numerical Discrete (int)
        - feedback_notes: Text / Unstructured (str)
        - churned: Binary Categorical / Target (int: 0 or 1)
        """
        parsed = {}
        parsed["customer_id"] = raw["customer_id"].strip()
        
        # Datetime parsing
        parsed["signup_date"] = datetime.strptime(raw["signup_date"].strip(), "%Y-%m-%d").date()
        
        # Numerical discrete & continuous
        parsed["tenure_months"] = int(raw["tenure_months"])
        parsed["monthly_charges"] = float(raw["monthly_charges"])
        
        # Handle potential empty or missing total_charges
        raw_total = raw.get("total_charges", "").strip()
        if raw_total:
            parsed["total_charges"] = float(raw_total)
        else:
            # Impute total charges = tenure * monthly
            parsed["total_charges"] = round(parsed["tenure_months"] * parsed["monthly_charges"], 2)
            
        # Categorical Nominal
        parsed["contract_type"] = raw["contract_type"].strip()
        
        # Ordinal Data
        sat_tier = raw["satisfaction_tier"].strip()
        parsed["satisfaction_tier"] = sat_tier
        parsed["satisfaction_tier_numeric"] = cls.ORDINAL_MAPPINGS["satisfaction_tier"].get(sat_tier, 0)
        
        # Discrete support tickets
        parsed["support_tickets"] = int(raw["support_tickets"])
        
        # Text
        parsed["feedback_notes"] = raw["feedback_notes"].strip()
        
        # Binary target
        parsed["churned"] = int(raw["churned"])
        
        return parsed

    @classmethod
    def process_all_records(cls, filepath: str) -> List[Dict[str, Any]]:
        """Loads and parses all records from CSV."""
        raw_records = cls.load_csv_data(filepath)
        return [cls.transform_churn_record(r) for r in raw_records]
