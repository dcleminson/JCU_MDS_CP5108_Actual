import os.path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



###########################################################################
#   SECONDARY MAIN LINE
###########################################################################
from matplotlib import pyplot


def main():
    dataframe = []
    data_loaded = False
    select_options_value = 4

    select_option = display_menu(select_options_value)

    while select_option != 4:
        if select_option is not 1 and data_loaded == False:
            display_response(102)
        elif select_option == 1:
            # file_to_load = validate_file_name()
            dataframe = load_data_from_file()
            data_loaded = True
        elif select_option == 2:
            if not data_loaded:
                display_response(102)
            else:
                display_response(101)
                index = get_dataset_index(dataframe)
                analyse_data_set(dataframe, index)
        elif select_option == 3:
            if not data_loaded:
                display_response(102)
            else:
                display_graph_type_submenu()
                graph_selection = menu_input_validation(3)
                data = setup_graph_data(dataframe)
                setup_graphics_details(graph_selection, dataframe)
                # plt.show(setup_graphics_details(graph_selection,data))
        elif select_option == 4:
            print("Goodbye.")

        select_option = display_menu(select_options_value)
###########################################################################
#   Function Name: DISPLAY MENU
#  function Purpose: This function will be reused for the presentation
#                    of the main menu
###########################################################################
def display_menu(select_options_value):
    print('\nWelcome to The DataFrame Statistician!')
    print('Choose one of the following options:')
    print('\t1 - Load from a CSV file')
    print('\t2 - Analyse')
    print('\t3 - Visualise')
    print('\t4 - Quit\n')

    select_option = menu_input_validation(select_options_value)

    return select_option

###########################################################################
#   Function Name: MENU INPUT VALIDATION
#  function Purpose:This function validates the correct number is entered
###########################################################################
def menu_input_validation(select_option_values):

    valid_choice = False
    while not valid_choice:
        try:
            select_option = int(input("\tPlease select a menu option and enter the number: ") or 0)
            if select_option not in range(1, select_option_values + 1):
                display_response(100)
                raise Exception
            valid_choice = True
            return select_option
        except:
            print(f'\tPlease Enter a number from 1 to {select_option_values} ')


###########################################################################
#   Function Name: DISPLAY RESPONSE
#  function Purpose: This is a central repository for all errors and
#                    responses displayed to the users
###########################################################################
def display_response(response_code):

    response_dictionary = {100: '\n\t You have entered an invalid number, Please try again:',
                           101: '\n\t Select a dataset to analise: ',
                           102: '\n\t You have not imported a data file yet. Please select option 1:',
                           103: '\n\t Filename does not exist or incorrect name, Please re-enter your filename: ',
                           104: '\n\t The response is empty, please enter a valid value: ',
                           105: '\n\t  Please enter a file name: '
                           }
    print(response_dictionary[response_code])

###########################################################################
#   Function Name: VALIDATE FILE NAME
#  function Purpose: This function validates the file name to make sure
#                    the name is valid and the file exists.
###########################################################################
def validate_file_name():

    user_input = False

    while not user_input:
        file_to_load = input("Please enter file name: ")
        if not os.path.isfile(file_to_load):
            display_response(103)
        else:
            print(f"\nThe file '{file_to_load}' was loaded successfully.")
            user_input = True
            return file_to_load

###########################################################################
#   Function Name: LOAD DATA FROM FILE
#  function Purpose: This function is used to load data from a csv file
#                    into a dataframe
###########################################################################
def load_data_from_file():

    file_to_load = validate_file_name()

    dataframe = None
    dataframe = pd.read_csv(file_to_load)
    dataframe.index = range(1, len(dataframe) + 1)

    return dataframe

###########################################################################
#   Function Name: DISPLAY DATASET SUBMENU
#  function Purpose:
#                    of the main menu
###########################################################################
def display_dataset_submenu(dataframe):
    """
    Prints the index and name of the dataset from all_datasets to the screen.
    """
    dataset_names = list(dataframe.keys())
    for index, name in enumerate(dataset_names, start=1):
        print("\t{} - {}".format(index, name))
    print()

