# create a student app in python
'''5 student entities should be in list by default
add new student
update any student
delete any student
show all student emails and id'''

students = [{
    "id" : 1,
    "name" : "Ahmad",
    "email" : "student1@gmail.com",
    "rollNo" : 234,
    "class" : "web development"
    
},
 {
    "id" : 2,
    "name" : "Zain",
    "email" : "student2@gmail.com",
    "rollNo" : 238,
    "class" : "Python development"
    
},

 {
    "id" : 3,
    "name" : "Zoha",
    "email" : "student3@gmail.com",
    "rollNo" : 240,
    "class" : "web development"
    
},

{
    "id" : 4,
    "name" : "Saad",
    "email" : "student4@gmail.com",
    "rollNo" : 244,
    "class" : "app development"
    
},

 {
    "id" : 5,
    "name" : "Rashid",
    "email" : "student5@gmail.com",
    "rollNo" : 245,
    "class" : "web development"
    
}]
#print(students)

add_Student={"id" : len(students)+1,
        "name" : "Nasir",
        "email" : "student8@gmail.com",
        "rollNo" : 250,
        "class" : "web development"
        
    }


students.append(add_Student)
print(type(students))
print(type(add_Student))

updateid = int(input("enter the student id you want to update"))

updatedEmail= input("Enter the new email of student: ")

def updateStudent (students):
    if students["id"]==updateid:
        return
    {"id" : students["id"],
        "name" : students["name"],
        "email" : updatedEmail,
        "rollNo" : students["rollno"],
        "class" : students["class"]
        
    }

      

