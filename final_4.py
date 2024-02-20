## Given the stubs for the following functions,
## complete the implementation to match the documentation.
def get_list_avg(lst):
    """ Given a list of numerical values,
    iterate over the elements until a negative
    value is found.
    Return the average of the positive elements
    in the list that came **before** the first
    negative element.
    If the input list is empty, return -1.
    If the first element of the input list is < 0,
    return -2.
    For example, if the list contains
    [10, 1, 6, 3, -1, 5, 9]
    the function returns (10 + 1 + 6 + 3) / 4,
    which is 5.0
    """
    if len(lst) == 0:
        return -1
    elif lst[0] < 0:
        return -2
    else:
        su = 0
    
        i = 0
        while i < len(lst):
            if lst[i] < 0:
                break
            
            su = su + lst[i]
            i = i + 1
            
        return su/(i)
    #pass

def date_euro_to_us(input_date):
    """
    The function splits the date given in the
    DD.MM.YYYY format and returns a new string
    with the date switched to MM/DD/YYYY.

    Performs the checks in the following order:
    If input_date is not a string, return -1.
    If the input_date does not contain the correct 
    number of shown delimiters, return -2.
    If the year does not contain 4 digits, return -3.
    
    For the following input:
    '08.03.2022', the function returns '03/08/2022'
    """
    if not isinstance(input_date, str):
        return -1
    elif not (input_date[2] == '.' and input_date[5] == '.'):
        return -2
    
    elif not(input_date[6].isdigit() and input_date[7].isdigit() and input_date[8].isdigit() and input_date[9].isdigit()):
        return -3
    else:
        new_split = input_date.split(".")
        new_string = "/".join(new_split)

        return new_string
        

    #pass
