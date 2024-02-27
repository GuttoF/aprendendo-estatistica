# Import necessary libraries
from import_data import load_data
import streamlit as st

# Load the dataset
data = load_data()

data.head().T
