# Add this at the VERY TOP before any other imports
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend for Streamlit Cloud

# Then proceed with the rest of the imports
import streamlit as st
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# ... [REST OF THE CODE REMAINS UNCHANGED FROM PREVIOUS VERSION] ...