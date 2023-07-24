#Calculate grade of five subjects.

print('Enter your marks:')
sub1=int(input())
sub2=int(input())
sub3=int(input())
sub4=int(input())
sub5=int(input())
 
avg=(sub1+sub2+sub3+sub4+sub5)/5
 
if avg >= 90:
   print("Grade: A")
elif avg >= 80:
   print("Grade: B")
elif avg >= 70:
   print("Grade: C")
elif avg >=60:
   print("Grade: D")
else:
   print("Grade: F")