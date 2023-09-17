# Execution
In order to run the program, run the file below:
```
main.py
```

The default method of running through the program is by using tkinter. If you would prefer to just use the console, however, you can change the variable near the top, which is initalized as:
```
CONSOLE_MODE = False
```

Likewise, you can also change the variable near the top initialized as:
```
MAX_PRINT = 20
```
This will affect how many test values and predictions are printed out. By default, I have it set to only print out up to 20, but this can be changed to any integer, including 0. Negative integers will result in all test values printing out.

If you continue with console mode deactivated, make sure you have the tkinter library installed. It is installed with Python, so you may need to use the Python installer to customize your Python build and add it. Also, sometimes tkinter windows will render behind your code editor, so you may need to minimize other windows to find the tkinter ones.

# Input
The program will expect models to be pickle files (.pkl). It will also expect training files as .tra and testing files as .tes, so please keep this in mind when inputting your file paths into the program, as it could cause errors if you provide an invalid file type.

# Dependencies
* tkinter (if not using the console mode)
* scikit-learn

# Project File Structure
```
main.py
README.md
model_scripts
    __init__.py
    get_model.py
data
    models
```
