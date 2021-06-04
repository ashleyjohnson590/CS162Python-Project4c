#Author: Ashley Johnson
#Date: 4/16/2021
#Description: Program uses insertion sort to sort a list of strings
def string_sort(string_list):
    """uses insertion sort to sort a list of strings"""
    for string in range(1, len(string_list)):
        lower_case_string = [string.lower() for string in string_list]
        value = lower_case_string[string]
        position = string - 1
        while position >= 0 and lower_case_string[position] > value:
            lower_case_string[position + 1] = lower_case_string[position]
            position -= 1
        string_list[position + 1] = value