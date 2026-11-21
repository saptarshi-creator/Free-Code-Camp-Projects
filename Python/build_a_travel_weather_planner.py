distance_mi = 10
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True

#distance_mi = float(input("Distance travelled in mile: "))
#is_raining = input("Is it raining(True/False): ") == "True"
#has_bike = input("Has bike(True/False): ") == "True"
#has_car = input("Has car(True/False): ") == "True"
#has_ride_share_app = input("Has Ride Share App(True/False): ") == "True"

if(distance_mi):
 if (distance_mi <= 1):
    if(is_raining):
        print("False")
    else:
        print("True")

 elif (distance_mi <= 6 ):
    if(is_raining):
        if(has_bike):
         print("False")
        else:
            print("False") 
    else:
        if(has_bike):
           print("True")
        else:
            print("False")

 elif (distance_mi >6 ):
    if(has_car or has_ride_share_app):
        print("True")
    else:
        print("False")
else:
    print("False")

