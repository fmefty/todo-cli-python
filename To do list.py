tasks = []

#Define a function to display the task

def show_tasks():
    for i, task in enumerate(tasks):
        print(f'{i+1}.{task}')
        
#start an infinite loop to keep the program running

while True: 
    action = input("Choose: Add / Delete / View / Exit: ").lower()
    
    #If the user wants to add a task
    if action == "add":
        task = input('Task: ')
        tasks.append(task)
        
        
    #if the user wants to delete a task
    elif action == "delete":
        index = int(input("Index to delete: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index) #Remove the task from list
        else: 
            print("Invalid index!") #Show error if index is out of range
            
    #if the user wants to view all the tasks
    elif action == "view":
        if tasks:
            print("\nYour Tasks: ")
            show_tasks()  #call the function to show the task
            
    #if the user wants to exit the program 
    elif action == "exit":
        print("Goodbye!")
        break #Exit the loop 
    
    else:
        print("Invalid action! please choose: add / delete / view / exit")