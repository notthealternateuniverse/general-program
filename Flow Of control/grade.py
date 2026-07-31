sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))

average = (sub1 + sub2 + sub3) / 3

if average >= 90:
            grade = 'A'
elif average >= 80:
            grade = 'B'
elif average >= 70:
            grade = 'C'
elif average >= 60:
            grade = 'D'
else:
            grade = 'F'
            

print(f"\n--- Results ---")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
