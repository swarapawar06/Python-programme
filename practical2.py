

def linear_search(account_list, target):
    for account_id in account_list:
        if account_id == target:
            return True
    return False
    
# Binary Search Function
def binary_search(account_list, target):
    # Make sure the list is sorted before using binary search
    account_list.sort()

    low = 0
    high = len(account_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if account_list[mid] == target:
            return True
        elif account_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

#Sample customer account IDs 
account_ids = [1023, 2045, 3011, 1500, 2988, 1234]

while True:
    print("\nMENU")
    print("1. Linear Search")
    print("2. Binary Search")
    print("3. Exit")
    choice = int (input("Enter your choice (1-3: )"))
    if choice == 1:
        target_id = int (input("Entercustomer account ID to search"))
        if linear_search(account_ids, target_id):
            print ("Linear Search : Account ID found")
        else:
            print ("Linear Search: Account ID not found")
    elif choice == 2:
        target_id = int (input("Enter customer account ID to search : ")) 
        if binary_search(account_ids, target_id):
            print ("Binary Search: Account ID found") 
        else:
            print ("Binary Search: Account ID not found") 
    elif choice == 3:
        print ("Exiting the program.")
        break 
    else:
        print ("Invalid choice . Please enter 1, 2, 3. ")            
