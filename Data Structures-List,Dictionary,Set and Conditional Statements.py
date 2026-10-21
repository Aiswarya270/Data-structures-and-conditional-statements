#List with integer
age_list=[44,48,52,56,60]
print(age_list)

#List with String
name_list=["Zara","Niom","Ithal","Vyom","Adhrik"]
print(name_list)

#Append string
name_list.append("Yazhini")
print(name_list)

#Insert element
age_list.insert(2,30)
print(age_list)

#Remove string
name_list.remove("Yazhini")
print(name_list)

#Pop
age_list.pop()
print(age_list)

#Extend
age_list.extend([29,30,26])
print(age_list)

#Sort
age_list.reverse()
print(age_list)

#Max ,Min & Sum
max_age=max(age_list)
min_age=min(age_list)
total_age=sum(age_list)
print(max_age)
print(min_age)
print(total_age)

#First element
print(name_list[0])
#Last element
print(name_list[-1])
#Index
print(name_list[2:5])
#Reverse
print(name_list[::-1])

##DICTIONARY
#Create dictionary
student_marks={"Zara":80,"Niom":90,"Ithal":85,"Vyom":92,"Adhrik":78}
print(student_marks)

#Specific
print(student_marks["Vyom"])

#Add
student_marks["Nithara"]=88
print(student_marks)

#Update
student_marks["Adhrik"]=82
print(student_marks)

#Key,Values
print("Keys:", student_marks.keys())
print("Values:", student_marks.values())
print("Key-Value Pairs:", student_marks.items())


##SET
#Create set
my_set = {'a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'}
print(my_set)
#"Output & explanation - This happens because set do not allow duplicates"

#Change value
#my_set[4] = 's'
#error_explanation ="Set is unordered and also does not support indexing"
#print(error_explanation)


#Create 2 sets
set1={1,3,5,7,9}
set2={2,3,5,8,10}
print(set1)
print(set2)

#Union and intersection
union_set=set1.union(set2)
intersection_set=set1.intersection(set2)
print(union_set)
print(intersection_set)

##OPERATORS & CONDITIONAL STATEMENTS
#Prompt user for input
score = float(input("Enter your score (0 to 10): "))
print("Your score is:", score)

#Check performance category
score = float(input("Enter your score (0 to 10): "))

if score > 7:
    print("Above Average")

elif score >= 4:
    print("Average")

else:
    print("Below Average")

#Print output and additional step
score = float(input("Enter your score (0 to 10): "))
if score > 7:
    print("Above Average")
    print("Excellent performance! Keep up the good work!")
elif score >= 4:
    print("Average")
    print("Good effort! Keep practicing.")
else:
    print("Below Average")
    print("Need to improve your performance. Consistent practice will lead to better results.")



