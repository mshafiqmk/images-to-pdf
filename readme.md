# Image to PDF Converter

This project provides a simple Python script to convert images into a single PDF file while maintaining the order of the images based on their filenames.

## Requirements

- Python 3.x
- Pillow library

## Installation

1. **Clone the repository (if applicable):**

   ```bash
   git clone <repository-url>
   cd <repository-name>

## Python Virtual Environment Instructions
=======================================

This document provides step-by-step instructions on how to create and use a Python virtual environment (venv).

What is a Virtual Environment?
------------------------------

A virtual environment is an isolated environment in which you can install packages separately from the system-wide Python installation. This helps manage dependencies for different projects without conflicts.

Creating a Virtual Environment
------------------------------

1.  **Open your terminal or command prompt.**
2.  **Navigate to your project directory:**
    
        cd path/to/your/project
    
3.  **Create a virtual environment:**
    
    Run the following command:
    
        python -m venv venv
    
    This creates a new directory named `venv` in your project folder, containing the virtual environment.
    

Activating the Virtual Environment
----------------------------------

To activate the virtual environment, use the following commands:

*   **On Windows:**
    
        venv\Scripts\activate
    
*   **On macOS/Linux:**
    
        source venv/bin/activate
    

Once activated, your command prompt should change to indicate that you are now working within the virtual environment (e.g., it might show `(venv)` at the beginning of the line).

Installing Packages
-------------------

While the virtual environment is activated, you can install packages using `pip`. For example, to install `Pillow`, run:

    pip install Pillow

To install multiple packages from a `requirements.txt` file:

    pip install -r requirements.txt

Deactivating the Virtual Environment
------------------------------------

When you are done working in the virtual environment, you can deactivate it by running:

    deactivate

Your command prompt will return to normal, indicating that you are no longer in the virtual environment.

Summary of Commands
-------------------

    
    cd path/to/your/project
    python -m venv venv
    # Activate
    # Windows:
    venv\Scripts\activate
    # macOS/Linux:
    source venv/bin/activate
    # Install packages
    pip install Pillow
    # Deactivate
    deactivate
        

By following these instructions, you can easily manage your Python projects using virtual environments.