import os.path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def display_menu():
    print('\nWelcome to The DataFrame Statistician!')
    print('Choose one of the following options:')
    print('\t1 - Load from a CSV file')
    print('\t2 - Analyse')
    print('\t3 - Visualise')
    print('\t4 - Quit\n')

def get_valid_choice(number_choices):
    """
    Function gets a valid choice from the user.
    """
    choice = 0
    valid_user_choice = False
    while not valid_user_choice:
        try:
            choice = int(input(f'Enter a number between 1 and {number_choices}: '))
            if choice not in range(1, number_choices+1):
                raise ValueError
            valid_user_choice = True
        except ValueError:
            print(f"\nError! Input must be an integer in range 1 to {number_choices}.")
    return choice

def valid_file_input():
    """
    Function checks the file input from the user is valid. 
    """
    user_input = False
    while not user_input:
        file_name = input("Enter file name: ")
        if not os.path.isfile(file_name):
            print("Error! Invalid file name. ")
        else:
            print(f"\nThe file '{file_name}' was loaded successfully.")
            return file_name

def load_data(file_name):
    """
    Function loads the data from a CSV into list called all_dataset.
    all_datasets contains each set is an individual dictionary.
    """
    dataframe = None
    dataframe = pd.read_csv(file_name)
    dataframe.index = range(1,len(dataframe)+1)
    return dataframe

def display_dataset_names(dataframe):
    """
    Prints the index and name of the dataset from all_datasets to the screen.
    """
    dataset_names = list(dataframe.keys())
    for index, name in enumerate(dataset_names, start=1):
        print("\t{} - {}".format(index,name))
    print()

def get_user_dataset(dataframe):
    """
    Displays the names for each user dataset and return index from the user's choice.
    """
    display_dataset_names(dataframe)
    index = get_valid_choice(len(dataframe.keys()))
    return index

def analyse_set(dataframe, index):
    report = {}
    names = dataframe.keys()
    values = dataframe[str(names[index-1])]
    report['name'] = names[index-1]
    report['count'] = len(values)
    report['mean'] = round(values.mean(),2)
    report['std'] = round(values.std(),2)
    report['std_error'] = round(values.sem(),2)
    display_report(report)


def display_report(report):
    print("")
    print(report["name"])
    print("----------")
    print("Number of values (n):", report["count"])
    print("Mean:", report["mean"])
    print("Standard Deviation:", report["std"])
    print("Std.Err of Mean:", report["std_error"])
    print("--------------------")

def display_visualisation_choices():
    print()
    print("Which type of graph do you want to generate?")
    print('\t1 - Line Graph')
    print('\t2 - Bar Graph')
    print('\t3 - Box Plot')

def get_subplot_decisison():
    valid_user_decision = False
    while not valid_user_decision:
        subplot_decision = input("\nDo you want every variable on subplots (y/n)?")
        subplot_decision.lower()
        if subplot_decision == "y" or subplot_decision == "n":
            if subplot_decision == "y":
                valid_user_decision = True
            else:
                valid_user_decision = True
        else:
            print("Error! Type in either 'y' or 'n'.") 
    return subplot_decision

def construct_graphics(index,subplot_decision,dataframe):
    if index == 1 and subplot_decision == "y":
        dataframe.plot.line(subplots = True, layout = (len(dataframe.columns),1))
        plt.show()
    elif index == 1 and subplot_decision == "n":
        dataframe.plot.line()
        plt.show()
    elif index == 2 and subplot_decision == "y":
        dataframe.plot.bar(subplots = True, layout = (len(dataframe.columns),1))
        plt.show()
    elif index == 2 and subplot_decision == "n":
        dataframe.plot.bar()
        plt.show()
    elif index == 3 and subplot_decision == "y":
        dataframe.plot.box(subplots = False, layout = (len(dataframe.columns),1))
        plt.show()
    elif index == 3 and subplot_decision == "n":
        dataframe.plot.box()
        plt.show()            


def main():
    dataframe = None
    option = None
    while option != 4:
        display_menu()
        option = get_valid_choice(4)
    
        if option is not 1 and dataframe is None:
            print("Error! Data must be loaded before performing an operation.")
        elif option == 1:
            file_name = valid_file_input()
            dataframe = load_data(file_name)
        elif option == 2:
            print("Which dataset do you want to analyse?")
            index = get_user_dataset(dataframe)
            analyse_set(dataframe,index)
        elif option == 3:
            display_visualisation_choices()
            index = get_valid_choice(3)
            subplot_decision = get_subplot_decisison()
            construct_graphics(index,subplot_decision,dataframe)
        elif option == 4:
            print("Goodbye.")

main()
