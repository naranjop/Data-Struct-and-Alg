#  File: Josephus.py

#  Description: CircularList class is defined and used to solve
#  Josephus problem.

#  Date Created: 11/10/20

#  Date Last Modified: 11/11/20


import sys

class Link(object):
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next


class CircularList(object):
    # Constructor
    def __init__ ( self ):
        self.last = None


    # Insert an element (value) in the list
    def insert ( self, data):
        new_link = Link(data)
        if self.last == None:
            self.last = new_link
            self.last.next = self.last
        else:
            current = self.last
            while current.next != self.last:
                current = current.next
            current.next = new_link
            new_link.next = self.last


    # Find the link with the given data (value)
    def find ( self, data ):
        current = self.last
        while current.data != data:
            current = current.next
        return current


    # Delete a link with a given data (value)
    def delete ( self, data ):
        previous = self.last
        current = previous.next
        while current.data != data:
            previous = current
            current = current.next
        if current.data == self.last.data:
            new_last = previous.data
            self.delete(previous.data)
            current.data = new_last
        else:
            previous.next = current.next
            current.next = None
            current.data = None


    # Delete the nth link starting from the Link start 
    # Return the next link from the deleted Link
    def delete_after ( self, start, n ):
        current = self.find(start)
        for i in range(n - 1):
            current = current.next
        next_link = current.next
        print(current.data)
        self.delete(current.data)
        return next_link.data


    # Return a string representation of a Circular List
    def __str__ ( self ):
        current = self.last
        last_string = str(current.data)
        string = ''
        while current.next != self.last:
            string += str(current.next.data)
            current = current.next
        return (string + last_string)
            

def main():
    # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int (line)
  
    # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int (line)

    # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int (line)

    # soldier elimination
    print()
    Circle = CircularList()
    for i in range(num_soldiers):
        Circle.insert(i + 1)
    while Circle.last.next != Circle.last:
        start_count = Circle.delete_after(start_count, elim_num)
    print(Circle.last.data)


if __name__ == "__main__":
    main()