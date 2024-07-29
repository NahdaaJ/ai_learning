# Python Basics

> Course: [The Complete Python Bootcamp From Zero to Hero in Python](https://www.udemy.com/course/complete-python-bootcamp/)

## Set Up

1. **Installing Python:** Install Python from the official website: https://www.python.org/downloads/.
2. **Making Python Accessible:** Add Python to you path:
    1. Get the path address (something like C:\Users\YourName\AppData\Local\Programs\Python\Python312)
    2. Type environment in your bottom search bar, go to your environment variables and add the path to system variables and your user variables.
    3. Check this has worked by entering `python --version` in cmd. A version number should be returned.
3. **Setting Up VSCode**: Install the Python extension by Microsoft in VSCode.
4. **Configure Python Interpreter**: Open your project folder in VSCode and open the command palette (`Ctrl+Shift+P`) and type and click on “Python: Select Interpreter.” Choose the appropriate Python interpreter (should be the version you have installed).
5. **Setting Up Virtual Environment:** In VSCode, open the terminal (`Ctrl+'`) and run the following commands:
    1. `python -m venv venv` to create the virtual environment.
    2. `.\venv\Scripts\activate` to activate the virtual environment.
6. **Installing Libraries:** Install your required libraries using `pip install`.
7. **Running Your Files:** In your terminal, type `python your-file-name.py` and press enter.
