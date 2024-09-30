class Seat:
    def __init__(self):
        self.free=True
        self.occupant=""

    def __str__(self):
        return "This is a seat class created with the attributes free and occupant"
    
    def set_occupant(self,name:str):
        """This function is used to assign a seat to an occupant if it is free."""
        if self.free==True:
            self.occupant=name
            self.free=False
        
    
    def remove_occupant(self)->str:
        """This function removes an occupant and returns their name."""
        self.free="True"
        name=self.occupant
        self.occupant=""
        return name



class Table:
    def __init__(self, capacity:int):
        self.capacity=capacity
        self.seats=[]
        for i in range(capacity):
            s=Seat()
            self.seats.append(s)
    
    def __str__(self):
        return "This is a table class created with the attributes capacity and seats"
    
    def has_free_spot(self)->bool:
        """This function checks if a spot is available"""
        for s in self.seats:
            if s.free==True:
                return True
        
        return False
        

    
    def assign_seat(self,name:str):
        """This function assigns a seat"""
        
        for s in self.seats:
            if s.free==True:
                s.set_occupant(name)
                break

                
        
    def left_capacity(self)->int:
        """This function returns the spaces left at the table as an integer"""
        left=0
        for s in self.seats:
            if s.free == True:
                left+=1
        return left