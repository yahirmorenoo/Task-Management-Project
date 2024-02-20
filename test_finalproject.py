from tasks import *
assert slashes_to_written(["01", "02", "2022"]) == 'January 2, 2022'
assert slashes_to_written(["01", "12", "1970"]) == 'January 12, 1970'
assert slashes_to_written(["04", "14", "2020"]) == 'April 14, 2020'
assert slashes_to_written(["06", "19", "2000"]) == 'June 19, 2000'
    
result = is_numeric('123')
print(f"--> is_numeric('123') returned `{result}`")
assert result == True

result = is_numeric('abc')
print(f"--> is_numeric('abc') returned `{result}`")
assert result == False

result = is_numeric('5.5.')
print(f"--> is_numeric('5.5.') returned `{result}`")
assert result == False

assert is_valid_index(0, [["Quizzes", 25.5]]) == True
assert is_valid_index(1, [["Quizzes", 25.5]]) == False
assert is_valid_index(-1, [["Quizzes", 25.5]]) == False
assert is_valid_index(1, [["Quizzes", 25.5], ["Project", 20]]) == True

assert create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[0] == True
assert type(create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]) == dict
assert create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]['name'] == 'do dishes'
assert create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]['description'] == 'wash the plates from dinner'
assert create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]['deadline'] == '03/04/2022'
   
# print(create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]['priority'])
assert create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]['priority'] == 2
 #print(create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]['completed'])
assert create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]['completed'] == False

# Regular input 2
assert create_a_task('see endgame', 'endgame with friends saturday', '01/18/2020', '3', 'yes')[0] == True
assert type(create_a_task('see endgame', 'endgame with friends saturday', '01/18/2020', '3', 'yes')[1]) == dict
assert create_a_task('see endgame', 'endgame with friends saturday', '01/18/2020', '3', 'yes')[1]['name'] == 'see endgame'
assert create_a_task('see endgame', 'endgame with friends saturday', '01/18/2020', '3', 'yes')[1]['description'] == 'endgame with friends saturday'
assert create_a_task('see endgame', 'endgame with friends saturday', '01/18/2020', '3', 'yes')[1]['deadline'] == '01/18/2020'
assert create_a_task('see endgame', 'endgame with friends saturday', '01/18/2020', '3', 'yes')[1]['priority'] == 3
assert create_a_task('see endgame', 'endgame with friends saturday', '01/18/2020', '3', 'yes')[1]['completed'] == True

# name too short
assert create_a_task('ii', 'did you see that name was too short?', '01/01/1970', '5', 'yes')[0] == False
assert create_a_task('ii', 'did you see that name was too short?', '01/01/1970', '5', 'yes')[1] == 'name'

# name too long
assert create_a_task('this is a very long name', 'name too long', '01/01/1970', '5', 'yes')[0] == False
assert create_a_task('this is a very long name', 'name too long', '01/01/1970', '5', 'yes')[1] == 'name'

# description empty
assert create_a_task('normal name', '', '01/01/1970', '5', 'yes')[0] == False
assert create_a_task('normal name', '', '01/01/1970', '5', 'yes')[1] == 'description'

# invalid dates empty
assert create_a_task('normal name', 'blah', '01/40/1970', '5', 'yes')[0] == False
assert create_a_task('normal name', 'blah', '01/40/1970', '5', 'yes')[1] == 'deadline'

assert create_a_task('normal name', 'blah', '13/01/1970', '5', 'yes')[0] == False
assert create_a_task('normal name', 'blah', '13/01/1970', '5', 'yes')[1] == 'deadline'

assert create_a_task('normal name', 'blah', '12#12#1970', '5', 'yes')[0] == False
assert create_a_task('normal name', 'blah', '12#12#1970', '5', 'yes')[1] == 'deadline'

assert create_a_task('normal name', 'blah', '02/30/1970', '5', 'yes')[0] == False
assert create_a_task('normal name', 'blah', '02/30/1970', '5', 'yes')[1] == 'deadline'
    
# invalid priority
assert create_a_task('normal name', 'blah', '10/15/2023', '10', 'yes')[0] == False
assert create_a_task('normal name', 'blah', '10/15/2023', '10', 'yes')[1] == 'priority'

assert create_a_task('normal name', 'blah', '10/15/2023', '0', 'yes')[0] == False
assert create_a_task('normal name', 'blah', '10/15/2023', '0', 'yes')[1] == 'priority'

assert create_a_task('normal name', 'blah', '10/15/2023', '6', 'yes')[0] == False
assert create_a_task('normal name', 'blah', '10/15/2023', '6', 'yes')[1] == 'priority'

# invalid completion
assert create_a_task('normal name', 'blah', '10/15/2023', '4', 'positive')[0] == False
assert create_a_task('normal name', 'blah', '10/15/2023', '4', 'positive')[1] == 'completed'

assert create_a_task('normal name', 'blah', '10/15/2023', '4', 'negative')[0] == False
assert create_a_task('normal name', 'blah', '10/15/2023', '4', 'negative')[1] == 'completed'

assert create_a_task('normal name', 'blah', '10/15/2023', '4', 'yess')[0] == False
assert create_a_task('normal name', 'blah', '10/15/2023', '4', 'yess')[1] == 'completed'

assert validate_date('01/12/2022')[0] == True
assert validate_date('01/12/2022')[1] == '01/12/2022'
    
assert validate_date('01/44/2022')[0] == False
assert validate_date('01/44/2022')[1] == -4
    
assert validate_date('January/12/2022')[0] == False
assert validate_date('January/12/2022')[1] == -2

assert update_category("invalid category", -1, []) == -3
assert update_category("invalid category", 1, []) == -3
result = update_category("Reflection 5", 0, [["RA", 2.0]])
expected = ["Reflection", 5.0]
print(f'update_category("Reflection 5", 0, [["RA", 2.0]]) \n returned {result} \n expected result is {expected}')
assert result == expected

result = load_from_csv("task_data.csv")
print(f"load_from_csv('task_data.csv') returned:\n{result}")
assert type(result) == list
assert type(result[0]) == dict
assert result[1]['name'] == "Do labs"
assert result[0]['deadline'] == "01/22/2022"
  
    
result = load_from_csv("task_data2.csv")
print(f"load_from_csv('task_data2.csv') successfully returned:\n'{result}'\n")
assert type(result) == str
assert result == "invalid data"
    
result = load_from_csv("task_data3.csv")
print(f"load_from_csv('task_data3.csv') successfully returned:\n'{result}'\n")
assert type(result) == str
assert result == "inconsistent format"    
