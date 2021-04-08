student_scores = input("Input a list of student scores \n").split()

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

#we intialize it to 0 so that we can keep track of the loop
highest_score = 0

for score in student_scores:
    # this line of code check if the score as a variable in for loop is greater than the value it have checked prevously
    if score > highest_score: 
        highest_score = score # in this line of code we reassigned the value of score to highest Score
print (f"The highest score in the class is: {highest_score}")
        


