"""
This is where the actual working of the program will happen!
We'll be Querying stuff for testing whether your classes were defined correctly

Whenever something inappropriate happens (like a function returning false in people.py),
raise a Value Error.
"""

from people import * # import everything!

if 1 == 1:
    last_input = 99
    while last_input != 0:
        last_input = int(input("Please enter a query number: "))

        if last_input == 1:
            name = input("Name: ")
            age = int(input("Age: "))
            ID = int(input("ID: "))
            city = input("City: ")
            branchcodes = input("Branch(es): ")  # e.g., user enters "2, 5"
            branches = [int(code.strip()) for code in branchcodes.split(",")]  # Split, strip whitespace, and convert to int
            salary = input("Salary: ")
            position = input("Position: ")
            engineer = Engineer(name, age, ID, city, branches, position, salary)

            engineer_roster.append(engineer) # Add him to the list! See people.py for definiton
            
        
        elif last_input == 2:
            # Gather input to create a Salesperson
            # Then add them to the roster
            name = input("Name: ")
            age = int(input("Age: "))
            ID = int(input("ID: "))
            city = input("City: ")
            branchcodes = input("Branch(es): ")  # e.g., user enters "2, 5"
            branches = [int(code.strip()) for code in branchcodes.split(",")]  # Split, strip whitespace, and convert to int
            salary = input("Salary: ")
            position = input("Position: ")
            superior = input("Superior: ")
            if len(superior) == 0:
                superior = None
            salesman = Salesman(name, age, ID, city, branches, position, salary, superior) 
            sales_roster.append(salesman) # Add him to the list! See people.py for definiton

        elif last_input == 3:
            ID = int(input("ID: "))
            # Print employee details for the given employee ID that is given. 
            
            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == int(ID):
                    found_employee = employee
                    break
            
            if not found_employee: print("No such employee")
            else:
                print(f"Name: {found_employee.name} and Age: {found_employee.age}")
                print(f"City of Work: {found_employee.city}")
                br_list = []
                br = []
                br = found_employee.branches 
                
                for i in br:
                    br_list.append(branchmap[i]["name"])
                comma_separated_string = ", ".join(br_list) # Convert the list to a comma-separated string
                #print(comma_separated_string) # Print the resulting string
                print(f"Branches: " + comma_separated_string)
                print(f"Salary: {found_employee.salary}")

                print(f"position: {found_employee.position}")

               

        elif last_input == 4:
            #### NO IF ELSE ZONE ######################################################
            # Change branch to new branch or add a new branch depending on class
            # Inheritance should automatically do this. 
            # There should be no IF-ELSE or ternary operators in this zone
            ID = int(input("enter id: "))
            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == int(ID):
                    found_employee = employee
                    break
            new_code = int(input("enter branchcode: "))

            found_employee.migrate_branch(new_code)

            #### NO IF ELSE ZONE ENDS #################################################

        elif last_input == 5:
            ID = int(input("Enter Employee ID to promote: "))
            # promote employee to next position
            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == int(ID):
                    found_employee = employee
                    break
            
            if not found_employee: print("No such employee")
            else:
                found_employee.promote(found_employee.ID)
  
        elif last_input == 6:
            ID = int(input("Enter Employee ID to give increment: "))
            increment_amt = int(input("Enter increment amt: "))
            # Increment salary of employee.
            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == int(ID):
                    found_employee = employee
                    break
            found_employee.increment(increment_amt)
        
        elif last_input == 7:
            ID = int(input("Enter Employee ID to find superior: "))
            # Print superior of the sales employee.
            found_employee = None
            for employee in sales_roster:
                if employee.ID == int(ID):
                    found_employee = employee
                    break
            k1 = found_employee.find_superior()
            print(k1[1]) 
            
        elif last_input == 8:
            ID_E = int(input("Enter Employee ID to add superior: "))
            ID_S = int(input("Enter Employee ID of superior: "))
            # Add superior of a sales employee
            found_employee = None
            for employee in engineer_roster + sales_roster:
                if employee.ID == int(ID_E):
                    found_employee = employee
                    break
            found_employee.add_superior(ID_E, ID_S)

        else:
            raise ValueError("No such query number defined")


            

            


            


        






