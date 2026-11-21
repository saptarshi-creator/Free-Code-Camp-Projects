running_total = 0

num_of_friends = int(input("Enter the number of friends:"))             #4


appetizers = float(input("Enter the cost of appetizers:"))                    #37.89
main_courses =  float(input("Enter the cost of main courses:"))               #57.34
desserts =  float(input("Enter the cost of desserts:"))                       #39.39
drinks = float(input("Enter the cost of drinks:"))                            #64.21

running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

tip_given = float(input("Enter the tip in decimal:"))
tip = running_total * tip_given
print('Tip amount:', tip)

running_total += tip
print('Total with tip:', running_total)

final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

each_pays = round(final_bill, 2)
print(f'Each person pays: {each_pays}')