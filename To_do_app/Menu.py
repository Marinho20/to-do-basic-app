import task_management as tm
def showmenu ():
    print("----------------------")
    print("\nMain Menu:")
    print("1-> Manage Tasks" )
    print("2-> view tasks" )
    print("3-> save and exit" )
    print("----------------------")

    

def Menu ():
    print("loading tasks from cloud...")
    tm.load_file()
    while True :  
        showmenu()
        choice = input("Enter your choice: ")
        if choice == '1':
         while True:
            print("----------------------")
            print("\nTask Management Menu:")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Remove Task")
            print("4. mark task as complete")
            print("5. Clear Completed Tasks")
            print("6. Return to Main Menu")
            print("----------------------")
            sub_choice = input("Enter your choice: ")
            print("----------------------")
            if sub_choice == '1':
                tm.add_task()
                tm.save_file()
            elif sub_choice == '2':
                tm.view_tasks()
            elif sub_choice == '3':
                tm.remove_task()
                tm.update_id()
                tm.save_file()  
            elif sub_choice == '4':
                tm.mark_complete()
                tm.save_file()
            elif sub_choice == '5':
                tm.clear_completed_tasks()
                tm.update_id()
                tm.save_file()
            elif sub_choice == '6':
                print("Returning to Main Menu...")
                break
            else:
                print("Invalid choice, please try again.")
        elif choice == '2':
            tm.view_tasks()     
        elif choice == '3':
            print("Saving tasks to cloud...")
            tm.save_file()
            print("Exiting the program...")
            break   





