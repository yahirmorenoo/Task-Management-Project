from tasks import *

if __name__ == "__main__":
    the_menu = {
        'P' : 'Print tasks',
        'A' : 'Add a task',
        'U' : 'Update a task',
        'D' : 'Delete task',
        'SI' : 'Show incomplete tasks',
        'SC' : 'Show completed tasks',
        'SP' : 'Show tasks sorted by priority, highest first',
        'SD' : 'Show tasks sorted by due date, earliest first',
        'S' : 'Save tasks',
        'L' : 'Load tasks from file',
        'Q' : 'Quit this program'



        }
    

    opt = None
    
    tasked = []
    
    while True:
        # print_main_menu(...) #TODO
        
        
        print_main_menu(the_menu)
        print("::: Enter an option")
        opt = input("> ")
        opt = opt.upper()
        

        if opt == 'q' or opt == 'Q': #TODO: make Q or q quit the program
            print("See you next time!")
            break # exit the main `while` loop
        else:
            if check_option(opt, the_menu) == "invalid": #TODO
                print("This is not a valid opt")
                continue
            
        print(f"You selected option {opt} to > {the_menu[opt]}.")

        if opt == 'P':
            print_formatted_tasks(tasked)
            if len(tasked) == 0:
                print("No current tasks")
            #print("")    
        
        elif opt == 'A':
            name = input("Enter name: ")
            description = input("Enter description: ")
            date = input("Enter a date: ")
            priority = input("Enter priority, (must be 1-5): ")
            completed = input("Enter yes or no: ")
            tasked.append(create_a_task(name,description, date, priority, completed)[1])
            
        elif opt == 'U':
            op = input("Would you like to see tasks again before picking?(Answer Y if so): ")
            if op == 'Y':
                print_formatted_tasks(tasked)
            
            idx = input("Enter the index you want to update: ")
            field = input("Field you would like to update here: ")
            up = input("New value of the field: ")
            update_task(tasked,idx,field,up)
            
        elif opt == 'D':
            op2 = input("Would you like to see tasks again before picking?(Answer Y if so): ")
            if op2 == 'Y':
                print_formatted_tasks(tasked)
            del_idx = int(input("Enter the index you want to delete: "))
            delete_task(del_idx, tasked)
            
            
        elif opt == 'SI':
            print_tasks_by_status(tasked, False)
            
        elif opt == 'SC':
            print_tasks_by_status(tasked, True)
            
        elif opt == "SP":
            print("this is extra credit option")
            
        elif opt == 'SD':
            print("this is extra credit option")
            
        elif opt == 'S':
            file = input("Enter file you want to save to: ")
            save_to_csv(tasked,file)
            
        elif opt == 'L':
            load_file = input("Enter file you want to load from: ")
            load_list = load_from_csv(load_file)
            tasked.append(load_list)
            
            
        else:
            print("This option is not yet implemented.") #TODO

        opt = input("::: Press Enter to continue...")

    print("Have a productive day!")

