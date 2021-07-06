import timeit
from Stack import Stack

def Hanoi_rec(n, s, a, d):
  print(n, s, a, d)
  # TODO replace pass with your base and recursive cases.
  if n==0:        #base case: if there's a single disk
    d.push(s.pop())   #push from source to destination
  else:
    Hanoi_rec(n-1, s, d, a)   #solve for n-1 where auxiliary and destination are swapped
    if len(s) != 0:         #if there's something in the source stack
      d.push(s.pop())     #push that disc to destination
    Hanoi_rec(n-1, a, s, d) #solve for n-1 where auxiliary and source are swapped
  

  
  print(n, s, a, d)
  print()
  

def Hanoi(n):
  source = Stack()
  dest = Stack()
  aux = Stack()
  i = n-1
  while i >= 0:
    source.push(i)
    i = i - 1
  Hanoi_rec(n-1, source, aux, dest)

if __name__ == "__main__":
  n=5  
  runtime = timeit.timeit("Hanoi(n)", setup="from __main__ import Hanoi,n", number=1)
  print("computed Hanoi(" + str(n) + ") in " + str(runtime) + " seconds.")
  