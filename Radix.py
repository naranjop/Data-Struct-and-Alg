#  File: Radix.py

#  Description: Takes in file with words composed of lower case
#  letters and numbers and sorts strings in ascending order 
#  using radix sort and returns list.

#  Date Created: 11/02/2020

#  Date Last Modified: 11/02/2020

import sys

class Queue (object):
    def __init__ (self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue (self, item):
        self.queue.append (item)

    # remove an item from the beginning of the queue
    def dequeue (self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty (self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size (self):
        return (len(self.queue))


# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort (a):
    queue_list = []
    ch_dict = {}
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',\
                'o','p','q','r','s','t','u','v','w','x','y','z']
    # Change strings so they are all same size
    # (add blank space to the right if not)
    max_len = 0
    for ele in a:
        if len(ele) > max_len:
            max_len = len(ele)
    for i in range(len(a)):
        if len(a[i]) < max_len:
            add_str = ' ' * (max_len - len(a[i]))
            a[i] = a[i] + add_str
    # Add queues to list and key value pairs to dictionary
    ch_dict[' '] = 0
    new_queue = Queue()
    queue_list.append(new_queue)
    for i in range(36):
        new_queue = Queue()
        queue_list.append(new_queue)
        if i < 10:
            ch_dict[str(i)] = i + 1
        else:
            ch_dict[alphabet[i - 10]] = i + 1
    for j in range(1, max_len + 1):
        a = do_pass(a, -j, queue_list, ch_dict)
    for i in range(len(a)):
        a[i] = a[i].strip()
    return a
    

def do_pass(a, index, queue_list, ch_dict):
    # place in appropriate queue
    for elem in a:
        queue_list[ch_dict[elem[index]]].enqueue(elem)

    # dequeue numbers starting from first queue and enqueue in new queue
    list_result = []
    for i in range(len(queue_list)):
        while not queue_list[i].is_empty():
            list_result.append(queue_list[i].dequeue())
    return list_result


def main():
    # read the number of words in file
    line = sys.stdin.readline()
    line = line.strip()
    num_words = int (line)

    # create a word list
    word_list = []
    for i in range (num_words):
        line = sys.stdin.readline()
        word = line.strip()
        word_list.append (word)

    '''
    # print word_list
    print (word_list)
    '''

    # use radix sort to sort the word_list
    sorted_list = radix_sort (word_list)

    # print the sorted_list
    print (sorted_list)

if __name__ == "__main__":
    main()
