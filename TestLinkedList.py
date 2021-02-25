#  File: TestLinkedList.py

#  Description: LinkedList class defined and tested.

#  Date Created: 11/03/2020

#  Date Last Modified: 11/06/2020


class Link (object):
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList (object):
    # create a linked list
    def __init__ (self):
        self.first = None


    # get number of links 
    def get_num_links (self):
        current = self.first

        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    
    # add an item at the beginning of the list
    def insert_first (self,data):
        new_link = Link(data)
        new_link.next = self.first
        self.first = new_link 


    # add an item at the end of a list
    def insert_last(self,data):
        new_link = Link(data)
        current = self.first
        if(current == None):
            self.first = new_link
            return
        while (current.next != None):
            current = current.next
        current.next = new_link


    # add an item in an ordered list in ascending order
    def insert_in_order (self, data): 
        previous = self.first
        current = self.first
        new_link = Link(data)

        if (current == None) or (new_link.data <= current.data):
            self.insert_first(new_link.data)
            return
            
        while current.next != None:
            if new_link.data > current.data:
                previous = current
                current = current.next
            else:
                previous.next = new_link
                new_link.next = current
                return
        
        if current == self.first:
            self.insert_first(new_link.data)
            return
        else:
            self.insert_last(new_link.data)
            return


    # search in an unordered list, return None if not found
    def find_unordered (self, data): 
        current = self.first
        if (current == None):
            return None
        while (current.data != data):
            if (current.next == None):
                return None
            else:
                current = current.next
        return current


    # Search in an ordered list, return None if not found
    def find_ordered (self, data): 
        current = self.first
        if (current == None):
            return None
        while (current.data != data):
            if (current.next == None):
                return None
            else:
                if current.next.data > data:
                    return None
                current = current.next
        return current


    # Delete and return Link from an unordered list or None if not found
    def delete_link (self, data):
        previous = self.first
        current = self.first
        if (current == None):
            return None
        while (current.data != data):
            if (current.next == None):
                return None
            else:
                previous = current
                current = current.next
        if (current == self.first):
            self.first = self.first.next
        else:
            previous.next = current.next
        return current


    # String representation of data 10 items to a line, 2 spaces between data
    def __str__ (self):
        current = self.first

        result = ''
        counter = 0
        while (current != None):
            result += str(current.data)
            counter += 1

            if (counter != 0) and (counter % 10 == 0):
                result += '\n'
            else:
                result += '  '

            current = current.next

        return result


    # Copy the contents of a list and return new list
    def copy_list (self):
        copyList = LinkedList()
        current = self.first

        while current != None:
            copyList.insert_last(current.data)

            current = current.next

        return copyList


    # Reverse the contents of a list and return new list
    def reverse_list (self):
        current = self.first
        result = LinkedList()
        while current != None:
            result.insert_first(current.data)
            current = current.next
        return result


    # Sort the contents of a list in ascending order and return new list
    def sort_list (self): 
        pass

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted (self):
        current = self.first
        while current != None:
            if current.data > current.next.data:
                return False
            current = current.next
        return True

    # Return True if a list is empty or False otherwise
    def is_empty (self): 
        return (self.first == None)

    # Merge two sorted lists and return new list in ascending order
    def merge_list (self, other):
        current = other.first
        mergedList = self.copy_list()
        while current != None:
            mergedList.insert_in_order(current.data)
            current = current.next
        return mergedList()
            

    # Test if two lists are equal, item by item and return True
    def is_equal (self, other):
        current1 = self.first
        current2 = other.first
        while current1 != None and current2 != None:
            if current1.data != current2.data:
                return False
            current1 = current1.next
            current2 = current2.next
        if current1 != None or current2 != None:
            return False
        return True

    
    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates (self):
        new_list = self.copy_list()
        previous = new_list.first
        current = previous.next
        memo = []
        memo.append(previous.data)
        while current != None:
            if current.data not in memo:
                memo.append(current.data)
                previous = current
                current = current.next
            else:
                previous.next = current.next
                current = previous.next
        return new_list 
        
        
def main():
    testLinkedList = LinkedList()
    print()
    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    for i in range(20, 0, -1):
        testLinkedList.insert_first(i)
    print('Testing for insert_first()')
    print(testLinkedList, '\n')
    
    # Test method insert_last()
    for i in range(31, 51, 1):
        testLinkedList.insert_last(i)
    print('Testing for insert_last()')
    print(testLinkedList, '\n')

    # Test method insert_in_order()
    print('Testing for insert_in_order()')
    testLinkedList.insert_in_order(-10)
    testLinkedList.insert_in_order(25)
    testLinkedList.insert_in_order(55)
    print(testLinkedList, '\n')

    # Test method get_num_links()
    print('Testing for get_num_links()')
    numLinks = testLinkedList.get_num_links()
    print('The total number of the links is', numLinks, '\n')

    # Test method find_unordered() 
    # Consider two cases - data is there, data is not there 
    print('Testing for find_unordered()')
    for num in [25, 60]:
        if testLinkedList.find_unordered(num) != None:
            print('Yes =>', num)
        else:
            print('No =>', num)
    print()

    # Test method find_ordered() 
    # Consider two cases - data is there, data is not there 
    print('Testing for find_ordered()')
    for num in [25, 60]:
        if testLinkedList.find_ordered(num) != None:
            print('Yes =>', num)
        else:
            print('No =>', num)
    print()

    # Test method delete_link()
    # Consider two cases - data is there, data is not there 
    print('Testing for delete_link()')
    for num in [-10, 60]:
        if testLinkedList.delete_link(num)!=None:
            print(num,'is deleted, below is the new LinkedList')
            print(testLinkedList, '\n')
        else:
            print(num,' is not there') 
    print()

    # Test method copy_list()
    print('Testing for copy_list()')
    testLinkedList.insert_in_order(99)
    testLinkedList.insert_in_order(-99)

    newList = testLinkedList.copy_list()

    testLinkedList.delete_link(99)
    testLinkedList.delete_link(-99)

    print(testLinkedList, '\n')
    print(newList, '\n')
    print()

    # Test method reverse_list()
    print('Testing for reverse_list()')
    print(testLinkedList, '\n')
    print(testLinkedList.reverse_list(), '\n')

    # Test method sort_list()

    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted

    # Test method is_empty()

    # Test method merge_list()

    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal

    # Test remove_duplicates()

if __name__ == "__main__":
    main()