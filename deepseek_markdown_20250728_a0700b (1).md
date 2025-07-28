# 🎰 DegenCrash Predictor

## Streamlit Cloud Deployment Guide

1. **Create GitHub repository** with these files:
   - `app.py`
   - `requirements.txt`
   - `setup.sh`
   - `README.md`

2. **Go to [Streamlit Cloud](https://share.streamlit.io/)**
   - Click "New app"
   - Select "From existing repo"

3. **Configure app settings:**
   - Repository: `your-username/your-repo-name`
   - Branch: `main`
   - Main file path: `app.py`
   - Python version: 3.10

4. **Add Advanced Settings:**
   - Click "Advanced settings..."
   - Add this command: `bash setup.sh`
   - Click "Save"

5. **Click "Deploy"**

The app will build in 2-5 minutes. You'll see "Your app is live!" when deployment completes.