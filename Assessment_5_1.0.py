#############################################################
# Project Name:
# Owner: David Cleminson
# Date: 13/02/2020
# Assessment: 5
#############################################################

import csv
import os
import numpy as np
import pandas as pd

###########################################################################
#   SECONDARY MAIN LINE
###########################################################################
def main():
    # This presents the main menu
    # There is a requirement to have the data available for functions 3-6
    menu_type = 1
    data_loaded = False
    list_data = []
    select_options_value = 4

    select_option = display_menu(menu_type, select_options_value)

    while select_option != 4:
        # display_response(100)
        if select_option == 1:
            list_data = load_data_from_file()
            data_loaded = True
        elif select_option == 2:
            if not data_loaded:
                display_response(102)
            else:
                analyse_data(list_data)
        elif select_option == 3:
            if not data_loaded:
                display_response(102)
            else:
                visualise_data(list_data)

        select_option = display_menu(menu_type, select_options_value)

###########################################################################
#   Function Name: DISPLAY MENU
###########################################################################
def display_menu(menu_type, select_options_value):
    # This function will be reused for the presentation of all menu's

    if menu_type == 1:
        print('\nWelcome to The Smart Statistician!')
        print('Please choose one of the following options:')
        print('\t1 – Load from a CSV file')
        print('\t2 – Analyse')
        print('\t3 – Visualise')
        print('\t4 - Quit')

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
                           101: '\n\t  Select which list to sort:',
                           102: '\n\t  You have not imported a data file yet. Please select option 1:',
                           103: '\n\t  Filename does not exist or incorrect name, Please re-enter your filename: ',
                           104: '\n\t  The response is empty, please enter a valid value: ',
                           105: '\n\t  The name already exists, please try another: ',
                           106: '\n\t  Which list do you want to edit: ',
                           107: '\n\t  Element in the list are unique: ',
                           108: '\n\t  Which list do you want to analyse: ',
                           109: '\n\t  Please select a menu option and enter it: ',
                           110: '\n\t  User Exit Selected - Bye',
                           111: '\n\t  You have entered a valid Entry',
                           112: '\n\t  You have successfully Uploaded your file',
                           113: '\n\t  Please enter file name:',
                           114: '\n\t  The data requested has been sorted : \n'
                           }
    print(response_dictionary[response_code])
###########################################################################
#   Function Name: LOAD DATA FROM FILE
#  function Purpose: This function is used to load data from a csv file
###########################################################################
def load_data_from_file():  #Part of 1 --------------------------------- Working

    # data_loaded = False
    file_to_load = validate_file_name()
    # list_data = []

    list_data = {}
    # filename = input("Enter the filename: ")
    try:
        with open(file_to_load, 'r') as file:
            raw_data = csv.reader(file)
            for column in raw_data:
                column = [i for i in column if i]
                name = column[0]
                values = [float(i) for i in column[:1]]
                list_data[name] = values
            print('Debugger1 : ', list_data)
            return list_data
    except:
        print('File does not exist.')

    # print('Debugger', list_data)
    # file_to_load = validate_file_name()
    # list_data = pd.read_csv(file_to_load)
    # list_data = list_data.to_dict('split')
    # data_loaded = True
    # print(f'Debugging: ',list_data) #------------------------------------Debugging
    print('Debugger2 : ', list_data)
    return list_data

###########################################################################
#   Function Name: VALIDATE FILE NAME
#  function Purpose: This function validates the file name to make sure
#                    the name is valid and the file exists.
###########################################################################
def validate_file_name(): #Part of 1 ---------------------------------- Working

    user_input = False

    while not user_input:

        file_to_load = input("Please enter file name: ")
        if not os.path.isfile(file_to_load):
            display_response(103)
        else:
            return file_to_load

###########################################################################
#   Function Name: GET INDEX DATA LIST
#  function Purpose: This function (3a) creates a dictionary
#                    index and presents a menu from the lists available
#                    lists to be able to select current list names in use.
###########################################################################
def get_index_data_list(list_data): #Part of 3 ---------------------------------- Working

    list_index = {}

    for i, list_name in enumerate(list_data):
        list_index[i]= list_name['name']
        menu_name = list_name['name']
        print(f'\t{i + 1} - {menu_name}')
    # print('\n The list Index :', list_index) #------------------------------------- for Debugging
    return list_index

###########################################################################
#   Function Name: GET MODE VALUE
#  function Purpose: This function calculates the mode(s)
#                    for the data list.
###########################################################################
def get_mode_value(list_array):

    element_no = dict((x, list_array.count(x)) for x in set(list_array))

    if len(set(element_no.values())) == 1:
        return 'All values are unique.'
    else:
        list_mode = [keys for keys, values in element_no.items() if values == max(element_no.values())]
        return ', '.join([str(i) for i in list_mode])

###########################################################################
#   Function Name: ANALYSE DATA LIST
#  function Purpose: This function (4) calculates the stats for
#                    the data list.
###########################################################################
def analyse_data(list_data):

    option_number = False
    # select_options_value = len(list_data)

    while not option_number:
        display_response(106)
        list_index = get_index_data_list(list_data)
        # select_option = menu_input_validation(select_options_value)
        # select_option_index = select_option - 1
        # list_name = list_index[select_option_index]

        for i in list_data:
            for key, val in i.items():
                # if i[key] == list_name:
                list_array = i['value']

        elements = len(list_array)
        min = min(list_array)
        max = max(list_array)
        median = np.median(list_array)
        mode = get_mode_value(list_array)

        # print(list_name)
        print('----------')
        print(f'\tNumber of values (n): {elements}')
        print(f'\t                  Min: {min}')
        print(f'\t                  Max: {max}')
        print(f'\t               Median: {median}')
        print(f'\t              Mode(s): {mode}')
        option_number = True
    return


def visualise_data():

    return


main()