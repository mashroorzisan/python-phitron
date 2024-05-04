class Star_Cinema:
    __hall_list = []

    def entry_hall(self):
        self.__hall_list.append(self)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.__seats = {}
        self.__show_list = []

        self.entry_hall()

    def entry_show(self, id, movie_name, time):
        show_tuple = (id, movie_name, time)
        self.__show_list.append(show_tuple)
        seat_alloc = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append('Free')
            seat_alloc.append(row)
        self.__seats[id] = seat_alloc

    def book_seats(self, id, seats_tuple):
        
        if id in self.__seats:
            show = self.__seats[id]
            for row, col in seats_tuple:
                if 0 <= row < self.rows and 0 <= col < self.cols:
                    if show[row][col] == 'Free':
                        show[row][col] = 'Booked'
                        print(f'({row}, {col}) seat booked successfully.')
                    else:
                        print(f'({row}, {col}) seat is already booked.')
                else:
                    print(f'The seat ({row},{col}) is not in range of this hall')
        else:
            print(f'There is no show with id {id}')

    def view_show_list(self):
        if len(self.__show_list) != 0:
            for id, movie_name, time in self.__show_list:
                print(f"ID: {id}, Movie Name: {movie_name}, Time: {time}")
        else:
            print("Currently no show is running")

    def view_available_seats(self, id):
        if id in self.__seats:
            show_seats = self.__seats[id]
            for i in range(self.rows):
                for j in range(self.cols):
                    if show_seats[i][j] == 'Free':
                        print(f"Row {i}, Col {j}")
        else:
            print(f"There is no show with ID {id}")
