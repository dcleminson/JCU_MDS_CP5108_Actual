#############################################################
# Project Name: Advanced Analysis
# Owner: David Cleminson
# Date: 20/02/2020
# Assessment: 5
#############################################################


import os.path
import pandas as pd
import matplotlib.pyplot as plt


###########################################################################
#   SECONDARY MAIN LINE
###########################################################################
def main():
    valid_dataframe = []
    data_loaded = False
    select_options_value = 4
    display_menu()
    select_option = menu_input_validation(select_options_value)

    while select_option != 4:
        if select_option is not 1 and not data_loaded:
            print(f'\n\t You have not imported a data file yet. Please select option 1:')
        elif select_option == 1:
            valid_dataframe = load_data_from_file()
            data_loaded = True
        elif select_option == 2:
            if not data_loaded:
                print(f'\n\t You have not imported a data file yet. Please select option 1:')
            else:
                print(f'\n\t Select a dataset to analise: ')
                index = get_dataset_index(valid_dataframe)
                analyse_data_set(valid_dataframe, index)
        elif select_option == 3:
            if not data_loaded:
                print(f'\n\t You have not imported a data file yet. Please select option 1:')
            else:
                display_graph_type_submenu()
                graph_selection = menu_input_validation(3)
                subplot_choice = get_graph_logic()
                plot_graphics(graph_selection, subplot_choice, valid_dataframe)

        display_menu()
        select_option = menu_input_validation(select_options_value)
    print(f'\t\n See you another time.')

###########################################################################
#   Function Name: DISPLAY MENU
#  function Purpose: This function will be reused for the presentation
#                    of the main menu
###########################################################################


def display_menu():

    print(f'\nWelcome to The DataFrame Statistician!')
    print(f'Choose one of the following options:')
    print(f'\t1 - Load from a CSV file')
    print(f'\t2 - Analyse')
    print(f'\t3 - Visualise')
    print(f'\t4 - Quit\n')

###########################################################################
#   Function Name: MENU INPUT VALIDATION
#  function Purpose:This function validates the correct number is entered
###########################################################################


def menu_input_validation(select_option_values):
    valid_option = False
    while not valid_option:
        try:
            select_option = int(input("\tPlease select a menu option and enter the number: ") or 0)
            if select_option not in range(1, select_option_values + 1):
                print(f'\n\t You have entered an invalid number, Please try again:',)
                raise Exception
            valid_option = True
            return select_option
        except:
            print(f'\tPlease Enter a number from 1 to {select_option_values} ')

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
            print(f'\n\t Filename does not exist or incorrect name, Please re-enter your filename: ')
        else:
            print(f"\nThe file '{file_to_load}' was loaded successfully.")
            valid_file_to_load = file_to_load
            return valid_file_to_load


###########################################################################
#   Function Name: LOAD DATA FROM FILE
#  function Purpose: This function is used to load data from a csv file
#                    into a dataframe
###########################################################################


def load_data_from_file():
    valid_file_to_load = validate_file_name()

    dataframe = pd.read_csv(valid_file_to_load)
    dataframe.index = range(1, len(dataframe) + 1)
    valid_dataframe = dataframe
    return valid_dataframe


###########################################################################
#   Function Name: DISPLAY DATASET SUBMENU
#  function Purpose:
#                    of the main menu
###########################################################################


def display_dataset_submenu(valid_dataframe):
    dataset_names = list(valid_dataframe.keys())
    for index, name in enumerate(dataset_names, start=1):
        print(f'\t{index} - {name}')
    print()


###########################################################################
#   Function Name: GET DATASET INDEX
#  function Purpose: This function (3a) creates a dictionary
#                    index and presents a menu from the lists available
#                    lists to be able to select current list names in use.
###########################################################################


def get_dataset_index(valid_dataframe):
    display_dataset_submenu(valid_dataframe)
    index = menu_input_validation(len(valid_dataframe.keys()))
    return index


###########################################################################
#   Function Name: ANALYSE DATA SET
#  function Purpose: This function (4) calculates the stats for
#                    the data list.
###########################################################################


def analyse_data_set(valid_dataframe, index):
    set_names = valid_dataframe.keys()
    set_values = valid_dataframe[str(set_names[index - 1])]
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
#   Function Name: GET GRAPH LOGIC
#  function Purpose: This function sets out the logic as to how the
#                    data will be presented.
###########################################################################


def get_graph_logic():
    valid_user_decision = False
    while not valid_user_decision:
        subplot_choice = input(f'\nDo you want all columns of the data presented in subplots (y/n)?')
        subplot_choice.lower()
        if subplot_choice == "y" or subplot_choice == "n":
            if subplot_choice == "y":
                valid_user_decision = True
            else:
                valid_user_decision = True
        else:
            print("Error! Type in either 'y' or 'n'.")
    return subplot_choice


###########################################################################
#   Function Name: PLOT GRAPHICS
#  function Purpose: This function plots the actual graphs based
#                    on the logic.
###########################################################################


def plot_graphics(graph_selection, subplot_choice, valid_dataframe):
    if graph_selection == 1:
        if subplot_choice == "y":
            valid_dataframe.plot.line(subplots=True, layout=(len(valid_dataframe.columns), 1))
        else:
            valid_dataframe.plot.line()
    elif graph_selection == 2:
        if subplot_choice == 'y':
            valid_dataframe.plot.bar(subplots=True, layout=(1, len(valid_dataframe.columns)))
        else:
            valid_dataframe.plot.bar()
    elif graph_selection == 3:
        if subplot_choice == "y":
            valid_dataframe.plot.box(subplots=True, layout=(1, len(valid_dataframe.columns)))
        else:
            valid_dataframe.plot.box()
    plt.show()


###########################################################################
#   Function Name: MAIN LINE
###########################################################################

main()
