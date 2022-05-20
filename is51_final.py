

""" STRUCTURED ENGLISH
This program is trying to show the number of grades, the average grade, 
and the percentage of grades that are above the average grade of 83.25. 

The main function will be used to start the application and we will use the 
calculate_percent_above_average function to find the percentage of the grades that 
are higher than the average grade. 

The number of grades will be shown as the length of a list of numbers
The average grade will be shown as sum of all the grades, divided by the number of all grades.
The percentage of grades above the average grade will be shown as the grades > average grade.

"""

""" PSUEDOCODE
Create list
len(list)

calculate average 
sum of list / len(list)

percentage of grades higher than average scores 
 sum of highscores / 24 * 100
 print percentage 
"""
#num_of_grades= len(78,67,56,99,80,83,82,91,94,95,77,88,85,92,91,79,88,82,81,86,94,93,92,45)

grades = [78,67,56,99,80,83,82,91,94,95,77,88,85,92,91,79,88,82,81,86,94,93,92,45]
num_of_grades = len(grades)
print("The number of grades is: ", len(grades))

def cal_average(grades):
    sum_grades = 0
    for t in grades:
        sum_grades = sum_grades + t
    avg = sum_grades / len(grades)
    return avg 
print ("The average is ", cal_average ([78,67,56,99,80,83,82,91,94,95,77,88,85,92,91,79,88,82,81,86,94,93,92,45]))

sum_of_highergrades = [99,91,94,95,88,85,92,91,88,86,94,94,92]
num_of_highergrades = len(99,91,94,95,88,85,92,91,88,86,94,94,92)
percentage_of_highergrades = ((sum_of_highergrades/ 1998) * 100)

print(" The percentage of grades that are above of the average grade is" (percentage_of_highergrades))
