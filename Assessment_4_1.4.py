#############################################################
# Project Name:
# Owner: David Cleminson
# Date: 15/02/2020
#############################################################

import csv
import os

###########################################################################
#   SECONDARY MAIN LINE
###########################################################################
def main():
    # This presents the main menu
    # There is a requirement to have the data available for functions 3-6
    menu_type = 1
    data_loaded = False
    list_data = []
    select_options_value = 6

    select_option = display_menu(menu_type, select_options_value)

    while select_option != 6:
        # display_response(100)
        if select_option == 1:
            list_data = load_data_from_file()
            data_loaded = True
        elif select_option == 2:
            if not data_loaded:
                display_response(102)
            else:
                display_all_data(list_data)
        elif select_option == 3:
            if not data_loaded:
                display_response(102)
            else:
                rename_data_list(list_data)
        elif select_option == 4:
            if not data_loaded:
                display_response(102)
            else:
                sort_data_list(list_data)
        elif select_option == 5:
            if not data_loaded:
                display_response(102)
            else:
                analyse_data_list(list_data)

        select_option = display_menu(menu_type, select_options_value)

###########################################################################
#   Function Name: DISPLAY MENU
###########################################################################
def display_menu(menu_type, select_options_value):
    # This function will be reused for the presentation of all menu's

    if menu_type == 1:
        print('\nWelcome to The Smart Statistician!')
        print('Please choose one of the following options:')
        print('\t1 – Load data from a file')
        print('\t2 – Display the data to the screen')
        print('\t3 – Rename a set')
        print('\t4 – Sort a set')
        print('\t5 – Analyse a set')
        print('\t6 - Quit')
    # elif menu_type == 2:

    select_option = validate_menu_input(select_options_value)

    return select_option

###########################################################################
#   Function Name: VALIDATE MENU INPUT
#  function Purpose:This function validates the correct number is entered
###########################################################################
def validate_menu_input(select_option_values):

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

    data_loaded = False
    list_data = []
    file_to_load = validate_file_name()

    with open(file_to_load, 'r') as file:
        raw_data = csv.reader(file)
        for line in raw_data:
            line = [i for i in line if i]
            list_data_set = {}
            list_data_set['name'] = line[0]
            list_data_set['value'] = [int(i) for i in line[1:]]
            list_data.append(list_data_set)
            # print('List data = ', list_data_set)  #------------------------ Debugging Print
        return list_data

###########################################################################
#   Function Name: GET INDEX DATA LIST
#  function Purpose: This function (3a) creates a dictionary
#                    index and presents a menu from the lists available
#                    lists to be able to select current list names in use.
###########################################################################
def get_index_list(list_data): #Part of 3 ---------------------------------- Working

    list_index = {}

    for i, list_name in enumerate(list_data):
        list_index[i]= list_name['name']
        menu_name = list_name['name']
        # print(f'\t{i + 1} - {menu_name}')
    # print('\n The list Index :', list_index) #------------------------------------- for Debugging
    return list_index

###########################################################################
#   Function Name: SHOW DATA MENU
#  function Purpose: This function index's and presents a menu from
#                    the lists available lists to be able to select current
#                    list names in use.
###########################################################################
def show_data_menu(list_index):
    for [key], menu_name in enumerate(list_index):
        print(f'\t{i + 1} - {menu_name}')

    return

###########################################################################
#   Function Name: VALIDATE FILE NAME
#  function Purpose: This function validates the file name to make sure
#                    the name is valid and the file exists.
###########################################################################
def validate_file_name(): #Part of 1 ---------------------------------- Working

    user_input = False

    while not user_input:
        # file_to_load = 'data.csv' #------------------------------------- for Debugging
        file_to_load = input("Please enter file name: ") # --------- Correct line
        # file_to_load = input(display_response(113)) # --------- Correct line
        if not os.path.isfile(file_to_load):
            display_response(103)
        else:
            return file_to_load

