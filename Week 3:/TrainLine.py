# Week 3: Train Line
class Station:
    
    def __init__(self, name: str)-> None:
        self.name = name
        self.next = None

    # ----- Mutators -----

    def set_next(self, station)-> None:
        self.next = station

    def set_name(self, new_name: str) -> None:
        self.name = new_name

    # ----- Acessors -----

    def get_next(self):
        return self.next

    def get_name(self):
        return self.name

    def has_next(self)-> bool:
        return self.next != None

class TrainLine:

    def __init__(self, name: str)-> None:
        self.name = name
        self.head = None

    # ----- Acessors & Mutators ----
    def get_name(self)-> str:
        return self.name

    def is_empty(self)-> bool:
        return self.head == None

    #----- add new station ----

    def add_station(self, new_station):
        if self.head == None:
            # Line is empty; new station becomes the head of the line
            self.head = station
        else:
            # traverse the line to find its last station
            cursor = self.head
            while cursor.has_next():
                cursor = cursor.get_next()
            # When this loops ends its because cursor.has_next is False,
            # Therefore we are standing at the end of the line
            cursor.set_next(new_station)