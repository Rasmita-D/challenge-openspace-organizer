from utils import file_utils
from utils.openspace import OpenSpace

input_filepath = "new_colleagues.csv"
output_filename = "output.csv"

# Creates a list that contains all the colleagues names
names = file_utils.read_names_from_csv(input_filepath)

#Take the number of seats and tables as an input from the user
number_of_tables=int(input("Please enter number of tables: "))
number_ofseats=int(input("Please enter number of seats in each table: "))

# create an OpenSpace() 
open_space = OpenSpace(number_of_tables,number_ofseats)

# assign a colleague randomly to a table
open_space.organize(names)

# save the seat assigments to a new file
open_space.store(output_filename)

# display assignments in the terminal
open_space.display()


new_members=[]
if open_space.get_remaining()>0:
    add_members=input("Do you want to add more members? Y/N: ")

    if add_members=='Y':
        new_members=input("Please enter the names separated by a comma: ")
        list_new_members=new_members.split(",")
        for i in list_new_members:
            names.append(i)
       
        open_space.add_members(list_new_members)
        open_space.display()
        open_space.store(output_filename)


reassign=input("Do you want to change the number of tables,seats to reassign? Y/N: ")

while reassign=='Y':
    #Take the number of seats and tables as an input from the user
    number_of_tables=int(input("Please enter number of tables: "))
    number_ofseats=int(input("Please enter number of seats in each table: "))

    # create an OpenSpace() 
    open_space = OpenSpace(number_of_tables,number_ofseats)

    # assign a colleague randomly to a table
    if new_members!=[]:
        open_space.organize(names)
    else:
        open_space.organize(names)

    # save the seat assigments to a new file
    open_space.store(output_filename)

    # display assignments in the terminal
    open_space.display()

    reassign=input("Do you want to change the number of tables, seats and reassign? Y/N: ")