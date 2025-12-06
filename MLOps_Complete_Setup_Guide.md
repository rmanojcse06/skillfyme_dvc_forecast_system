# 🚀 Complete MLOps Pipeline Setup Guide
## End-to-End Automated ML System with CI/CD

**Course:** MLOps with Agentic AI (Advanced Certification Course)  
**Duration:** 60-90 minutes  
**Platforms:** Windows & macOS  
**Tools:** Anaconda Prompt / VS Code Terminal  
**Result:** Fully automated ML pipeline with zero manual deployment

---

# 📋 Table of Contents

1. [Prerequisites & System Requirements](#prerequisites)
2. [Phase 1: GitHub Repository Setup](#phase-1-github-repository)
3. [Phase 2: DagsHub Account & Configuration](#phase-2-dagshub-setup)
4. [Phase 3: Local Environment Setup](#phase-3-environment-setup)
5. [Phase 4: DagsHub Integration](#phase-4-dagshub-integration)
6. [Phase 5: GitHub Secrets Configuration](#phase-5-github-secrets)
7. [Phase 6: Initial Model Training](#phase-6-initial-training)
8. [Phase 7: Start Applications](#phase-7-start-applications)
9. [Phase 8: Trigger CI/CD Pipeline](#phase-8-cicd-trigger)
10. [Phase 9: Verify Automation](#phase-9-verification)
11. [Troubleshooting Guide](#troubleshooting)
12. [Quick Reference Commands](#quick-reference)

---

<a name="prerequisites"></a>
# 📦 Prerequisites & System Requirements

## What You Need

### Hardware Requirements
- **RAM:** Minimum 8GB (16GB recommended)
- **Storage:** 10GB free space
- **Internet:** Stable broadband connection

### Software to Install

#### 1. **Anaconda Distribution**
- **Windows:** Download from https://www.anaconda.com/download
  - Choose: `Anaconda3-2025.XX-Windows-x86_64.exe`
  - During installation: ✅ Check "Add Anaconda to PATH" (optional but helpful)
- **macOS:** Download from https://www.anaconda.com/download
  - Choose: `Anaconda3-2025.XX-MacOSX-x86_64.pkg` (Intel) or `-arm64.pkg` (Apple Silicon)
  - Install via GUI installer

#### 2. **VS Code (Optional but Recommended)**
- Download from: https://code.visualstudio.com/
- **Windows:** `VSCodeUserSetup-x64-X.XX.X.exe`
- **macOS:** `VSCode-darwin-universal.zip`
- Extensions to install (in VS Code):
  - Python (by Microsoft)
  - Jupyter (by Microsoft)
  - YAML (by Red Hat)

#### 3. **Git**
- **Windows:** Download from https://git-scm.com/download/win
  - Install with default settings
- **macOS:** Git comes pre-installed. Verify with: `git --version`
  - If not installed: `xcode-select --install`

### Account Registrations

#### 1. **GitHub Account**
- Sign up at: https://github.com/signup
- Free tier is sufficient

#### 2. **DagsHub Account**
- Sign up at: https://dagshub.com/user/sign_up
- **Recommended:** Use "Sign up with GitHub" for easier integration

---

<a name="phase-1-github-repository"></a>
# Phase 1: GitHub Repository Setup (10 minutes)

## Step 1.1: Create GitHub Repository

**In Browser:**

1. Go to: https://github.com/new
2. Fill in repository details:
   ```
   Repository name: ml-forecast-system
   Description: Production MLOps Pipeline with DagsHub & MLflow
   Visibility: ✅ Public (for portfolio!)
   
   ❌ Do NOT check:
      - Add a README file
      - Add .gitignore
      - Choose a license
   ```
3. Click **"Create repository"**
4. **Keep this page open** - you'll need the commands

## Step 1.2: Prepare Your Project Files

Your project folder should have this structure:

```
ml-forecast-system/
├── .github/
│   ├── scripts/
│   │   ├── __init__.py
│   │   ├── register_model.py
│   │   └── validate_data.py
│   └── workflows/
│       └── ml-pipeline.yml
├── app/
│   ├── backend.py
│   └── dashboard.py
├── data/
│   ├── raw/
│   └── processed/
├── metrics/
├── models/
│   └── trained/
├── scripts/
│   └── generate_data.py
├── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│   └── utils.py
├── tests/
│   ├── test_preprocess.py
│   ├── test_train.py
│   └── test_utils.py
├── .env.example
├── .gitignore
├── dvc.yaml
├── params.yaml
├── requirements.txt
└── README.md
```

---

## Step 1.3: Initialize Git Repository

### 🪟 **For Windows Users (Anaconda Prompt)**

**Open Anaconda Prompt:**
- Start Menu → Anaconda3 → Anaconda Prompt

```bash
# Navigate to your project folder
cd C:\Users\YourName\Documents\ml-forecast-system

# Verify you're in the right folder
dir

# You should see folders: .github, app, data, src, scripts, etc.
```

### 🍎 **For macOS Users (Terminal)**

**Open Terminal:**
- Spotlight (Cmd + Space) → type "Terminal"

```bash
# Navigate to your project folder
cd ~/Documents/ml-forecast-system

# Verify you're in the right folder
ls -la

# You should see folders: .github, app, data, src, scripts, etc.
```

---

## Step 1.4: Initialize and Push to GitHub

**Commands are identical for Windows & macOS:**

```bash
# Initialize git repository
git init

# Configure git (first time only - use your details)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Stage all files
git add .

# Create initial commit
git commit -m "Initial commit: Complete MLOps starter kit with DagsHub integration"

# Rename branch to main
git branch -M main

# Add remote (replace YOUR_USERNAME with your actual GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/ml-forecast-system.git

# Push to GitHub
git push -u origin main
```

**Expected Output:**
```
Enumerating objects: 150, done.
Counting objects: 100% (150/150), done.
Delta compression using up to 8 threads
Compressing objects: 100% (120/120), done.
Writing objects: 100% (150/150), 85.23 KiB | 4.26 MiB/s, done.
Total 150 (delta 45), reused 0 (delta 0)
To https://github.com/YOUR_USERNAME/ml-forecast-system.git
 * [new branch]      main -> main
```

### ✅ **Checkpoint 1:**
- Refresh your GitHub repository page
- You should see all files uploaded
- Verify `.github/workflows/ml-pipeline.yml` exists

---

<a name="phase-2-dagshub-setup"></a>
# Phase 2: DagsHub Account & Configuration (15 minutes)

## Step 2.1: Create DagsHub Account

**In Browser:**

1. Go to: https://dagshub.com/user/sign_up
2. **Recommended:** Click **"Sign up with GitHub"**
   - This automatically connects your accounts
3. Authorize DagsHub to access your GitHub
4. Complete profile setup

## Step 2.2: Create DagsHub Repository

**In DagsHub Dashboard:**

1. Click **"New Repository"** (top-right, green button)
2. Fill in details:
   ```
   Repository name: ml-forecast-system
   Description: Production MLOps Pipeline with CI/CD
   Visibility: ✅ Public
   
   ❌ Do NOT check:
      - Initialize this repository with a README
   ```
3. Click **"Create Repository"**

## Step 2.3: Connect GitHub Repository to DagsHub

**In DagsHub Repository:**

1. Click **"Settings"** tab (top menu)
2. Click **"Integrations"** (left sidebar)
3. Find **"GitHub Integration"**
4. Click **"Connect to GitHub"**
5. Select repository: `YOUR_USERNAME/ml-forecast-system`
6. Click **"Connect"**

**✅ Result:** Commits to GitHub will automatically appear in DagsHub

## Step 2.4: Generate DagsHub Access Token

**This is critical - follow carefully:**

**In DagsHub:**

1. Click your **profile icon** (top-right corner)
2. Click **"Settings"**
3. Click **"Access Tokens"** (left sidebar)
4. Click **"Generate New Token"**
5. Fill in:
   ```
   Token name: mlops-cicd-pipeline
   Scopes: ✅ Select ALL scopes (or minimum: repo, read:user)
   Expiration: No expiration (or 1 year for practice)
   ```
6. Click **"Generate Token"**

**⚠️ CRITICAL: Copy the token NOW!**

The token looks like: `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

**Save it securely:**
- 🪟 **Windows:** Save in Notepad (don't close the window yet)
- 🍎 **macOS:** Save in TextEdit or Notes
- You'll need this token multiple times

**⚠️ You cannot see this token again after closing the page!**

### ✅ **Checkpoint 2:**
- DagsHub repository created: ✓
- GitHub connected to DagsHub: ✓
- Access token copied and saved: ✓

---

<a name="phase-3-environment-setup"></a>
# Phase 3: Local Environment Setup (20 minutes)

## Step 3.1: Create Conda Environment

### 🪟 **Windows (Anaconda Prompt)**

```bash
# Make sure you're in project directory
cd C:\Users\YourName\Documents\ml-forecast-system

# Create conda environment with Python 3.10
conda create -n mlops python=3.10 -y

# Activate environment
conda activate mlops

# Verify activation (prompt should show: (mlops))
# Check Python version
python --version
# Should show: Python 3.10.x
```

### 🍎 **macOS (Terminal)**

```bash
# Make sure you're in project directory
cd ~/Documents/ml-forecast-system

# Create conda environment with Python 3.10
conda create -n mlops python=3.10 -y

# Activate environment
conda activate mlops

# Verify activation (prompt should show: (mlops))
# Check Python version
python --version
# Should show: Python 3.10.x
```

### 💻 **Alternative: VS Code Terminal**

If you prefer using VS Code terminal:

1. Open VS Code
2. File → Open Folder → Select `ml-forecast-system`
3. Open terminal: View → Terminal (or Ctrl/Cmd + `)
4. Run the same conda commands above

**Note:** First time in VS Code, you may need to:
```bash
# Initialize conda in shell
conda init

# Then close and reopen VS Code terminal
```

---

## Step 3.2: Install Project Dependencies

**With conda environment activated `(mlops)`:**

### 🪟 **Windows**

```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Install all dependencies
pip install -r requirements.txt

# This takes 5-10 minutes - you'll see packages installing
```

### 🍎 **macOS**

```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Install all dependencies
pip install -r requirements.txt

# This takes 5-10 minutes - you'll see packages installing
```

**Expected Output:**
```
Collecting pandas==2.0.3
  Downloading pandas-2.0.3-cp310-cp310-win_amd64.whl (11.6 MB)
Collecting numpy==1.24.3
  Downloading numpy-1.24.3-cp310-cp310-win_amd64.whl (14.8 MB)
...
Successfully installed pandas-2.0.3 numpy-1.24.3 scikit-learn-1.3.0 ...
```

### ✅ **Verify Installation:**

```bash
# Check key packages
pip list | grep mlflow     # macOS/Linux
pip list | findstr mlflow  # Windows

# Should show:
# mlflow         2.8.0
# dvc            3.27.0
# fastapi        0.104.0
# streamlit      1.28.0
```

**All four packages should be listed!**

---

## Step 3.3: Initialize DVC

DVC (Data Version Control) tracks our datasets.

**Commands (same for Windows & macOS):**

```bash
# Initialize DVC
dvc init

# Check DVC status
dvc status

# Expected output:
# Data and pipelines are up to date.
```

**If you see an error:** DVC may already be initialized (that's okay!)

---

### ✅ **Checkpoint 3:**
- Conda environment created: ✓
- All packages installed: ✓
- DVC initialized: ✓

---

<a name="phase-4-dagshub-integration"></a>
# Phase 4: DagsHub Integration (15 minutes)

## Step 4.1: Create .env File

The `.env` file stores your credentials securely.

### 🪟 **Windows Method 1: Using Notepad**

```bash
# Copy example file
copy .env.example .env

# Open in Notepad
notepad .env
```

### 🪟 **Windows Method 2: Using Command Line**

```bash
# Create .env file
type nul > .env

# Edit with VS Code
code .env
```

### 🍎 **macOS Method 1: Using TextEdit**

```bash
# Copy example file
cp .env.example .env

# Open in TextEdit
open -a TextEdit .env
```

### 🍎 **macOS Method 2: Using nano/vim**

```bash
# Copy example file
cp .env.example .env

# Edit with nano (beginner-friendly)
nano .env

# Or use vim (advanced)
vim .env
```

### 💻 **VS Code Method (Windows & macOS)**

```bash
# Copy example
# Windows:
copy .env.example .env

# macOS:
cp .env.example .env

# Open in VS Code
code .env
```

---

## Step 4.2: Configure .env File

**Edit the `.env` file and replace placeholders:**

```bash
# DagsHub Configuration
DAGSHUB_USERNAME=your-actual-dagshub-username
DAGSHUB_TOKEN=ghp_your_actual_token_here
DAGSHUB_REPO=ml-forecast-system

# MLflow Tracking
MLFLOW_TRACKING_URI=https://dagshub.com/your-actual-dagshub-username/ml-forecast-system.mlflow
MLFLOW_TRACKING_USERNAME=your-actual-dagshub-username
MLFLOW_TRACKING_PASSWORD=ghp_your_actual_token_here

# DVC Remote
DVC_REMOTE_URL=https://dagshub.com/your-actual-dagshub-username/ml-forecast-system.dvc

# Auto-reload configuration
AUTO_RELOAD_MODEL=true
AUTO_RELOAD_INTERVAL=30
```

### **Example (with fake credentials):**

```bash
DAGSHUB_USERNAME=amey_trainer
DAGSHUB_TOKEN=ghp_abc123xyz789def456ghi012jkl345mno678
DAGSHUB_REPO=ml-forecast-system

MLFLOW_TRACKING_URI=https://dagshub.com/amey_trainer/ml-forecast-system.mlflow
MLFLOW_TRACKING_USERNAME=amey_trainer
MLFLOW_TRACKING_PASSWORD=ghp_abc123xyz789def456ghi012jkl345mno678

DVC_REMOTE_URL=https://dagshub.com/amey_trainer/ml-forecast-system.dvc

AUTO_RELOAD_MODEL=true
AUTO_RELOAD_INTERVAL=30
```

**⚠️ Important:**
- Replace `amey_trainer` with YOUR DagsHub username
- Replace `ghp_abc123...` with YOUR actual token (from Phase 2.4)
- Keep the `.mlflow` and `.dvc` suffixes in URLs

**Save and close the file.**

---

## Step 4.3: Configure DVC Remote

**In Terminal/Anaconda Prompt (with `mlops` environment active):**

### 🪟 **Windows**

```bash
# Remove any existing remote
dvc remote remove origin 2>nul

# Add DagsHub remote (replace YOUR_USERNAME)
dvc remote add origin https://dagshub.com/YOUR_USERNAME/ml-forecast-system.dvc

# Set as default
dvc remote default origin

# Configure authentication
dvc remote modify origin --local auth basic
dvc remote modify origin --local user YOUR_USERNAME
dvc remote modify origin --local password YOUR_TOKEN

# Test connection
dvc push

# Expected: "Everything is up to date." (since no data yet)
```

### 🍎 **macOS**

```bash
# Remove any existing remote
dvc remote remove origin 2>/dev/null

# Add DagsHub remote (replace YOUR_USERNAME)
dvc remote add origin https://dagshub.com/YOUR_USERNAME/ml-forecast-system.dvc

# Set as default
dvc remote default origin

# Configure authentication
dvc remote modify origin --local auth basic
dvc remote modify origin --local user YOUR_USERNAME
dvc remote modify origin --local password YOUR_TOKEN

# Test connection
dvc push

# Expected: "Everything is up to date." (since no data yet)
```

**Replace:**
- `YOUR_USERNAME` → Your DagsHub username
- `YOUR_TOKEN` → Your DagsHub token

---

## Step 4.4: Generate and Track Dataset

**Generate synthetic sales data:**

### 🪟 **Windows**

```bash
# Generate 1065 days of data (3 years)
python scripts/generate_data.py --n-days 1065

# You should see:
# ✓ Generated 1065 days of sales data
# Date range: 2023-01-01 to 2025-10-31
# Sales range: $xx.xx to $xxx.xx
# ✓ Data saved to: data/raw/sales_data.csv

# Verify file exists
dir data\raw\sales_data.csv
```

### 🍎 **macOS**

```bash
# Generate 1065 days of data (3 years)
python scripts/generate_data.py --n-days 1065

# You should see:
# ✓ Generated 1065 days of sales data
# Date range: 2023-01-01 to 2025-10-31
# Sales range: $xx.xx to $xxx.xx
# ✓ Data saved to: data/raw/sales_data.csv

# Verify file exists
ls -lh data/raw/sales_data.csv
```

---

## Step 4.5: Track Dataset with DVC

**Track the dataset with DVC:**

```bash
# Add data file to DVC tracking
dvc add data/raw/sales_data.csv

# This creates: data/raw/sales_data.csv.dvc (metadata file)

# Add metadata to Git
git add data/raw/sales_data.csv.dvc data/raw/.gitignore

# Commit
git commit -m "Track sales dataset with DVC"

# Push data to DagsHub DVC storage
dvc push

# Expected output:
# 1 file pushed

# Push Git metadata to GitHub
git push origin main
```

**Expected Output from `dvc push`:**
```
Collecting                                                          
Pushing to remote 'origin'
1 file pushed
```

### ✅ **Checkpoint 4:**
- .env file configured: ✓
- DVC remote connected: ✓
- Dataset generated: ✓
- Data tracked with DVC: ✓
- Data pushed to DagsHub: ✓

**Verify in Browser:**
- Go to: `https://dagshub.com/YOUR_USERNAME/ml-forecast-system`
- Click **"Data"** tab
- You should see `sales_data.csv`

---

<a name="phase-5-github-secrets"></a>
# Phase 5: GitHub Secrets Configuration (5 minutes)

GitHub Actions needs your DagsHub credentials to run the pipeline.

## Step 5.1: Add Repository Secrets

**In Browser:**

1. Go to: `https://github.com/YOUR_USERNAME/ml-forecast-system`
2. Click **"Settings"** tab (far right in menu)
3. Click **"Secrets and variables"** → **"Actions"** (left sidebar)
4. Click **"New repository secret"** (green button)

---

## Step 5.2: Add Secret 1 - DAGSHUB_USERNAME

**Add First Secret:**

```
Name: DAGSHUB_USERNAME
Value: your-dagshub-username
```

Example:
```
Name: DAGSHUB_USERNAME
Value: amey_trainer
```

Click **"Add secret"**

---

## Step 5.3: Add Secret 2 - DAGSHUB_TOKEN

**Click "New repository secret" again:**

```
Name: DAGSHUB_TOKEN
Value: ghp_your_actual_token_here
```

Example:
```
Name: DAGSHUB_TOKEN
Value: ghp_abc123xyz789def456ghi012jkl345mno678
```

Click **"Add secret"**

---

### ✅ **Checkpoint 5:**

**In GitHub Secrets page, you should see:**

| Name | Updated |
|------|---------|
| DAGSHUB_TOKEN | now |
| DAGSHUB_USERNAME | now |

Values are hidden for security (that's correct!)

---

<a name="phase-6-initial-training"></a>
# Phase 6: Initial Model Training (10 minutes)

Before triggering CI/CD, let's train a model locally to verify everything works.

## Step 6.1: Preprocess Data

**In Terminal/Anaconda Prompt (with `mlops` environment):**

### 🪟 **Windows**

```bash
# Ensure you're in project root
cd C:\Users\YourName\Documents\ml-forecast-system

# Activate environment if not active
conda activate mlops

# Run preprocessing
python src/preprocess.py
```

### 🍎 **macOS**

```bash
# Ensure you're in project root
cd ~/Documents/ml-forecast-system

# Activate environment if not active
conda activate mlops

# Run preprocessing
python src/preprocess.py
```

**Expected Output:**
```
Loading raw data from data/raw/sales_data.csv
✓ Data loaded: 1065 rows, 7 columns

Feature Engineering:
✓ Created date features
✓ Created lag features

Train/Test Split (80/20):
✓ Train set: 852 samples (80.0%)
✓ Test set: 213 samples (20.0%)

✓ Processed data saved:
  - data/processed/train.csv
  - data/processed/test.csv

Preprocessing complete in 2.34 seconds
```

---

## Step 6.2: Train Model

**Train the model (this will log to DagsHub MLflow):**

```bash
# Train model
python src/train.py
```

**Expected Output:**
```
========================================
Starting Model Training Pipeline
========================================

MLflow Configuration:
  Tracking URI: https://dagshub.com/YOUR_USERNAME/ml-forecast-system.mlflow
  Experiment: sales-forecaster-dev

Loading training data...
✓ Training data loaded: 852 samples

Model Configuration:
  Type: RandomForestRegressor
  n_estimators: 100
  max_depth: 10
  random_state: 42

Training model...
✓ Model trained in 3.45 seconds

Model Performance:
  MAE (Mean Absolute Error): 4.92
  RMSE (Root Mean Squared Error): 7.01
  R² Score: 0.89
  MAPE: 3.45%

✓ Model saved: models/trained/model.pkl
✓ Metrics saved: metrics/train_metrics.json
✓ MLflow Run ID: abc123def456...

========================================
✅ Training Complete!
========================================

View experiment: https://dagshub.com/YOUR_USERNAME/ml-forecast-system/experiments
```

---

## Step 6.3: Verify MLflow Logging

**In Browser:**

1. Go to: `https://dagshub.com/YOUR_USERNAME/ml-forecast-system/experiments`
2. You should see:
   - Experiment: `sales-forecaster-dev`
   - 1 run with metrics (MAE, RMSE, R²)
   - Parameters (max_depth, n_estimators)

**🎉 If you see this, MLflow integration works!**

---

### ✅ **Checkpoint 6:**
- Data preprocessed: ✓
- Model trained locally: ✓
- Metrics logged to DagsHub: ✓
- Model file created: ✓

---

<a name="phase-7-start-applications"></a>
# Phase 7: Start Applications (15 minutes)

Now we'll start the backend API and dashboard.

## Overview

You need **THREE terminal windows/tabs running simultaneously:**

1. **Terminal 1:** Backend API (FastAPI)
2. **Terminal 2:** Dashboard (Streamlit)
3. **Terminal 3:** Commands (optional, for git operations)

---

## Setup Options

### **Option A: Using Anaconda Prompt (Recommended for Beginners)**

### 🪟 **Windows**

**Terminal 1 - Backend:**
1. Open Anaconda Prompt (Window 1)
2. Run:
```bash
cd C:\Users\YourName\Documents\ml-forecast-system
conda activate mlops
cd app
uvicorn backend:app --reload --port 5000
```

**Terminal 2 - Dashboard:**
1. Open ANOTHER Anaconda Prompt (Window 2)
2. Run:
```bash
cd C:\Users\YourName\Documents\ml-forecast-system
conda activate mlops
streamlit run app/dashboard.py
```

### 🍎 **macOS**

**Terminal 1 - Backend:**
1. Open Terminal (Window 1)
2. Run:
```bash
cd ~/Documents/ml-forecast-system
conda activate mlops
cd app
uvicorn backend:app --reload --port 5000
```

**Terminal 2 - Dashboard:**
1. Open ANOTHER Terminal (Window 2: Cmd+N)
2. Run:
```bash
cd ~/Documents/ml-forecast-system
conda activate mlops
streamlit run app/dashboard.py
```

---

### **Option B: Using VS Code (Recommended for Advanced Users)**

**Open VS Code:**

1. File → Open Folder → Select `ml-forecast-system`
2. Open Terminal: View → Terminal (Ctrl/Cmd + `)

**Terminal 1 - Backend:**
```bash
# In VS Code terminal
conda activate mlops
cd app
uvicorn backend:app --reload --port 5000
```

**Terminal 2 - Dashboard:**
- Click **"+"** icon in terminal panel (creates new terminal)
```bash
conda activate mlops
streamlit run app/dashboard.py
```

**Terminal 3 - Commands:**
- Click **"+"** again (for git operations later)
```bash
conda activate mlops
```

---

## Step 7.1: Start Backend API

**In Terminal 1:**

### 🪟 **Windows**
```bash
cd C:\Users\YourName\Documents\ml-forecast-system
conda activate mlops
cd app
uvicorn backend:app --reload --port 5000
```

### 🍎 **macOS**
```bash
cd ~/Documents/ml-forecast-system
conda activate mlops
cd app
uvicorn backend:app --reload --port 5000
```

**Expected Output:**
```
INFO:     Will watch for changes in these directories: ['C:\\Users\\...\\app']
INFO:     Uvicorn running on http://127.0.0.1:5000 (Press CTRL+C to quit)
INFO:     Started reloader process [12345] using WatchFiles
INFO:     Started server process [67890]
INFO:     Waiting for application startup.
🚀 Starting Sales Forecaster API...
🔗 Connecting to MLflow: https://dagshub.com/YOUR_USERNAME/ml-forecast-system.mlflow
📥 Loading model: models:/sales-forecaster/Production
⚠️  No Production model found
Loading from local file...
✅ Model loaded from: ..\models\trained\model.pkl
✅ Auto-reload thread started (checking every 30s)
✅ Sales Forecaster API ready!
INFO:     Application startup complete.
```

**Note:** "No Production model found" is NORMAL on first run. We'll register a model via CI/CD.

**✅ Backend is running when you see:**
```
INFO:     Application startup complete.
✅ Sales Forecaster API ready!
```

**Test Backend:**
- Open browser: http://localhost:5000
- You should see JSON response with API info

---

## Step 7.2: Start Dashboard

**In Terminal 2 (NEW window/tab):**

### 🪟 **Windows**
```bash
cd C:\Users\YourName\Documents\ml-forecast-system
conda activate mlops
streamlit run app/dashboard.py
```

### 🍎 **macOS**
```bash
cd ~/Documents/ml-forecast-system
conda activate mlops
streamlit run app/dashboard.py
```

**Expected Output:**
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

**Dashboard should automatically open in browser!**

**If it doesn't open automatically:**
- Manually go to: http://localhost:8501

---

## Step 7.3: Verify Dashboard

**In Browser (http://localhost:8501):**

You should see:

### **Dashboard Components:**

1. **Header:**
   - 📊 Sales Forecasting Dashboard
   - Production ML System - Real-time Predictions

2. **Sidebar:**
   - 🔌 API Status: ✅ Connected
   - 🔄 Auto-Reload Status: ✅ Backend Auto-Reload: ON
   - 🔄 Dashboard Settings: Auto-refresh Dashboard (checked)

3. **Main Panel:**
   - 🎯 Model Information
     - Model Version: Local File (will change to v1 after CI/CD)
     - Status: 🟡 Local
     - Auto-Reload: ✅ ON
   
   - 📊 Model Performance Metrics
     - MAE: ~4.92
     - RMSE: ~7.01
     - R² Score: ~0.890
   
   - 📈 7-Day Sales Forecast (line chart)
   
   - 🔮 Make a Custom Prediction (form)

---

## Step 7.4: Test Prediction

**In Dashboard:**

1. Scroll to **"Make a Custom Prediction"**
2. Enter values:
   ```
   Advertising Spend: 3000
   Promotions: Yes
   Day of Week: Monday
   Month: January
   Is Weekend: No
   ```
3. Click **"🚀 Get Prediction"**

**Expected Result:**
```
✅ Prediction Complete!

Predicted Sales: $142.35
Confidence: 85%
Model Version: Local File
```

**🎉 If prediction works, everything is set up correctly!**

---

### ✅ **Checkpoint 7:**

**Three things running:**
- ✅ Backend: http://localhost:5000 (shows JSON)
- ✅ Dashboard: http://localhost:8501 (shows UI)
- ✅ Predictions work: Input → Prediction → Result

**Keep both terminals running!** Don't close them.

---

<a name="phase-8-cicd-trigger"></a>
# Phase 8: Trigger CI/CD Pipeline (20 minutes)

Now for the magic! We'll make a code change and watch full automation.

## Step 8.1: Make a Code Change

**Open a new terminal (Terminal 3) or use VS Code:**

### 🪟 **Windows - Using Notepad**

```bash
# Open params.yaml in Notepad
notepad params.yaml
```

### 🍎 **macOS - Using TextEdit**

```bash
# Open params.yaml in TextEdit
open -a TextEdit params.yaml
```

### 💻 **Using VS Code**

```bash
# Open in VS Code
code params.yaml
```

---

**In params.yaml, find this section:**

```yaml
train:
  model_type: RandomForestRegressor
  n_estimators: 100
  max_depth: 10        # ← CHANGE THIS LINE
  min_samples_split: 2
  random_state: 42
```

**Change to:**

```yaml
train:
  model_type: RandomForestRegressor
  n_estimators: 100
  max_depth: 15        # ← CHANGED from 10 to 15
  min_samples_split: 2
  random_state: 42
```

**Save the file (Ctrl+S / Cmd+S)**

---

## Step 8.2: Commit and Push

**In Terminal 3 (or new Anaconda Prompt/Terminal):**

### 🪟 **Windows**

```bash
cd C:\Users\YourName\Documents\ml-forecast-system
conda activate mlops

# Check what changed
git status

# You should see: modified: params.yaml

# Add the change
git add params.yaml

# Commit with descriptive message
git commit -m "Experiment 1: Increase max_depth to 15 for better accuracy"

# Push to GitHub (this triggers CI/CD!)
git push origin main
```

### 🍎 **macOS**

```bash
cd ~/Documents/ml-forecast-system
conda activate mlops

# Check what changed
git status

# You should see: modified: params.yaml

# Add the change
git add params.yaml

# Commit with descriptive message
git commit -m "Experiment 1: Increase max_depth to 15 for better accuracy"

# Push to GitHub (this triggers CI/CD!)
git push origin main
```

**Expected Output:**
```
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 345 bytes | 345.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0)
To https://github.com/YOUR_USERNAME/ml-forecast-system.git
   abc1234..def5678  main -> main
```

**🚀 CI/CD Pipeline has started!**

---

## Step 8.3: Watch Pipeline Execute

**In Browser - Open 3 Tabs:**

### **Tab 1: GitHub Actions**

URL: `https://github.com/YOUR_USERNAME/ml-forecast-system/actions`

You should see:
- **Workflow:** "ML Training & Deployment Pipeline with DagsHub"
- **Status:** 🟡 In progress (yellow circle)
- **Trigger:** "Experiment 1: Increase max_depth..."

**Click on the workflow run to see details**

---

### **Tab 2: DagsHub Experiments**

URL: `https://dagshub.com/YOUR_USERNAME/ml-forecast-system/experiments`

You should see:
- New experiment run appearing (may take 2-3 minutes)
- Experiment: `sales-forecaster-production`
- Parameters: max_depth = 15
- Metrics being logged in real-time

---

### **Tab 3: Dashboard**

URL: http://localhost:8501

Keep this open - it will auto-update after pipeline completes!

---

## Step 8.4: Pipeline Stages (Expected Timeline)

Watch GitHub Actions - you'll see 6 jobs running in sequence:

### **Job 1: 🔍 Code Quality & Tests** (~2 min)
```
✅ Checkout code
✅ Setup Python
✅ Install dependencies
✅ Check code formatting (Black)
✅ Lint code (Flake8)
✅ Run unit tests
```

### **Job 2: 📊 Data Validation** (~3 min)
```
✅ Checkout code
✅ Setup Python
✅ Configure DVC
✅ Pull data from DagsHub
✅ Validate data quality
```

### **Job 3: 🎓 Train Model** (~5-10 min) ⭐ **MOST IMPORTANT**
```
✅ Checkout code
✅ Setup Python
✅ Configure DVC
✅ Pull data
✅ Preprocess data
✅ Train model with MLflow
   - Training with max_depth=15
   - Logging to DagsHub MLflow
   - MAE: ~4.68 (improved!)
✅ Upload trained model
```

### **Job 4: 📊 Evaluate Model** (~2 min)
```
✅ Download trained model
✅ Get test data
✅ Evaluate performance
✅ Compare with baseline
✅ Decision: APPROVE DEPLOYMENT ✓
```

### **Job 5: 📦 Register Model in MLflow** (~1 min) ⭐ **KEY STEP**
```
✅ Connect to DagsHub MLflow
✅ Register model: sales-forecaster
✅ Version: 1
✅ Promote to Production stage
✅ Archive previous versions
```

### **Job 6: 🎉 Deployment Complete** (~1 min)
```
✅ Print summary
✅ Show links to DagsHub
✅ Pipeline finished successfully!
```

**Total Pipeline Time: ~15-20 minutes**

---

## Step 8.5: Monitor Progress in Real-Time

**In GitHub Actions (Tab 1):**

Click on each job to see live logs:

**Example - Train Model logs:**
```
Run python src/train.py
========================================
Starting Model Training Pipeline
========================================
MLflow Configuration:
  Tracking URI: https://dagshub.com/YOUR_USERNAME/ml-forecast-system.mlflow
  Experiment: sales-forecaster-production

Training model...
✓ Model trained in 4.23 seconds

Model Performance:
  MAE: 4.68
  RMSE: 6.85
  R² Score: 0.90

✓ Model saved
✓ Metrics logged to MLflow
========================================
✅ Training Complete!
========================================
```

---

## Step 8.6: Verify Model Registration

**When Job 5 completes, check DagsHub Model Registry:**

**In Browser:**

URL: `https://dagshub.com/YOUR_USERNAME/ml-forecast-system.mlflow/#/models/sales-forecaster`

You should see:

```
Model: sales-forecaster
Version: 1
Stage: Production
Source Run: abc123def...
Created: just now
```

**🎉 Model is now in Production!**

---

### ✅ **Checkpoint 8:**

**All 6 jobs completed:**
- ✅ Code Quality
- ✅ Data Validation
- ✅ Train Model
- ✅ Evaluate Model
- ✅ Register Model ⭐
- ✅ Deployment Complete

**Model registered in MLflow Registry:**
- ✅ Version: 1
- ✅ Stage: Production

---

<a name="phase-9-verification"></a>
# Phase 9: Verify Automation (10 minutes)

## Step 9.1: Watch Backend Auto-Reload

**In Backend Terminal (Terminal 1):**

After pipeline completes (~2 minutes), you should see:

```
🆕 New model version detected!
   Current: Local File
   Latest: v1
🔄 Auto-reloading model...
✅ Model auto-reloaded to version v1!
   Run ID: abc123def456...
```

**This happens automatically every 30 seconds!**

**If you don't see it yet:** Wait 30 more seconds (backend checks every 30s)

---

## Step 9.2: Watch Dashboard Update

**In Browser - Dashboard Tab (http://localhost:8501):**

After backend reloads (~30 seconds after that), dashboard will auto-refresh.

**You should see changes:**

### **Before (old):**
```
Model Version: Local File
Status: 🟡 Local
MAE: 4.92
RMSE: 7.01
R² Score: 0.890
```

### **After (new):** ✨
```
Model Version: v1
Status: 🟢 Active
MAE: 4.68  (with delta: -4.9% ↓)
RMSE: 6.85 (with delta: -2.3% ↓)
R² Score: 0.900 (with delta: +1.1% ↑)
```

**🎉 The metrics improved! Model is better!**

---

## Step 9.3: Test New Predictions

**In Dashboard:**

1. Scroll to **"Make a Custom Prediction"**
2. Enter same values as before:
   ```
   Advertising Spend: 3000
   Promotions: Yes
   Day of Week: Monday
   Month: January
   Is Weekend: No
   ```
3. Click **"🚀 Get Prediction"**

**New Result:**
```
✅ Prediction Complete!

Predicted Sales: $145.82  ← Different from before!
Confidence: 85%
Model Version: v1  ← Changed from "Local File"!
```

**Prediction changed because we're now using the new model!**

---

## Step 9.4: Verify Complete Automation

**Let's recap what happened automatically:**

1. ✅ You changed ONE line in `params.yaml`
2. ✅ Pushed to GitHub
3. ✅ GitHub Actions automatically:
   - Validated code
   - Trained new model
   - Evaluated performance
   - Registered in MLflow Registry
   - Promoted to Production
4. ✅ Backend automatically:
   - Detected new model (30s polling)
   - Reloaded model
5. ✅ Dashboard automatically:
   - Refreshed (30s polling)
   - Showed new metrics
   - Served new predictions

**🎊 ZERO MANUAL STEPS AFTER GIT PUSH!**

---

## Step 9.5: View Complete Pipeline History

### **GitHub Actions History**

URL: `https://github.com/YOUR_USERNAME/ml-forecast-system/actions`

Shows:
- All pipeline runs
- Success/failure status
- Time taken for each run

### **DagsHub Experiments**

URL: `https://dagshub.com/YOUR_USERNAME/ml-forecast-system/experiments`

Shows:
- All training runs
- Parameters for each run
- Metrics comparison
- Git commit links

### **DagsHub Model Registry**

URL: `https://dagshub.com/YOUR_USERNAME/ml-forecast-system.mlflow/#/models`

Shows:
- Model: sales-forecaster
- Version 1 (Production)
- Can promote/archive versions

---

### ✅ **Checkpoint 9:**

**Complete automation verified:**
- ✅ Backend auto-reloaded new model
- ✅ Dashboard auto-refreshed
- ✅ New predictions served
- ✅ Metrics updated with real deltas
- ✅ Zero manual intervention

**🎉 YOU HAVE A PRODUCTION MLOPS PIPELINE!**

---

<a name="troubleshooting"></a>
# 🔧 Troubleshooting Guide

## Common Issues & Solutions

### Issue 1: Cannot Activate Conda Environment

**Symptom:**
```
'conda' is not recognized as an internal or external command
```

**Solution - Windows:**
```bash
# Initialize conda for command line
C:\Users\YourName\anaconda3\Scripts\conda.exe init

# Close and reopen Anaconda Prompt
# Then try: conda activate mlops
```

**Solution - macOS:**
```bash
# Initialize conda
source ~/anaconda3/bin/activate
conda init zsh  # or: conda init bash

# Close and reopen Terminal
# Then try: conda activate mlops
```

---

### Issue 2: DVC Push Fails

**Symptom:**
```
ERROR: failed to push data to the remote
```

**Solution:**
```bash
# Re-configure DVC remote
dvc remote modify origin --local user YOUR_USERNAME
dvc remote modify origin --local password YOUR_TOKEN

# Verify credentials in .env file
# Windows:
type .env

# macOS:
cat .env

# Try push again
dvc push
```

---

### Issue 3: Backend Cannot Connect to MLflow

**Symptom:**
```
❌ Failed to load from MLflow Registry
Loading from local file...
```

**Solution:**
```bash
# Check .env file exists and has correct values
# Windows:
dir .env
type .env

# macOS:
ls -la .env
cat .env

# Verify MLFLOW_TRACKING_URI format:
# Should be: https://dagshub.com/USERNAME/REPO.mlflow

# Restart backend:
# Ctrl+C to stop
uvicorn app.backend:app --reload --port 5000
```

---

### Issue 4: GitHub Actions Fails

**Symptom:** Red X on GitHub Actions

**Solution:**

1. Click on failed job
2. Read error message
3. Common fixes:

**Missing Secrets:**
```
Go to: GitHub Repo → Settings → Secrets → Actions
Add: DAGSHUB_USERNAME and DAGSHUB_TOKEN
```

**DVC Pull Fails:**
```
Check DVC remote is configured correctly
Verify DagsHub token is valid
```

**Model Registration Fails:**
```
Check MLflow experiment exists in DagsHub
Verify model was trained successfully
```

---

### Issue 5: Dashboard Shows "Cannot Connect to API"

**Symptom:**
```
❌ Cannot connect to API
Start backend: uvicorn app.backend:app --reload --port 5000
```

**Solution:**

**Check if backend is running:**

Windows:
```bash
netstat -ano | findstr :5000
```

macOS:
```bash
lsof -i :5000
```

**If nothing shown, start backend:**
```bash
cd app
uvicorn backend:app --reload --port 5000
```

**If port is used by another process:**
```bash
# Use different port
uvicorn backend:app --reload --port 5002

# Update dashboard API_URL in app/dashboard.py:
API_URL = "http://localhost:5002"
```

---

### Issue 6: Model Not Auto-Reloading

**Symptom:** Dashboard still shows "Local File" after CI/CD

**Solution:**

```bash
# Check backend logs for auto-reload messages
# Should see every 30s:
# 🔄 Auto-reload enabled: checking every 30s

# If not seeing this:
# 1. Check .env file
type .env  # Windows
cat .env   # macOS

# Should have:
# AUTO_RELOAD_MODEL=true
# AUTO_RELOAD_INTERVAL=30

# 2. Restart backend
# Ctrl+C
uvicorn app.backend:app --reload --port 5000

# 3. Manually reload via API
# In browser: http://localhost:5000/model/reload
```

---

### Issue 7: Python Version Mismatch

**Symptom:**
```
ERROR: Package requires a different Python: 3.x.x not in '>=3.10'
```

**Solution:**
```bash
# Check Python version
python --version

# If not 3.10, recreate environment
conda deactivate
conda env remove -n mlops
conda create -n mlops python=3.10 -y
conda activate mlops
pip install -r requirements.txt
```

---

### Issue 8: Git Push Requires Authentication

**Symptom:**
```
Username for 'https://github.com':
```

**Solution:**

**Use GitHub Personal Access Token:**

1. GitHub → Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Select scopes: `repo`
4. Copy token

**Configure git to use token:**

Windows:
```bash
git config --global credential.helper wincred
git push origin main
# Username: YOUR_GITHUB_USERNAME
# Password: ghp_YOUR_TOKEN
```

macOS:
```bash
git config --global credential.helper osxkeychain
git push origin main
# Username: YOUR_GITHUB_USERNAME
# Password: ghp_YOUR_TOKEN
```

---

### Issue 9: Streamlit Port Already in Use

**Symptom:**
```
OSError: [Errno 48] Address already in use
```

**Solution:**

Windows:
```bash
# Kill process on port 8501
netstat -ano | findstr :8501
taskkill /PID <PID> /F

# Or use different port
streamlit run app/dashboard.py --server.port 8502
```

macOS:
```bash
# Kill process on port 8501
lsof -ti:8501 | xargs kill -9

# Or use different port
streamlit run app/dashboard.py --server.port 8502
```

---

### Issue 10: Metrics Show 0.00

**Symptom:** Dashboard shows MAE: 0.00, RMSE: 0.00, R²: 0.00

**Solution:**

**Check if model has metrics in MLflow:**

```bash
# Run diagnostic script
python
```

```python
import mlflow
from mlflow.tracking import MlflowClient
from dotenv import load_dotenv

load_dotenv()

client = MlflowClient()
model_name = "sales-forecaster"

# Get Production model
versions = client.get_latest_versions(model_name, stages=["Production"])

if versions:
    run_id = versions[0].run_id
    run = mlflow.get_run(run_id)
    
    print("Metrics from run:")
    for key, value in run.data.metrics.items():
        print(f"  {key}: {value}")
else:
    print("No Production model found")

exit()
```

**If no metrics found:**
```bash
# Re-train and register
python src/train.py
python .github/scripts/register_model.py <RUN_ID>

# Restart backend
```

---

<a name="quick-reference"></a>
# 📚 Quick Reference Commands

## Daily Workflow

### Start Work Session

**Windows:**
```bash
cd C:\Users\YourName\Documents\ml-forecast-system
conda activate mlops
```

**macOS:**
```bash
cd ~/Documents/ml-forecast-system
conda activate mlops
```

### Start Services

**Terminal 1 - Backend:**
```bash
conda activate mlops
cd app
uvicorn backend:app --reload --port 5000
```

**Terminal 2 - Dashboard:**
```bash
conda activate mlops
streamlit run app/dashboard.py
```

### Make Changes & Deploy

```bash
# 1. Edit code (e.g., params.yaml)
# 2. Commit and push
git add .
git commit -m "Experiment X: description"
git push origin main

# 3. Wait for automation (~15-20 min)
# 4. Backend auto-reloads (~30s after pipeline)
# 5. Dashboard auto-refreshes (~30s after backend)
```

---

## Useful Commands

### Check Status

```bash
# Git status
git status

# DVC status
dvc status

# Conda environment
conda env list
conda list

# Check running processes
# Windows:
netstat -ano | findstr :5000
netstat -ano | findstr :8501

# macOS:
lsof -i :5000
lsof -i :8501
```

### Update Code

```bash
# Pull latest changes
git pull origin main

# Update dependencies
pip install -r requirements.txt --upgrade

# Pull data
dvc pull
```

### Clean Up

```bash
# Stop services: Ctrl+C in terminals

# Deactivate conda
conda deactivate

# Remove environment (if needed)
conda env remove -n mlops
```

---

## Important URLs

### Local Applications
- **Backend API:** http://localhost:5000
- **API Docs:** http://localhost:5000/docs
- **Dashboard:** http://localhost:8501

### DagsHub (replace YOUR_USERNAME)
- **Repository:** https://dagshub.com/YOUR_USERNAME/ml-forecast-system
- **Experiments:** https://dagshub.com/YOUR_USERNAME/ml-forecast-system/experiments
- **Model Registry:** https://dagshub.com/YOUR_USERNAME/ml-forecast-system.mlflow/#/models
- **Data:** https://dagshub.com/YOUR_USERNAME/ml-forecast-system/data

### GitHub (replace YOUR_USERNAME)
- **Repository:** https://github.com/YOUR_USERNAME/ml-forecast-system
- **Actions:** https://github.com/YOUR_USERNAME/ml-forecast-system/actions
- **Settings:** https://github.com/YOUR_USERNAME/ml-forecast-system/settings

---

## Environment Variables (.env)

```bash
# DagsHub
DAGSHUB_USERNAME=your-username
DAGSHUB_TOKEN=ghp_your_token
DAGSHUB_REPO=ml-forecast-system

# MLflow
MLFLOW_TRACKING_URI=https://dagshub.com/your-username/ml-forecast-system.mlflow
MLFLOW_TRACKING_USERNAME=your-username
MLFLOW_TRACKING_PASSWORD=ghp_your_token

# DVC
DVC_REMOTE_URL=https://dagshub.com/your-username/ml-forecast-system.dvc

# Auto-reload
AUTO_RELOAD_MODEL=true
AUTO_RELOAD_INTERVAL=30
```

---

## File Structure Reference

```
ml-forecast-system/
├── .github/workflows/ml-pipeline.yml    # CI/CD pipeline
├── .github/scripts/                     # Helper scripts
├── app/
│   ├── backend.py                       # FastAPI backend
│   └── dashboard.py                     # Streamlit dashboard
├── data/
│   ├── raw/sales_data.csv              # Original data (DVC tracked)
│   └── processed/                       # Train/test splits
├── models/trained/model.pkl             # Local model
├── src/
│   ├── preprocess.py                    # Data preprocessing
│   ├── train.py                         # Model training
│   └── evaluate.py                      # Model evaluation
├── scripts/generate_data.py             # Data generation
├── .env                                 # Credentials (DO NOT COMMIT)
├── params.yaml                          # Model hyperparameters
└── requirements.txt                     # Python dependencies
```

---

# 🎓 Learning Outcomes

After completing this guide, you will have:

## Technical Skills ✅
- Set up complete MLOps pipeline
- Integrated MLflow for experiment tracking
- Configured DVC for data versioning
- Implemented CI/CD with GitHub Actions
- Created auto-reloading backend API
- Built real-time dashboard with Streamlit

## DevOps Practices ✅
- Infrastructure as Code (IaC)
- Continuous Integration/Continuous Deployment (CI/CD)
- Automated testing and validation
- Model registry and versioning
- Monitoring and observability

## Portfolio Project ✅
- Production-grade MLOps system
- Fully automated pipeline
- Professional documentation
- Demonstrable in interviews
- Public GitHub + DagsHub repositories

---

# 🚀 Next Steps

## Experiment Ideas

1. **Hyperparameter Tuning:**
   ```yaml
   # Try different values in params.yaml
   max_depth: 5, 10, 15, 20, 25
   n_estimators: 50, 100, 150, 200
   ```

2. **Feature Engineering:**
   - Add moving averages
   - Create holiday indicators
   - Include weather data

3. **Model Comparison:**
   - Try XGBoost
   - Try LightGBM
   - Compare with ensemble methods

## Advanced Topics

- **Docker:** Containerize applications
- **Kubernetes:** Orchestrate deployments
- **Monitoring:** Add Prometheus & Grafana
- **A/B Testing:** Multi-model serving
- **LLMOps:** Apply same patterns to LLM projects

---

# 📞 Support & Resources

## Documentation
- **MLflow:** https://mlflow.org/docs/latest/
- **DVC:** https://dvc.org/doc
- **FastAPI:** https://fastapi.tiangolo.com/
- **Streamlit:** https://docs.streamlit.io/

## Community
- **MLOps Community:** https://mlops.community/
- **GitHub Discussions:** Use your repo's Discussions tab
- **Stack Overflow:** Tag `mlops`, `mlflow`, `dvc`

---

# 🎉 Congratulations!

You've built a **production-grade MLOps pipeline** with:

✅ Automated training  
✅ Model versioning  
✅ CI/CD deployment  
✅ Real-time monitoring  
✅ Auto-reloading backend  
✅ Interactive dashboard  

**This is what top tech companies use!**

Share your achievement:
- LinkedIn post with screenshots
- GitHub README with badges
- DagsHub experiments visualization
- Add to resume/portfolio

---

**Version:** 1.0  
**Last Updated:** November 2025

---

**Keep experimenting, keep learning, keep building! 🚀**

---