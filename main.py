print("Please enter grades in full caps, with no spaces. If a grade for one of your classes is not currently avaliable, please type null")

class1 = input("Enter class 1 grade:")
class2 = input("Enter class 2 grade:")
class3 = input("Enter class 3 grade:")
class4 = input("Enter class 4 grade:")
class5 = input("Enter class 5 grade:")
class6 = input("Enter class 6 grade:")
class7 = input("Enter class 7 grade:")
class8 = input("Enter class 8 grade:")

class_list = [class1, class2, class3, class4, class5, class6, class7, class8]

total = 0
classes = 8

for response in class_list:
  if response == "A+":
    response = 4.0
    total = response + total
  elif response == "A":
    response = 4.0
    total = response + total
  elif response == "A-":
    response = 3.7
    total = response + total
  elif response == "B+":
    response = 3.3
    total = response + total
  elif response == "B":
    response = 3.0
    total = response + total
  elif response == "B-":
    response = 2.7
    total = response + total
  elif response == "C+":
    response = 2.3
    total = response + total
  elif response == "C":
    response = 2.0
    total = response + total
  elif response == "C-":
    response = 1.7
    total = response + total
  elif response == "D+":
    response = 1.3
    total = response + total
  elif response == "D":
    response = 1.0
    total = response + total
  elif response == "F":
    response = 0.0
    total = response + total
  elif response == "null":
    respones = None
    classes = classes - 1
  else:
    print("Invalid Response. Please reset program.")
  

total = total/classes
print("Your GPA is ", total)