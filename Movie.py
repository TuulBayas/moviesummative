""""
Movie Theatre Booking System with Seats
By Tuul Bayasgalan
"""
#ask user for thier name and phone number
print("Welcome to YK Movie Theater!")

name = input("What is your name? ")
number = None
#validate phone number
while not isinstance (number, int):
        try:
            number = int(input("What is your phone number?"))
        except:
            print ('Please enter a valid phone number.')
#books movie
movies = ['1. Lucifer', '2. Shrek', '3. All of us are Dead']
def moviebooking():

    #global variable for movie
    global movies

    print("Today's movies")

    #prints movies one by one
    for movie in movies:
        print (movie)

    movie_choice = None

    #match case for user picking movie choice
    while movie_choice not in ('1','2','3'):

        movie_choice = input ('Please, select a movie (a/b/c): ')

        match movie_choice:
            case '1':
                print('You have chosen', movies[0])
                selected_movie = movies[0]
            case '2':
                print('You have chosen', movies[1])
                selected_movie = movies[1]
            case '3':
                print('You have chosen', movies[2])
                selected_movie = movies[2]
            case '':
                print('Invalid choice')
    return selected_movie
#books time
times = ['1. Morning', '2. Afternoon', '3. Evening']
def timebooking():        
    global times
    #prints times for movies
    for time in times:
        print (time)

    time_choice = None

    #match case for user picking movie choice
    while time_choice not in ('1','2','3'):

        time_choice = input ('Please, select time (a/b/c): ')

        match time_choice:
            case '1':
                print('You have chosen', times[0])
                selected_time = times[0]
            case '2:
                print('You have chosen', times[1])
                selected_time = times[1]
            case '3':
                print('You have chosen', times[2])
                selected_time = times[2]
            case _:
                print('Invalid choice')
    return selected_time

#seats
movie_seats = (([],[],[]),([],[],[]),([],[],[]))
#for morning lucifer
def movie_seat(selected_movie, selected_time): 
    ordered_seats=[]
    while True:  
        movie_index = movies.index(chosen_movie)
        time_index = times.index(chosen_time)
        #print seats and checks if seat is already booked or not
        seats_text = ''
        for seat_number in range(1,11):
            if seat_number in movie_seats[movie_index][time_index]:
                seats_text = seats_text + ' X'
            else:
                seats_text = seats_text + f' {seat_number}'

        print (seats_text)
        #asks user for their seat choice and adds it to their order
        seat_choice = None
        while seat_choice not in range(1,11):
            #Validate that while not chosen_seat.isnumber():  
            seat_choice = int(input("What seat do you want? "))
            
            if seat_choice in movie_seats[movie_index][time_index]:
                print("Seat has been chosen, Please choose a different seat.")
            else:
                movie_seats[movie_index][time_index].append(seat_choice)
                ordered_seats.append(seat_choice)

        #asks the user if they want to rebook their order
        rebook = None
        rebook = input("Do you want to book a seat again? ")
        if rebook == 'no':
            print("Thanks")
            break
    return ordered_seats

#function that asks the user to confirm their order
def confirmation(chosen_movie, chosen_time):
    print("Name: ", name, "Phone Number: ", number, "Movie: ", chosen_movie, "Time: ", chosen_time, "Seat: ", seat_choice), 

while True:  
    chosen_movie = moviebooking()
    chosen_time = timebooking()
    seat_choice = movie_seat(chosen_movie, chosen_time)

    #confirm information
    print("Name: ", name, "Phone Number: ", number, "Movie: ", chosen_movie, "Time: ", chosen_time, "Seat: ", seat_choice), 
    answer = None
    while answer not in ('yes', 'no'):
        answer = (input("Is your order accurate? ")).lower()
    answer = answer.lower()
    if answer=='yes':   
        print("Order confirmed")     
        print("Name: ", name, "Phone Number: ", number, "Movie: ", chosen_movie, "Time: ", chosen_time, "Seat: ", seat_choice), 
        break
