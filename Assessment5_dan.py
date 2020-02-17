import os.path
import numpy as np
import pandas as pd


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
    return index - 1

def Debug(data):
    raw_data = load_data("raw_data.csv")
    names = raw_data.keys()
    index = get_user_dataset(raw_data)
    print(names[index])

    data = raw_data[str(names[index])]
    print(np.mean(data))



def analyse_set(dataframe):
    """
    Function calculates selected summary statistics for a dataset.
    """
    report = {}
    values = dataset['values']
    report['name'] = dataset['name']
    report['count'] = len(values)
    report['max_value'] = max(values)
    report['min_value'] = min(values)
    report['median'] = calculate_median(values)
    report['mode'] = calculate_mode(values)
    display_report(report)