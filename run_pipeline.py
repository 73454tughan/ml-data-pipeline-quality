"""
One-Command Execution Script for Lab 4 Machine Learning Pipeline
Student: Tughan Bulut Kurtulus (73454)
Usage:
    python run_pipeline.py
"""
import sys
from src.pipeline_runner import execute_pipeline

if __name__ == "__main__":
    try:
        execute_pipeline()
        sys.exit(0)
    except Exception as e:
        print(f"[FATAL PIPELINE ERROR]: {e}", file=sys.stderr)
        sys.exit(1)
