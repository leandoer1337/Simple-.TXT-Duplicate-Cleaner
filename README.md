# Simple .TXT Duplicate Cleaner

A lightweight Python GUI tool that scans `.txt` files or entire folders for duplicate lines and removes them. Built with `tkinter`, it provides a clean interface and supports dark mode, icon customization, and a Windows installer.

---

## ✨ Features

- Scan individual `.txt` files for duplicates
- Scan folders and clean all `.txt` files inside
- Removes duplicate lines automatically
- Dark mode theme
- Custom icon
- Lightweight standalone `.exe` (no need to install Python)
- GUI installer created with Inno Setup

---

## 🛠 How to Build

### 1. Build the Python Executable

Install PyInstaller if you haven't:

```bash
pip install pyinstaller
```

Then run:
```bash
pyinstaller --onefile --icon=icon.ico "Simple .TXT Duplicate Cleaner.py"
```
*Output will be in the dist/ folder.*

2. Build the Windows Installer
Download and install Inno Setup from:
📦 https://jrsoftware.org/isinfo.php

Then open **installer.iss** in Inno Setup and build the installer.

```graphql
📂 Project Structure

Simple-TXT-Duplicate-Cleaner/
│
├── Simple .TXT Duplicate Cleaner.py     # Main Python script
├── icon.ico                             # Icon used for EXE
├── installer.iss                        # Inno Setup script
├── README.md                            # This file
├── .gitignore                           # Git exclusions
└── dist/                                # Output from PyInstaller (ignored)
```
---
## 💡 Usage

Download and run the installer from Releases

Launch the app from your start menu or shortcut

**Click:**

*Clean single .TXT file* to clean one .txt file

*Clean folder of .TXT files* to clean all .txt files in a folder

Duplicates are removed automatically, and original files are overwritten with clean versions.

---
## 💻 Requirements (for building only)
Python 3.9+

tkinter (standard with Python)

PyInstaller (pip install pyinstaller)

Inno Setup (to build installer)

End users do **not** need Python installed — the app runs standalone.

## 📝 License

This project is licensed under the MIT License.