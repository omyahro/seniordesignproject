#Source from Zybooks 4.6

from Node import Node
from LinkedList import LinkedList

import random
outfile = open('students.txt', 'w')

for x in range(100):
  num = random.randint(900000000,900999999)
  outfile.write(str(num)+'\n')

outfile.close()
 
students=LinkedList()
infile = open('students.txt', 'r')

y = infile.readline()
while y!= '':
  node_x = Node(y)
  students.append(node_x)
  y  = infile.readline()
students.print()


attempts = 'A'

while attempts == 'A':
  search = input("Enter Student ID:")
  found = students.ListSearch(students, search)
  if found != None:
    print('Student ID:', found, 'Found')
  else:
    print('Student ID Not Found. Try Again Below')
   
  attempts = input("Enter A to try again:")
 
  
