import os

# Whether or not to run the whole program using only the console.
# Will otherwise not affect the program's execution.
CONSOLE_MODE = False

# The max number of test predictions to print out.
# Note: negative values will result in all test predictions printing.
MAX_PRINT = 20

if not CONSOLE_MODE:
    from tkinter import messagebox as mb, filedialog as fd

from model_scripts.get_model import load_model, train_model, save_model, test_model


cwd = os.getcwd()
data_folder = f"{cwd}/data"
models_folder = f"{cwd}/data/models"
default_modelname = "model"
again = True

while again:
    if not os.path.exists(models_folder):
        os.mkdir(models_folder)

    # Ask the user if they'd like to train a model or load one. Whichever the choice, store the result in model.
    message = "Would you like to train a model?"
    if CONSOLE_MODE:
        print(message)
        response = input().lower()
        response = response == "yes" or response == "y"
    else:
        response = mb.askyesno(title="Train Model?", message=message)

    # Prompt the user for the model's file path
    model_filename = ""
    if response:
        # Train and save a model
        training_filename = ""
        if CONSOLE_MODE:
            print("Please provide the path of the training file you'd like to use for this model...")
            training_filename = input()
        else:
            training_filename = fd.askopenfilename(title="Select a Training File", initialdir=data_folder, defaultextension=".tra", filetypes=[("Training File", "*.tra")])
        
        if training_filename != "" and training_filename is not None:
            model = train_model(training_filename)
        else:
            print("Error: Invalid test file path.")
            break

        save_location = ""
        if CONSOLE_MODE:
            print("Please input a file path to save your model to (not just a directory path)...")
            save_location = input()
        else:
            save_location = fd.asksaveasfilename(title="Save Model", initialdir=models_folder, initialfile=default_modelname, defaultextension=".pkl", filetypes=[("Pickle File", "*.pkl")])
        
        if save_location != "" and save_location is not None:
            save_model(model, save_location)
            model_filename = save_location
        else:
            print("Error: Invalid file path.")
            break
    else:
        # Load a model file
        if CONSOLE_MODE:
            print("Please input the path of the model you'd like to test...")
            model_filename = input()
        else:
            model_filename = fd.askopenfilename(title="Select a Model File", initialdir=models_folder, defaultextension=".pkl", filetypes=[("Pickle File", "*.pkl")])
        
        if model_filename == "" or model_filename is None:
            print("Error: Invalid model file path.")
            break

    model = load_model(model_filename)

    # Break if model is invalid
    if model is None:
        print("Error: Model not found")
        break



    # Prompt the user to provide a test file
    test_filename = ""
    if CONSOLE_MODE:
        print("Please input the path of the test file you'd like to run through the model...")
        test_filename = input()
    else:
        test_filename = fd.askopenfilename(defaultextension=".tes", filetypes=[("Test File", "*.tes")], initialdir=data_folder, title="Select a Test File")
    
    if test_filename != "" and test_filename is not None:
        test_model(model, test_filename, MAX_PRINT)
    else:
        print("Error: Invalid test file path.")



    # Prompt the user to go through the program again
    if CONSOLE_MODE:
        print("Would you like to run the program again?")
        response = input().lower()
        response = response == "yes" or response == "y"
    else:
        response = mb.askyesno(title="Run Again?", message="Would you like to run the program again?")
    again = response