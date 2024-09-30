from .file_utils import *
from .table import Table
import random

class OpenSpace:
    def __init__(self,number_of_tables:int, number_of_seats:int) -> None:
        self.tables=[]
        for i in range(number_of_tables):
            t=Table(number_of_seats)
            self.tables.append(t)
        self.number_of_tables=number_of_tables
        self.number_of_seats=number_of_seats
    
    def __str__(self) -> str:
        """This is the openspace class"""

    
    def organize(self,names):
        """This function is used to randomly assign seats"""
        #Looping the seats and picking a table at random for each member of the list
        
        for i in range(self.number_of_seats*self.number_of_tables):
            while True:
                picked_table=random.choice(self.tables)
                if(picked_table.has_free_spot()):
                    picked_table.assign_seat(names[i])
                    break
            #if there are more seats than number of members, this condition breaks when all members are assigned
            if(i==len(names)-1):
                break
        
        #Marking the first person who entered a table as the leader
        for t in self.tables:
            if t.left_capacity()!=self.number_of_seats:
                t.seats[0].occupant= str(t.seats[0].occupant)+" - Leader"
                
        global overflow 
        overflow = len(names)-self.number_of_tables*self.number_of_seats 
        


    def get_remaining(self):
        #Looping through the seats of each table to get the remaining seats
        remaining=0
        for t in self.tables:
            remaining+=t.left_capacity()
            
        return remaining   
                    
                    

    
    def display(self):
        """Display tables and their occupants"""
        remaining=0
        
        #Looping through the seats of each table and printing the seats assigned
        for t in self.tables:
            remaining+=t.left_capacity()
            print("Table"+" "+str(self.tables.index(t)+1))
            for s in t.seats:
                if s.occupant!="":
                    print(s.occupant)
            print("")
        
        #Overflow is used to handle extra members
        if(overflow>0):
            print("No seats remaining for "+str(overflow)+" members!!")
        print(str(remaining)+" spots remaining!")
                



    
    def store(self,filename):
        """Store the repartition in an excel file"""

        #Creating a csv of each table and storing it in a file using the utility function
        distributed_string=""
        for t in self.tables:
            
            distributed_string =distributed_string+"Table"+" "+str(self.tables.index(t)+1)
            for s in t.seats:
                if s.occupant!="":
                    distributed_string =distributed_string+", "+s.occupant
            distributed_string =distributed_string+"\n"
        write_names_to_file(distributed_string,filename)


    def add_members(self,names):
        random.shuffle(names)
        i=0
        for i in range(len(names)):
            for t in self.tables:
                if t.has_free_spot():
                    t.assign_seat(names[i])
                    break
            
    def no_alone(self,names):
        #Not a working logic for making sure there are no people sitting by themselves, must be developed and tested
        table_members=[]
        for t in self.tables:
            if self.number_of_seats-t.left_capacity()==1:
                table_members.append(t)
        
        if len(table_members)==0:
            return
        
        else:
            reassigned=0
            i=0
            for t in self.tables:
                if t not in table_members and i<len(table_members):
                    if t.left_capacity!=0:
                        name = table_members[i].seats[0].remove_occupant()
                        t.assign_seat
                        reassigned+=1
                        table_members.remove(table_members[i])
                        i+=1
            
            



                    
                



