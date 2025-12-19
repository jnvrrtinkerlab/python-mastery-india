# 🚀 Setup Guide - Get Started in Minutes!

## Prerequisites

Before you begin, make sure you have:

- **Python 3.8 or higher** installed
- **A code editor** (VS Code, PyCharm, or similar)
- **Git** for version control
- **About 30 minutes** to set up

## Windows Setup

### Step 1: Install Python

1. Visit [python.org](https://python.org)
2. Download Python 3.10 or higher
3. Run the installer
4. **IMPORTANT**: Check "Add Python to PATH"
5. Click "Install Now"

### Step 2: Verify Installation

```bash
python --version
pip --version
```

Both should show version numbers.

### Step 3: Clone This Repository

```bash
git clone https://github.com/jnvrrtinkerlab/python-mastery-india.git
cd python-mastery-india
```

### Step 4: Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

### Step 5: Install Requirements

```bash
pip install -r requirements.txt
```

### Step 6: Run Your First Program!

```bash
cd phase_01_basics
python lesson_01_hello_world.py
```

---

## Mac Setup

### Step 1: Install Python

```bash
# Using Homebrew (recommended)
brew install python3

# Or visit python.org and download installer
```

### Step 2: Verify Installation

```bash
python3 --version
pip3 --version
```

### Step 3: Clone Repository

```bash
git clone https://github.com/jnvrrtinkerlab/python-mastery-india.git
cd python-mastery-india
```

### Step 4: Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 5: Install Requirements

```bash
pip install -r requirements.txt
```

### Step 6: Run Your First Program

```bash
cd phase_01_basics
python3 lesson_01_hello_world.py
```

---

## Linux Setup

### Step 1: Install Python

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### Step 2: Verify Installation

```bash
python3 --version
pip3 --version
```

### Step 3: Clone Repository

```bash
git clone https://github.com/jnvrrtinkerlab/python-mastery-india.git
cd python-mastery-india
```

### Step 4: Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 5: Install Requirements

```bash
pip install -r requirements.txt
```

### Step 6: Run Your First Program

```bash
cd phase_01_basics
python3 lesson_01_hello_world.py
```

---

## Code Editor Setup

### VS Code (Recommended)

1. Download from [code.visualstudio.com](https://code.visualstudio.com)
2. Install the Python extension
3. Open this repository in VS Code
4. Select Python interpreter from virtual environment

### PyCharm

1. Download Community Edition from [jetbrains.com](https://jetbrains.com/pycharm)
2. Open this repository
3. Configure Python interpreter
4. Start coding!

### Replit (Online - No Installation Needed!)

1. Visit [replit.com](https://replit.com)
2. Create account
3. Click "Create Repl"
4. Select Python
5. Start learning instantly!

---

## Troubleshooting

### "python: command not found"

**Windows**: Reinstall Python with "Add to PATH" checked
**Mac/Linux**: Use `python3` instead of `python`

### "pip: command not found"

```bash
# Windows
python -m pip install --upgrade pip

# Mac/Linux
python3 -m pip install --upgrade pip
```

### Virtual Environment Not Activating

**Windows**: Use full path: `.\.venv\Scripts\activate.bat`
**Mac/Linux**: Make sure you're in the repo directory

### Permission Denied on Mac/Linux

```bash
chmod +x venv/bin/activate
source venv/bin/activate
```

---

## Verify Setup Success

Run this in your terminal:

```python
import sys
import os

print(f"Python Version: {sys.version}")
print(f"Python Path: {sys.executable}")
print(f"\n🎉 Setup Successful! You're ready to learn!")
```

Save as `test_setup.py` and run:
```bash
python test_setup.py
```

If you see the version info, you're all set! 🚀

---

## Next Steps

1. Navigate to `phase_01_basics`
2. Open `README.md` to understand the phase
3. Run `lesson_01_hello_world.py`
4. Read through the lessons
5. Complete the exercises
6. Move to the next phase!

---

## Need Help?

- Check the FAQ in the main README
- Open an issue on GitHub
- Review troubleshooting section above
- Join our community discussions

**Happy Learning! 🎉**
