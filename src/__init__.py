# MLOps with Agentic AI - Session 8: Complete CI/CD Pipeline
# Author: Amey Talkatkar
# Repository: https://github.com/ameytrainer/ml-forecast-system

"""
ML Forecast System - Source Code Package
"""

__version__ = "3.0.0"
__author__ = "MLOps Team"

from . import utils
from . import preprocess
from . import train
from . import evaluate

__all__ = ["utils", "preprocess", "train", "evaluate"]
