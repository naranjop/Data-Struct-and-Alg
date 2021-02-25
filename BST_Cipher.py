#  File: BST_Cipher.py

#  Description: Encrypt and Decrypt different strings using the given key.

#  Date Created: 11/16/2020

#  Date Last Modified: 11/16/2020

import sys

class Node (object):
    def __init__ (self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class Tree (object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__ (self, encrypt_str):
        encrypt_str = convert_lower(encrypt_str)
        self.root = Node(encrypt_str[0])
        for i in range(1, len(encrypt_str)):
            self.insert(encrypt_str[i])


    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.
    def insert (self, ch):
        current = self.root
        next = current
        # Go through tree until find the right spot
        while next != None: 
            current = next
            if current.data == ch:
                return
            elif ch < current.data:
                next = current.lchild
            else:
                next = current.rchild

        # Create new node
        if ch < current.data:
            current.lchild = Node(ch)
        else:
            current.rchild = Node(ch)


    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search (self, ch):
        output = ''
        if self.root.data == ch: return '*'
        current = self.root
        while current != None and current.data != ch:
            if ch < current.data:
                output += '<'
                current = current.lchild
            else:
                output += '>'
                current = current.rchild
        if current == None: return ' '
        return output


    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding 
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse (self, st):
        if st == '*': return self.root.data
        current = self.root
        # Go through tree until find the right spot
        index = 0
        while current != None and index < len(st):
            if st[index] == '<':
                current = current.lchild
            else:
                current = current.rchild
            index += 1
        if current == None:
            return ''
        return current.data


    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt (self, st):
        st = convert_lower(st)
        encr = ''
        for ch in st:
            encr += self.search(ch) + '!'
        encr = encr.rstrip('!')
        return encr
      

    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt (self, st):
        decr = ''
        st = st.split('!')
        for ch in st:
            decr += self.traverse(ch)
        return decr
    

def convert_lower(encrypt_str):
    encrypt_str = encrypt_str.lower()
    new_str = ''
    for i in range(len(encrypt_str)):
        if encrypt_str[i].isalpha():
            new_str += encrypt_str[i]
    return new_str


def main():
  # read encrypt string
  line = sys.stdin.readline()
  encrypt_str = line.strip()

  # create a Tree object
  the_tree = Tree (encrypt_str)

  # read string to be encrypted
  line = sys.stdin.readline()
  str_to_encode = line.strip()

  # print the encryption
  print (the_tree.encrypt(str_to_encode))

  # read the string to be decrypted
  line = sys.stdin.readline()
  str_to_decode = line.strip()
  
  # print the decryption
  print (the_tree.decrypt(str_to_decode))
 
if __name__ == "__main__":
  main()