"""
We'll try to understand classes in python. 
Check the resources on google classroom to ensure you have gone through everything expected.

"""
###### THESE LISTS HAVE ALREADY BEEN DEFINED FOR YOU ###############
engineer_roster = [] # A list of all instantiated engineer objects
sales_roster = [] # List of all instantiated sales objects
branchmap = {  # A dictionary of dictionaries -> Maps branchcodes to cities and branch names
    0:  { "city": "NYC", "name": "Hudson Yards"},
    1:  { "city": "NYC" , "name": "Silicon Alley"},
    2:  { "city": "Mumbai", "name": "BKC"},
    3:  { "city": "Tokyo", "name": "Shibuya"},
    4:  { "city": "Mumbai", "name": "Goregaon"},
    5:  { "city": "Mumbai", "name": "Fort"}
}

####################################################################



class Employee:
    name : str 
    age : int
    ID : int
    city : str
    branches : list[int] # This is a list of branches (as branch codes) to which the employee may report
    salary : int 

    def __init__(self, name, age, ID, city,\
                 branchcodes, salary = None):
        self.name = name
        self.age = age 
        self.ID = ID
        self.city = city
        self.branches = branchcodes
        if salary != '':
            self.salary = salary
        else: self.salary = 10000 
    
    def change_city(self, new_city:str) -> bool:
        new_city = input("enter city name: ")
        if (new_city == self.city):
            return False
        else:
            return True
    
    def migrate_branch(self, new_code:int) -> bool:
        # Should work only on those employees who have a single 
        # branch to report to. Fail for others.
        # Change old branch to new if it is in the same city, else return false.
        if (len(self.branches)==1):
            old_code = self.branches[0]
            if (branchmap[new_code]["city"] == branchmap[old_code]["city"]):
                self.branches=[new_code]
                return True
            else:
                return False
        else:
            return False
    
    def increment(self, increment_amt: int) -> None:
        increment_amt = input("enter increment amount: ")
        self.salary = self.salary + increment_amt
    

class Engineer(Employee):
    position : str # Position in organization Hierarchy
    predef_pos = ["Junior", "Senior", "Team Lead", "Director"]

    def __init__(self, name, age, ID, city,\
                 branchcodes, position= "Junior", salary = 10000):
        # Call the parent's constructor
        super().__init__(name, age, ID, city, branchcodes, salary)
        # Check if position is one of  "Junior", "Senior", "Team Lead", or "Director" 
        # Only then set the position. 
        if position in self.predef_pos:
            self.position = position
        else:
            self.position = "Junior"
    
    def increment(self, amt:int) -> None:
        # While other functions are the same for and engineer,
        # and increment to an engineer's salary should add a 10% bonus on to "amt"
        self.salary = float(self.salary) + 0.1 * float(amt)

    def find_pos(self, id: int) -> str:
        #function for matching ID to position
        for e in engineer_roster:
            if e.ID == id:
                return e.position

    def promote(self, ID:int) -> bool:
        # Return false for a demotion or an invalid promotion
        # Promotion can only be to a higher position and
        # it should call the increment function with 30% of the present salary
        # as "amt". Thereafter return True.
        #assuming demotion==invalid promotion-yt
        current_pos = self.find_pos(ID)
        i = self.predef_pos.index(current_pos)
        if i < (len(self.predef_pos) - 1):
            promoted_index = i + 1
            promoted_pos = self.predef_pos[promoted_index]
            self.position = promoted_pos
            return True
        else:
            print("employee can't be promoted")
   
    def __repr__(self):
        return f"name: {self.name}, age: {self.age}, id: {self.ID}, city: {self.city}, branchcodes: {self.branches}, position: {self.position}, salary: {self.salary}"
   

class Salesman(Employee):
    position : str # Position in organization Hierarchy
    superior : int # EMPLOYEE ID of the superior this guy reports to
    predef_pos = ["Rep", "Manager", "Head"]
    def __init__(self, name, age, ID, city,\
                 branchcodes, position= "Rep", salary = None, superior = None):
        # Call the parent's constructor
        super().__init__(name, age, ID, city, branchcodes, salary)
        # Check if position is one of  "Rep", "Manager" or "Head" 
        # Only then set the position. 
        if position in self.predef_pos:
            self.position = position
        else:
            self.position = "Rep"
        # if position is Head, no superior; else, superior id is valid-yt
        # check whether id exists-yt
        # check whether the superior is valid-yt
        if (self.position != "Head"):
            self.superior = superior
        else:
            self.superior = None
    
    def increment(self, amt:int) -> None:
        # Add increment (this time only a 5% bonus)
        self.salary = float(self.salary) + 0.05 * float(amt)

    def find_pos(self, id: int) -> str:
        #function for matching ID to position
        for s in sales_roster:
            if s.ID == id:
                return s.position

    def promote(self, ID:int) -> bool:
        # Return false for a demotion or an invalid promotion
        # Promotion can only be to a higher position and
        # it should call the increment function with 30% of the present salary
        # as "amt". Thereafter return True.
        #assuming demotion==invalid promotion-yt
        current_pos = self.find_pos(ID)
        i = self.predef_pos.index(current_pos)
        if i < (len(self.predef_pos) - 1):
            promoted_index = i + 1
            promoted_pos = self.predef_pos[promoted_index]
            self.position = promoted_pos
            self.salary = float(self.salary) + 0.3 * float(self.salary) #any specifications on increment for sales? -yt
            return True
        else:
            print("employee can't be promoted")

    
    def find_superior(self) -> tuple[int, str]:
        # Return the employee ID and name of the superior
        # Report a tuple of None, None if no superior.
        j=0
        if self.position == "Head":
            print('superior is none.')
            k = [self.ID, None]
            
        elif self.position == "":
            if int(self.superior) == int(s.ID):
                    k = [int(s.ID), s.name]
                    
        else:
            for index, s in enumerate(sales_roster):
                if int(self.superior) == int(s.ID):
                    k = [int(s.ID), s.name]
                    break
        return k


    def add_superior(self, ID_E: int, ID_S: int) -> bool:
        # Add superior of immediately higher rank.
        # If superior doesn't exist return false,
        #in main.py, the only inputs are IDs of employee and salesman-yt
     
        if self.position == "Head":
            print('salesman cannot have a superior')
            return False #salesman cannot have a superior
        else:
            m = self.predef_pos.index(self.find_pos(ID_E))
            n = self.predef_pos.index(self.find_pos(ID_S))
            if n>m:
                self.superior = ID_S
                return True
            else:
                return False #incompatible ids or id entered is invalid     '''    

    def migrate_branch(self, new_code: int) -> bool:
        # This should simply add a branch to the list; even different cities are fine
        list_branches = self.branches
        list_branches.append(new_code)
        return True


    def __repr__(self):
        return f"name: {self.name}, age: {self.age}, id: {self.ID}, city: {self.city}, branchcodes: {self.branches}, position: {self.position}, superior: {self.superior}, salary: {self.salary}"
        