###########################################################################
#   Function Name: GET DATASET INDEX
#  function Purpose: This function (3a) creates a dictionary
#                    index and presents a menu from the lists available
#                    lists to be able to select current list names in use.
###########################################################################
def get_dataset_index(dataframe):
    """
    Displays the names for each user dataset and return index from the user's choice.
    """
    display_dataset_submenu(dataframe)
    index = menu_input_validation(len(dataframe.keys()))
    return index

###########################################################################
#   Function Name: ANALYSE DATA SET
#  function Purpose: This function (4) calculates the stats for
#                    the data list.
###########################################################################
def analyse_data_set(dataframe, index):

    set_names = dataframe.keys()
    set_values = dataframe[str(set_names[index - 1])]
    print("")
    print(f'{set_names[index - 1]}')
    print(f'----------')
    print(f'Number of values (n):{len(set_values)}')
    print(f'Mean: {round(set_values.mean(), 2)}')
    print(f'Standard Deviation:{round(set_values.std(), 2)}')
    print(f'Std.Err of Mean:{round(set_values.sem(), 2)}')
    print("--------------------")

###########################################################################
#   Function Name: DISPLAY GRAPH TYPE SUBMENU
#  function Purpose:
#                    of the main menu
###########################################################################
def display_graph_type_submenu():
    print()
    print("Which type of graph do you want to generate?")
    print('\t1 - Line Graph')
    print('\t2 - Bar Graph')
    print('\t3 - Box Plot')

###########################################################################
#   Function Name: SETUP GRAPH DATA
#  function Purpose:
#                    of the main menu
###########################################################################
def setup_graph_data(dataframe):
    valid_user_decision = False
    while not valid_user_decision:
        subplot_decision = input("\nDo you want every attribute of the dataframe graphed (y/n)?")
        subplot_decision.lower()
        if subplot_decision == "y" or subplot_decision == "n":
            if subplot_decision == "y":
                dataset = dataframe
                valid_user_decision = True
            else:
                print("Which dataset do you want graphed?")
                index = get_dataset_index(dataframe)
                names = dataframe.keys()
                dataset = dataframe[str(names[index])]
                valid_user_decision = True
        else:
            print("Error! Type in either 'y' or 'n'.")
    return dataset

###########################################################################
#   Function Name: SETUP GRAPHICS DETAIL
#  function Purpose:
#                    of the main menu
###########################################################################
def setup_graphics_details(graph_selection, dataframe):
    # if index == 1 and len(dataset.columns) == 1:
    #     data_set_subplot = dataset.plot.line(subplots=False)
    # elif index == 1 and len(dataset.columns) > 1:
    #     data_set_subplot = dataset.plot.line(subplots=True)
    # elif index == 2 and len(dataset.columns) == 1:
    #     data_set_subplot = dataset.plot.bar(subplots=False)
    # elif index == 2 and len(dataset.columns) > 1:
    #     data_set_subplot = dataset.plot.bar(subplots=True)
    # elif index == 3 and len(dataset.columns) == 1:
    #     data_set_subplot = dataset.plot.box(subplots=False)
    # elif index == 3 and len(dataset.columns) > 1:
    #     data_set_subplot = dataset.plot.box(subplots=True)




    set_names = dataframe.keys()
    set_values = dataframe[(set_names)]
    if graph_selection == 1:
        print('Set Values:',set_names)
        for i in dataframe:
            plt.plot(set_values)
            plt.ylabel('some numbers')
        plt.show()
    elif graph_selection == 2:
        print('Set Values:',set_names)
        for i in dataframe:
            plt.plot(set_names, set_values)
            plt.ylabel('some numbers')
        plt.show()
    elif graph_selection == 3:
        print('Set Values:',set_names)
        for i in dataframe:
            plt.boxplot(set_values)
            plt.ylabel('some numbers')
        plt.show()

###########################################################################
#   Function Name: MAIN LINE
###########################################################################

main()
