import pandas as pd

def main():
    ###########################################################
    #   TASK: Week6 Book 3 Task 1
    ###########################################################
    my_data = [43, 37, 94, 64, 89, 57, 12, 32, 98, 74, 39, 56, 91, 61, 53, 36, 94, 34, 23, 62, 59, 92, 85, 86, 52]
    bins = [-1, 49, 64, 74, 84, 100]

    cats = pd.cut(my_data, bins)
    code_array = cats.codes
    cat_list = cats.categories

    print(f'\n Here is the interval Index:\n {cat_list}')
    print(f'\n Here is the code array:\n {code_array}')

    ###########################################################
    #   TASK: Week6 Book 3 Task 2
    ###########################################################
    cats_range = pd.cut(my_data, 5)
    print(f'\n My data with same range: \n {cats_range}')

    ###########################################################
    #   TASK: Week6 Book 3 Task 3
    ###########################################################
    cats_entries = pd.qcut(my_data, 5)
    print(f'\n My data with same number of entries \n {cats_entries}')

main()