first_name = input('Your First Name: ')
last_name = input('Your Last Name: ')

full_name = first_name + ' ' + last_name

address = input('Your Address: ')
address += ' is your address'

employee_age = int(input('Your Age: '))
employee_info = full_name + ' is ' + str(employee_age) + ' years old'

print(employee_info)

experience_years = int(input('Years of experience:   '))
experience_info = 'Experience: ' + str(experience_years) + ' years'

print(experience_info)

position = input('Your Position: ')
salary = int(input('Your salary in dollars:'))

employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'

print(employee_card)

employee_code = input('Your Employee code: ')  #'DEV-2026-JD-001'
department = employee_code[0:3]

print(department)

year_code = employee_code[4:8]
initials = employee_code[9:11]
last_three = employee_code[-3:]


print('Year Code:',year_code)
print('The initials are:', initials)
print('Last Three Characters is: ',last_three)