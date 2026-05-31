print("---------Graphs----------")
#if a graph is complete or almost complete we should use adjacency matrix
class Graph :
    def __init__(self):
        self.adjacency_list = {}
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    def add_edge(self , vertex1 , vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            return True 
        return False
    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for other_vertex in self.adjacency_list.keys():
                if vertex in self.adjacency_list[other_vertex]:
                    self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False 
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":" ,self.adjacency_list[vertex])
            
mygraph = Graph()
mygraph.add_vertex("A")
mygraph.add_vertex("B")
mygraph.add_vertex("C")
mygraph.add_vertex("D")
mygraph.add_vertex("E")
mygraph.add_edge("A" , "B")
mygraph.add_edge("A","C")
mygraph.add_edge("A","D")
mygraph.add_edge("B","A")
mygraph.add_edge("B","E")
mygraph.add_edge("D","A")
mygraph.add_edge("D","C")
mygraph.add_edge("D","E")
mygraph.add_edge("C","A")
mygraph.add_edge("E","B")
mygraph.add_edge("C","D")

mygraph.remove_vertex("D")

mygraph.print_graph()
print()

print("---------Static Method----------")
class Student :
    @staticmethod
    def get_personal_details(firstname , lastname):
        print("Your personal details : " , firstname,lastname)
    @staticmethod
    def contact_details(mobile_no , roll_no):
        print("Your contact details : " , mobile_no , roll_no)
        
Student.get_personal_details("Prashant","Jha")
Student.contact_details(9521563654 , 1011)
print()

print("--------SINGLE INHERITANCE---------")
class College:
    def college_name(self):
        print("RBU")
        
class Student(College):
    def Student_info(self):
        print("Name : Apurva Pande")
        print("Branch : MCA")
        
obj = Student()
obj.college_name()
obj.Student_info()
print()

print("---------MULTI-LEVEL INHERITANCE---------")
class College:
    def college_name(self):
        print("RBU")
        
class Student(College):
    def Student_info(self):
        print("Name : Apurva Pande")
        print("Branch : MCA")
        
class Exam(Student):
    def subject(self):
        print("Subject1 : OR")
        print("Subject2 : Math")
        
obj1 = Exam()
obj1.college_name()
obj1.Student_info()
obj1.subject()
print()

print("----------MULTIPLE INHERITANCE-----------")
class Submarks:
    math = int(input("Enter marks of maths : "))
    DE = int(input("Enter marks of DE : "))

class PractMarks :
    cpract = int(input("Enter practical marks of DE : "))

class result(Submarks,PractMarks):
    def total(self):
        if self.math >= 40 and self.DE >= 40 and self.cpract >= 20 :
            print("Pass")
        else:
            print("Fail")

obj2 = result()
obj2.total()
print()

print("---------AMBIGUITY---------")
class Submarks:
    def display(self):
        print("Submarks")

class PractMarks:
    def display(self):
        print("PractMarks")

class Result(Submarks, PractMarks):
    pass

obj = Result()
obj.display()
print()

print("----------POLYMORPHISM : METHOD OVERRIDING------------")
class Rbi:
    def home_loan(self):
        print("Home Loan ROI = 8%")
    def edu_loan(self):
        print("Education loan ROI = 9%")

class Sbi:
    def edu_loan(self):
        print("Education Loan ROI = 7.5%")
        
obj4 = Sbi()
obj4.edu_loan()
obj5 = Rbi()
obj5.home_loan()
obj5.edu_loan() 
print()

print("---------CONSTRUCTOR OVERLOADING-----------")
class Student:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age
    def display(self):
        print("Name :", self.name)
        print("Age :", self.age)

# Object 1
s1 = Student()
s1.display()
print()
# Object 2
s2 = Student("Apurva", 24)
s2.display()
print()
# Object 3
s3 = Student("Apurva", 20)
s3.display()
print()
