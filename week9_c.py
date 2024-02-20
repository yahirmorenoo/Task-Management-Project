## Given the stub for the following function 
## and the main program, complete the implementation.
## Finish the assert statement to properly
## assert the result shown below (be careful 
## with the types of the variables).
def slice_str(input_str, start_idx, end_idx):
    """
    The function slices the string from the start_idx
    (included) until the end_idx (not included).
    Returns the sliced string.
    The function expects:
    - input_str: a string
    - start_idx: an integer >= 0
    - end_idx: an integer >= 0

    Performs the checks in the following order:
    If input_str is not a string, return -1.
    If either start_idx or end_idx is not an integer,
    return -2.
    If the input_str is empty, return None.
    If either start_idx or end_idx is not a valid index
    in the input_str, return -3.
    
    For the following input:
    'The cow jumped over the moon.', 4, 7
    the function returns "cow"
    """
    if(not(isinstance(input_str,str))):
        return -1
    
    elif (not(isinstance(start_idx,int))):
        return -2
    
    elif (not(isinstance(end_idx,int))):
        return -2
    
    elif(len(input_str) == 0):
        return none
    
    elif(len(input_str) <= start_idx):
        return -3
    
    elif(len(input_str) <= end_idx):
        return -3
    
    else:
        x = start_idx
        new_string = ""
        while(x < end_idx):
            chara = input_str[x]
            new_string = new_string + chara
            x = x + 1
        return new_string
            
    


if __name__ == "__main__":
    ### Write 3 assert statements
    ### to test the function
    assert(slice_str('c', 1, "2") == -2)
    assert(slice_str("cat",1, 4) == -3)
    assert(slice_str("cat", 0, 2) == "ca")
