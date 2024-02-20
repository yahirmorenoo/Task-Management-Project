from validate import *

def print_main_menu(menu_1):
    """
    Prints main menu in main program.
    """
    print('**************************')
    print('What would you like to do?')
    for number, text in enumerate(menu_1):
        print((f'{text} - {menu_1[text]}'))
    print('**************************')
    
def check_option(option, menu):
    """
    Checks option is valid or invalid in the main program.
    """
    if option in menu and isinstance(option, str) == True:
        return "valid"
    else:
        return "invalid"

def create_a_task(name, description, date, priority, completed):
    """
    creates task from name to deadline.
    """
    if validate_name(name) == False:
        return False, "name"
    if validate_description(description) == False:
        return False, "description"
    if validate_date(date) == False:
        return False, "deadline"
    if validate_priority(priority) == False:
        return False, "priority"
    if validate_completed(completed) == False:
        return False, "completed"
        
    if completed == 'no' or completed == 'No':
        completed = False
    else:
        completed = True
    dic = {"name": name, "description": description, "deadline": date, "priority": int(priority), "completed": completed}
    return True, dic
    
def slashes_to_written(date_list):
    """
    Turns date into letter month form, starting with month, date and year.
    """
    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    month = int(date_list[0])
    day = int(date_list[1])
    year = date_list[2]
    return month_names[month]+" "+str(day)+", "+year


def print_formatted_tasks(tasks_list):
    """
    Prioritizes the importance of task.
    """
    priority = {1:"Lowest", 2: "Low", 3: "Medium", 4: "High", 5: "Highest"}
    month = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
    counter = 0
    for dic in tasks_list:
        print(str(counter) + ":  " + dic.get('name').upper())
        print("    Description: " + dic.get('description'))
        print("    Priority: " + priority.get(dic.get('priority')))
        temp = dic.get('deadline')
        s = temp.split("/")
        print("    Deadline: " + str(month.get(s[0])) + " " + str(int(s[1])) + ", " + str(s[2]))
        if (dic.get('completed')):
            print("    Completed: Yes")
        else:
            print("    Completed: No")
        counter += 1
        print()

def print_tasks_by_status(all_tasks, completed=False):
    
    """
    Prints tasks from 'all_tasks',
    based on the value of 'completed' of each task.
    If there are no tasks that are incomplete,
    prints 'You do not have incomplete tasks.'
    If there are no tasks that are completed,
    prints 'You do not have completed tasks.'
    Otherwise, prints the requested tasks.
    """
    lst = []
    for x in range(len(all_tasks)):
        if all_tasks[x]["completed"] == completed:
            lst.append(all_tasks[x])

    if len(lst) == 0:
        if completed == False:
            print("You do not have incomplete tasks.")
        else:
            print("You do not have completed tasks.")
        
    else:
        print_formatted_tasks(lst)

def update_task(task_list, task_id, task_field, task_update):
    """
    updates task depending on what will be updated.
    """
    fields = ['name','description','deadline','priority','completed'] 
    
    if is_valid_index(int(task_id), task_list) == False:
        return False, "idx"
    
   
    if task_field == fields[0]:
        if validate_name(task_update) == False:
            return False, 'name'
        else:
            (task_list[int(task_id)])['name'] = task_update;
                #update
    elif task_field == fields[1]:
        if validate_description(task_update) == False:
            return False, 'description'
        else:
            (task_list[int(task_id)])['description'] = task_update;
            #update
    elif task_field == fields[2]:
        if validate_date(task_update) == False:
            return False, 'deadline'
        else:
            (task_list[int(task_id)])['deadline'] = task_update;
            #update
    elif task_field == fields[3]:
        if validate_priority(task_update) == False:
            return False, 'priority'
        else:
            (task_list[int(task_id)])['priority'] = task_update;
            #update
    elif task_field == fields[4]:
        if validate_completed(task_update) == False:
            return False, 'completed'
        else:
            if task_update == 'no' or task_update == "No":
                task_update = False
            else:
                task_update = True
            
            (task_list[int(task_id)])['completed'] = task_update;
            #update
    else:
        return False, 'field'
   
        #succes replaction
    return True, task_list[int(task_id)]
    
def delete_task(idx, tasks):
    
    """
    Checks if idx, which is an integer, is a valid index inside Tasks
    """

    if is_valid_index(idx,tasks) == False:
       return False
    
    else:
        del tasks[idx]
    #not sure if this how you delete a task
        return True

import csv
def save_to_csv(task_list, filename):
    
    """
    saves file to csv
    """
    with open(filename, 'w', newline='') as f:
         task_writer = csv.writer(f)
         for current_dict in task_list:
             task_data=[current_dict['name'], current_dict['description'], current_dict['deadline'], current_dict['priority'], current_dict['completed']]
             task_writer.writerow(task_data)
    
def load_from_csv(filename):
    """
    loads file from csv
    """
    new_list = [] # empty list to store the data from the csv file
    
    with open(filename, 'r') as csvfile:
        
        reader_object =  csv.reader(',') #... #TODO: initiate csv.reader object

        for values in reader_object:
            if len(values) == 5:#... #check if there are 5 items in the list 'values'
                
                #convert the last field (a Boolean flag) to "yes" or "no"
                if values[4] == False:
                    values[4] = 'no'
                else:
                    values[4] = 'yes'
                
                #call create_task_task and add it to new_list
                result = create_a_task(values[0],values[1],values[2],values[3],values[4]) #TODO: FILL ME IN

                if result[0] == True:#... #TODO: checks what create_a_task returned
                    new_list.append(result[1])#TODO: append the dictionary to the new_list
                    return new_list
                else:
                    print("WARNING: invalid data -", values)
                    return "invalid data"

            else: #if data formatting is inconsistent
                print("WARNING: invalid data -", values)
                print("WARNING: Data formatting is inconsistent with the task manager!")
                return "inconsistent format"
    

         
    
