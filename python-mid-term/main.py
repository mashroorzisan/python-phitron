from cinemahall import Hall

hall1 = Hall(rows=5, cols=6, hall_no=1)
hall1.entry_show('001', 'Movie A', '12:00 PM')
hall1.entry_show('002', 'Movie A', '12:00 PM')

hall1.book_seats('001', [(3, 4), (5, 6)])
hall1.book_seats('002', [(1, 2), (3, 4), (5, 6)])


while True:
    print("\nWelcome to Star Cinema:")
    print("1. View Shows")
    print("2. View Available Seats")
    print("3. Book Tickets")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        hall1.view_show_list()
    elif choice == "2":
        show_id = input("Enter show ID: ")
        hall1.view_available_seats(show_id)
    elif choice == "3":
        show_id = input("Enter show ID: ")
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        seats_list = [(row, col)]
        hall1.book_seats(show_id, seats_list)
    elif choice == "4":
        print("Thank you for visiting Star Cinema!")
        break
    else:
        print("Invalid choice. Please choose again.")
