salary = int(input("Please enter your income: ")) # we got the income from the user
raise_rate = int(input("Please enter the raise rate: ")) # we got the raise rate from the user
current_salary = salary * raise_rate / 100 + salary # we calculated the new salary by adding the raise rate to the salary
print(current_salary) # we used this code to print the current salary