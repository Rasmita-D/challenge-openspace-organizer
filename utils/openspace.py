from .file_utils import *
from .table import Table
import random

class OpenSpace:
    def __init__(self,number_of_tables:int, number_of_seats) -> None:
        self.tables=[]
        for i in range(number_of_tables):
            t=Table(number_of_seats)
            self.tables.append(t)
        self.number_of_tables=number_of_tables
        self.number_of_seats=number_of_seats
    
    def __str__(self) -> str:
        """This is an openspace class"""

    
    def organize(self,names):
        """This function is used to randomly assign seats"""
        for i in range(self.number_of_seats*self.number_of_tables):
            while True:
                picked_table=random.choice(self.tables)
                if(picked_table.has_free_spot()):
                    picked_table.assign_seat(names[i])
                    break
            if(i==len(names)-1):
                break
        
        for t in self.tables:
            t.seats[0].occupant= str(t.seats[0].occupant)+" - Leader"
        global overflow 
        overflow = len(names)-self.number_of_tables*self.number_of_seats 

        
    
    def display(self):
        """Display tables and their occupants"""
        remaining=0
        
        for t in self.tables:
            remaining+=t.left_capacity()
            print("Table"+" "+str(self.tables.index(t)+1))
            for s in t.seats:
                if s.occupant!="":
                    str
                    print(s.occupant)
            print("")
        
        if(overflow>0):
            print("No seats remaining for "+str(overflow)+" members!!")
        else:
            print(str(remaining)+" spots remaining!")
                



    
    def store(self,filename):
        """Store the repartition in an excel file"""
        distributed_string=""
        for t in self.tables:
            
            distributed_string =distributed_string+"Table"+" "+str(self.tables.index(t)+1)
            for s in t.seats:
                if s.occupant!="":
                    distributed_string =distributed_string+", "+s.occupant
            distributed_string =distributed_string+"\n"
        write_names_to_file(distributed_string,filename)

