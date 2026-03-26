import json

def save_data():
    with open("text.json", "w") as f:
        json.dump(tasks, f)

def load_data():
    global tasks
    try:
        with open("text.json", "r") as f:
            tasks = json.load(f)
    except:
        tasks = []

tasks = []
load_data()

while True:
    print("=="*20)
    print("Smart To-Do List")
    print("=="*20)
    print("1.add\n2.view\n3.delete\n4.exit")

    choice = input("enter your choice > ")

    if choice == "2":
        print("Tasks:")
        for i, t in enumerate(tasks):
            print(i+1, t)

    elif choice == "4":
        print("exiting bye bye....")
        break

    elif choice == "1":
        task = input("enter your task >> ")
        tasks.append(task)
        save_data()
        print("Added:", task)

    elif choice == "3":
        if not tasks:
            print("no tasks there, kuch toh daal 😅")
        else:
            for i, t in enumerate(tasks):
                print(i+1, t)

            delete_task = int(input("enter task number >> ")) - 1

            if 0 <= delete_task < len(tasks):
                removed = tasks.pop(delete_task)
                save_data()
                print("Deleted:", removed)
            else:
                print("invalid input bhai")

    else:
        print("wrong choice")



    

        
        








    




    


   