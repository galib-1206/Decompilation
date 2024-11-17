# Decompilation Project

## Overview

**This project demonstrates the process of decompiling Python bytecode files (`.pyc`) to retrieve the original source code.** 

It includes steps from creating a Python script (`example.py`), compiling it into bytecode, and then decompiling the bytecode file (`.pyc`) back into a Python source file. The decompiled Python file is saved in the `decompiled_files` folder.

#### **What is a .pyc file?** 
.pyc files are created by the Python interpreter when a .py file is imported. They contain the “compiled bytecode” of the imported module/program so that the “translation” from source code to bytecode (which only needs to be done once) can be skipped on subsequent imports if the .pyc is newer than the corresponding .py file.

In short, .pyc files are basically treated like a cache; they speed things up, so if they’re present, it can save some time by not having to re-compile the Python source code.

## Prerequisites

Ensure that you have the following installed on your system:

- **Python** (version 3.9 or higher)
- **pip3** (for managing Python packages)
- **pycdc** (Python bytecode decompiler)

## Setup Instructions

### 1. Create the Example Python Script

First, create a simple Python script named `example.py` with the following content:

```python
def greet(name):
    return f'''Hello, {name}!'''

if __name__ == '__main__':
    user_name = input('Enter your name: ')
    greeting = greet(user_name)
    print(greeting)
```
This script takes the user's name as input and prints a greeting message.

### 2. Compile the Python Script into Bytecode

Next, compile the example.py file into Python bytecode (.pyc file), which is automatically stored in the __pycache__ directory.
If the __pycache__ directory does not exist, you can explicitly generate the .pyc file using the py_compile module:
```bash
python3 -m py_compile example.py
```
After running the above command, you should find the bytecode file example.cpython-39.pyc inside the __pycache__ directory.

### 3. Install Dependencies

To decompile the .pyc file, you need to install a Python decompiler. There are several decompilers available, but we will use pycdc in this guide due to its compatibility with Python 3.9 bytecode files.

**Why use pycdc?**

While there are other decompilers available (e.g.**uncompyle6**, **decompyle++**, **pycdde**), we chose **pycdc** for the following reasons:

**Compatibility with Python 3.9 Bytecode:** Some decompilers, like *uncompyle6*, may not support newer Python versions such as 3.9 or higher. For example, uncompyle6 currently does not support bytecode for Python 3.9 and later (e.g., version 3.9.0 or 3.10).

#### **Example error with uncompyle6 for Python 3.9:**
```bash
uncompyle6 -o decompiled_files __pycache__/example.cpython-39.pyc

Unsupported Python version, 3.9.0, for decompilation
```
**On the other hand**, pycdc supports Python 3.9 bytecode, making it a better fit for this project.

To install pycdc, run the following command:
```bash
pip3 install pycdc
```

If you encounter issues with pip3, you can install it for the current user using:
```bash
pip3 install --user pycdc
```
or

```bash
sudo snap install pycdc
```

### 4. Decompile the Bytecode
Once pycdc is installed, you can decompile the .pyc file to get back the original Python source code. To save the decompiled code into a file inside the decompiled_files folder, run the following command:
```bash
pycdc __pycache__/example.cpython-39.pyc > decompiled_files/decompiled_example.py
```
This will save the decompiled content into a file named decompiled_example.py in the decompiled_files folder.

### 5. Check the Decompiled Code
After running the above command, navigate to the decompiled_files directory to confirm that the decompiled Python file has been created:
```bash
ls decompiled_files
```
**Example Decompiled Code**
The decompiled content should look something like this:
```python
# Source Generated with Decompyle++
# File: example.cpython-39.pyc (Python 3.9)

def greet(name):
    return f'''Hello, {name}!'''

if __name__ == '__main__':
    user_name = input('Enter your name: ')
    greeting = greet(user_name)
    print(greeting)
```

### 6. Cleanup
You can now delete the __pycache__ directory and the original .pyc file if you no longer need them, keeping only the example.py and decompiled_example.py files:
```bash
rm -r __pycache__
```