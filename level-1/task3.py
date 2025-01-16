Physics = int(input("Enter Physics Marks: "))
Chemistry = int(input("Enter Chemistry Marks: "))
Biology = int(input("Enter Biology Marks: "))
Mathematics = int(input("Enter Mathematics Marks: "))
Computer = int(input("Enter Computer Marks: "))
Total_Subject = 5

Total = Physics + Chemistry + Biology + Mathematics + Computer
Percentage = Total/Total_Subject

print("Total", Total)
print("Percentage", Percentage)

if Percentage >= 90 :
    print("Grade A")
elif Percentage >= 80:
    print("Grade B")
elif Percentage >= 70:
    print("Grade C")
elif Percentage >= 60:
    print("Grade D")
elif Percentage >= 50:
    print("Grade E")
else:
    print("Grade FB")