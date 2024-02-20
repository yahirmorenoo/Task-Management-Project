def check_option(option, menu):
    if option in menu and type(option) == str:
        return "valid"
    else:
        return "invalid"

def is_numeric(val):
    """
    Checks if the string is a valid interger or float number.
    """
    
    lst = val.split('.')
    
        
    if len(lst) <= 2:
        for x in range(len(lst)):
            if not lst[x].isnumeric():
                return False
        return True
       
        
    else:
        return False
    
    
def is_valid_index(idx, in_list):
    """
    Checks if the given idx is a valid index in the list.
    """
    if idx < 0:
        return False
    elif idx > len(in_list)-1:
        return False
    else:
        return True

def validate_name(name):
    """
    checks if the name lenght is valid.
    """
    if len(name) >= 3 and len(name) <= 15:
        return True
    else:
        return False

def validate_description(desc):
    """
    checks if the inputted description is valid by making sure theres
    an input.
    """
    if len(desc) > 0:
        return True
    else:
        return False

def validate_date(date_string):
    """
    checks the date is valid.
    """
    num_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    if len(date_string) == 0:
        return False
    if not date_string[0].isdigit():
        return False
    if date_string[2] != '/':
        return False
    if not date_string[3].isdigit():
        return False
    if date_string[5] != '/':
        return False
    if not date_string[6].isdigit():# might have to add is digit for the rest of the dates not just the beginnings
        return False
    if len(date_string) > 10:#check to keep good digits
        return False
    month = int(date_string[0:2])
    day = int(date_string[3:5])
    
    if month not in num_days:
        return False
    if day < 1 or day > num_days[month]:
        return False
    return True

def validate_priority(priority):
    """
    checks the priority importance value from 1-5.
    """
    if not priority.isdigit():
        return False
        
    if int(priority) >= 1 and int(priority) <= 5:
        return True
    else:
        return False

def validate_completed(comp):
    """
    Checks if the task has been completed.
    """
    if comp == 'yes' or comp == 'no' or comp == "Yes" or comp == "No":
        return True
    else:
        return False









    

    
