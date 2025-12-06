# MLOps with Agentic AI - Session 8: Complete CI/CD Pipeline
# Author: Amey Talkatkar
# Repository: https://github.com/ameytrainer/ml-forecast-system

"""
Data Validation Script
Validates data quality and schema
"""

import sys
import pandas as pd


def validate_data(data_path: str):
    """
    Validate dataset quality and schema
    
    Args:
        data_path: Path to CSV file
    
    Returns:
        bool: True if valid, exits with error code if invalid
    """
    print(f"📊 Validating dataset: {data_path}")
    print()
    
    try:
        # Load data
        df = pd.read_csv(data_path)
        print(f"✓ Data loaded successfully")
        print(f"  Rows: {len(df):,}")
        print(f"  Columns: {df.shape[1]}")
        print()
        
        # Check required columns
        required_cols = [
            'date', 'sales', 'advertising_spend', 
            'promotions', 'day_of_week', 'month', 'is_weekend'
        ]
        
        missing_cols = set(required_cols) - set(df.columns)
        if missing_cols:
            print(f"❌ Missing required columns: {missing_cols}")
            sys.exit(1)
        print(f"✓ All required columns present")
        print()
        
        # Check for missing values
        missing = df.isnull().sum().sum()
        if missing > 0:
            print(f"❌ Found {missing} missing values")
            print(df.isnull().sum())
            sys.exit(1)
        print(f"✓ No missing values")
        print()
        
        # Check data size
        if len(df) < 1000:
            print(f"❌ Dataset too small: {len(df)} rows (minimum: 1000)")
            sys.exit(1)
        print(f"✓ Dataset size adequate: {len(df):,} rows")
        print()
        
        # Check data types
        if not pd.api.types.is_numeric_dtype(df['sales']):
            print(f"❌ 'sales' column must be numeric")
            sys.exit(1)
        print(f"✓ Data types correct")
        print()
        
        # Check value ranges
        if (df['sales'] < 0).any():
            print(f"❌ Negative sales values found")
            sys.exit(1)
        
        if not df['promotions'].isin([0, 1]).all():
            print(f"❌ 'promotions' must be 0 or 1")
            sys.exit(1)
        
        if not ((df['day_of_week'] >= 0) & (df['day_of_week'] <= 6)).all():
            print(f"❌ 'day_of_week' must be 0-6")
            sys.exit(1)
        
        if not ((df['month'] >= 1) & (df['month'] <= 12)).all():
            print(f"❌ 'month' must be 1-12")
            sys.exit(1)
        
        print(f"✓ Value ranges valid")
        print()
        
        # Summary statistics
        print("📈 Dataset Summary:")
        print(f"  Date range: {df['date'].min()} to {df['date'].max()}")
        print(f"  Sales range: ${df['sales'].min():.2f} to ${df['sales'].max():.2f}")
        print(f"  Sales mean: ${df['sales'].mean():.2f}")
        print(f"  Sales std: ${df['sales'].std():.2f}")
        print()
        
        print("=" * 60)
        print("✅ DATA VALIDATION PASSED")
        print("=" * 60)
        
        return True
        
    except FileNotFoundError:
        print(f"❌ File not found: {data_path}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Validation error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_data.py <data_path>")
        sys.exit(1)
    
    data_path = sys.argv[1]
    validate_data(data_path)