###########################################################################
#   Function Name: VALIDATE NEW NAME
#  function Purpose: This function prompts for the name of the list
#                    and makes sure the list name does not exist already.
###########################################################################
def validate_new_name(list_index): #Part of 3 ---------------------------------- Working

    name_option = False
    show_data_menu(list_index)
    # print('List_Index Data: ', list_index) #------------------------------------- for Debugging

    while not name_option:
        define_new_name = str(input(f'\nPlease enter a new name :'))
        if define_new_name in list_index:
            display_response(105)
            name_option = True
        else:
            return define_new_name

###########################################################################
#   Function Name: VALIDATE LIST SELECTION
#  function Purpose: Validates the data list and the selection
#                    of a list from all the possible lists
###########################################################################
def validate_list_selection(list_data):

    option_number = False
    select_options_value = len(list_data)

    while not option_number:
        display_response(106)  # Check response code 101 or 106 ------ for Debugging
        list_index = get_index_list(list_data)
        data_menu = show_data_menu(list_index)
        print (data_menu)
        select_option = validate_menu_input(select_options_value)
        select_option_index = select_option -1
        list_name = list_index[select_option_index]
        option_number = True

    return list_name

###########################################################################
#   Function Name: DISPLAY ALL DATA
#  function Purpose: This function displays all the data loaded for
#                    the user to view
###########################################################################
def display_all_data(list_data):  #Part of 2 ------------------------ Working

       for i in list_data:
            print(i['name'])
            print(str(i['value'])[1:-1])
            print('----------')

###########################################################################
#   Function Name: RENAME DATA LIST
#  function Purpose: This function renames the a specific list of data
#                    chosen by the user.
###########################################################################
def rename_data_list(list_data): #Part of 3 ------------------------ Working

    list_index = get_index_list(list_data)

    list_name = validate_list_selection(list_data)
    new_name = validate_new_name(list_index)
    # print('new name =:', new_name)
    print(f'{list_name} renamed to {new_name}')

    return

###########################################################################
#   Function Name: SORT DATA LIST
###########################################################################
def sort_data_list(list_data): #Part of 4 ---------------------------------- Working
    # This function (4) sorts the a data list.
    list_name = validate_list_selection(list_data)

    for i in list_data:
        for key, val in i.items():
            if i[key] == list_name:
                list_array = i['value']

                print(f'\t The {list_name} list will be sorted.\n')
                print(f'\tBefore : {list_array} \n') #------------------------------------- for Debugging
                list_array.sort()
                # i['value'] = sorted(i['value'])
                print(f'\tAfter  : {list_array}\n')
                display_response(114)
    return

###########################################################################
#   Function Name: ANALYSE DATA LIST
###########################################################################
def analyse_data_list(list_data):
    # This function (4) claculates the stats for the data list.

    list_name = validate_list_selection(list_data)

    for i in list_data:
        for key, val in i.items():
            if i[key] == list_name:
                # print(i['value'])  # ------------------------------------- for Debugging
                list_array = i['value']
                no_elements = len(list_array)
                list_min = min(list_array)
                list_max = max(list_array)
                list_median = get_median_value(list_array, no_elements)
                list_mode = get_mode_value(list_array, no_elements)

                print(list_name)
                print('----------')
                print(f'\tNumber of values (n): {no_elements}')
                print(f'\t                  Min: {list_min}')
                print(f'\t                  Max: {list_max}')
                print(f'\t               Median: {list_median}')
                print(f'\t              Mode(s): {list_mode}')
                option_number = True
            return

###########################################################################
#   Function Name: GET MEDIAN VALUE
###########################################################################
def get_median_value(list_array, no_elements):
    # This function (4a) claculates the median for the data list.

    element_half = no_elements // 2

    if not no_elements % 2:
        median_value = (list_array[element_half] + list_array[element_half - 1]) / 2.0
        return median_value
    else:
        median_value = list_array[element_half]
        return median_value

###########################################################################
#   Function Name: GET MODE VALUE
###########################################################################
def get_mode_value(list_array, no_elements):
    # This function (4a) claculates the mode for the data list.
    element_no = dict((x, list_array.count(x)) for x in set(list_array))

    if len(set(element_no.values())) == 1:
        return 'All values are unique.'
    else:
        list_mode = [keys for keys, values in element_no.items() if values == max(element_no.values())]
        return ', '.join([str(i) for i in list_mode])

###########################################################################
#   Call main Function
###########################################################################
main()
