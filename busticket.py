from datetime import datetime

print("List of locations :\n 1.Chennai Egmore \n 2.Guduvanchery \n 3.Perungalathur \n 4.Pondicherry \n 0.Cancel Ride")
print("Type the number to choose the location of departure :")

#input for location of departure to location of arrival

start = int(input('Start = '))
stop = int(input('Stop = '))
distance = 0      #in kilometres
from_start = " "
to_stop = " " 


if(start == 0 or stop == 0):
    print("Ride Cancelled. Thank you for spending time\n")
    exit();
elif(start==stop):
    print("Invalid input!Try again")
elif(start<0 or stop>5):
    print("Invalid input! Try again")
else:
    if(start == 1 and stop == 2):
        from_start='Chennai Egmore'
        to_stop='Guduvanchery'
        distance = 52
    if(start == 1 and stop == 3):
        from_start='Chennai Egmore'
        to_stop='Perungalathur'
        distance = 35
    if(start == 1 and stop == 4):
        from_start='Chennai Egmore'
        to_stop='Pondicherry'
        distance=164
    if(start == 2 and stop == 3):
        from_start='Guduvancherry'
        to_stop='Perangalathur'
        distance=10
    if(start == 2 and stop == 4):
        from_start='Guduvancherry'
        to_stop='Pondicherry'
        distance=123
    if(start == 3 and stop == 4):
        from_start='Perangalathur'
        to_stop='Pondicherry'
        distance=132

no_of_passengers=int(input('Enter the number of passengers:'))

ride=distance*no_of_passengers

total_distance = str(distance)
cost_of_ride = str(ride)
time_data = str(datetime.now())

print("\n")
print("--------------------------------------\n")
print(time_data.center(40," "))
print("\n")
print(from_start.center(40," "))
print("\n\t\tTo\n")
print(to_stop.center(40," "))
print("\n")
print("\tCost of ride : " + str(no_of_passengers)+ " X "+str(distance)+"="+ str(ride))
print("--------------------------------------\n")
print("\n\n\n")


    

    