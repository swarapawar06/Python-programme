event_queue = [] 
 
def add_event(event): 
    event_queue.append(event) 
    print(f"Event '{event}' is added to queue") 
 
def process_event(): 
    if event_queue: 
        x = event_queue.pop(0) 
        print(f"Event '{x}' is processed") 
    else: 
        print("No event available for processing") 
 
def display_pending_event(): 
    if event_queue: 
        print("Pending Events:") 
        for event in event_queue: 
            print(f"- {event}") 
    else: 
        print("No pending events") 
 
def cancel_event(event_name): 
    if event_name in event_queue: 
        event_queue.remove(event_name) 
        print(f"Event '{event_name}' is canceled") 
    else: 
        print(f"Event '{event_name}' is not found or already processed") 
 
def menu(): 
    while True: 
        print("\n--- EVENT MENU ---") 
        print("1. Add Event") 
        print("2. Process Event") 
        print("3. Display Pending Events") 
        print("4. Cancel Event") 
        print("5. Exit") 
 
        choice = input("Enter your choice: ") 
 
        if choice == '1': 
            event = input("Enter event name to add: ") 
            add_event(event) 
        elif choice == '2': 
            process_event() 
        elif choice == '3': 
            display_pending_event() 
        elif choice == '4': 
            event_name = input("Enter event name to cancel: ") 
            cancel_event(event_name) 
        elif choice == '5': 
            print("Exiting... Bye!") 
            break 
        else: 
            print("Invalid choice! Please try again.") 
 
menu()