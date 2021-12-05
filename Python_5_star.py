'''
 Hackranker Python Solution  for 5 Star 
 ----------------------------------------------------------------------------------------------------------------------------
 Challenge 1 - 
 
 print("Hello, World!")
 
 ----------------------------------------------------------------------------------------------------------------------------
  Challenge 2 -
  
  n=int(input())
if (n%2!=0):
    print("Weird")
else:
    if n>=2 and n<=5:
        print("Not Weird")
    elif n>=6 and n<=20:
        print("Weird") 
    elif n>20:       
        print("Not Weird")     
 
 ----------------------------------------------------------------------------------------------------------------------------
 Challenge 3 -
 
 a=int(input())
 b=int(input())
 print(a+b)
 print(a-b)
 print(a*b)
 
 ------------------------------------------------------------------------------------------------------------------------------
 Challenge 4 -
 
a = int(input())
b = int(input())
print(a//b)
print(a/b)

----------------------------------------------------------------------------------------------------------------------------------------------------------
Challenge 5 -

n = int(input())
for i in range(0,n):
    print(i*i)
    
--------------------------------------------------------------------------------------------------------------------------------------------------------------------    
Challenge 6 -

def is_leap(year):
    leap = False
    
    if year%400==0:
        leap=True
    elif year%100==0:
        leap=False
    elif year%4==0:
        leap=True        
    
    return leap

year = int(input())
print(is_leap(year))

------------------------------------------------------------------------------------------------------------------------------------------------------------------
Challenge 7 -

n = int(input())
for i in range(1,n+1):
    print(i,end="")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Challenge 8 -
 
 if __name__ == '__main__':
        n = int(input())
    arr = map(int, input().split())
    print(sorted(list(set(arr)))[-2])

------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
    
Challenge 9-    

N = int(input())

stud = []
for i in range(2*N):
    stud.append(input().split())
grades = {}
for j in range(0, len(stud), 2):
    grades[stud[j][0]] = float(stud[j + 1][0])
    
result = []
num_to_match = sorted(set(grades.values()))[1]
for pupil in grades.keys():
    if grades[pupil] == num_to_match:
        result.append(pupil)
for k in sorted(result):
    print(k)
    
------------------------------------------------------------------------------------------------------------------------    
 Challenge 10- 
 
 if __name__ == '__main__':
        n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    l=list(student_marks[query_name])
    le=len(l)
    s=sum(l)
    av=s/le
    print('%.2f'%av)
    
---------------------------------------------------------------------------------------------------------------------
Challenge 11 -

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score

n = int(input())
words = input().split()
print(score_words(words))     
 
------------------------------------------------------------------------------------------------------------
Challenge 12 - 

class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())



queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())

----------------------------------------------------------------------------------------------------------------
Challenge 13 -

import numpy

N, M = map(int, input().split())

A = numpy.array([list(map(int, input().split())) for n in range(N)])
B = numpy.array([list(map(int, input().split())) for n in range(N)])

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)

-------------------------------------------------------------------------------------------------------------------------
 Challenge 14 -
 
import numpy

numpy.set_printoptions(sign=' ')

array = numpy.array(input().split(),float)

print(numpy.floor(array))
print(numpy.ceil(array))
print(numpy.rint(array))
--------------------------------------------------------------------------------------------------------------------------
 Challenge 15 -
 
import numpy

N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)], int)
print(numpy.prod(numpy.sum(A, axis=0), axis=0))

-----------------------------------------------------------------------------------------------------------------------
 Challenge 16 -
 
import numpy

N, M = map(int, input().split())
storage = numpy.array([input().split() for _ in range(N)],int)
print(numpy.max(numpy.min(storage, axis=1), axis=0))

--------------------------------------------------------------------------------------------------------------------------
Challenge 17 -

import numpy
array = []
n, m = map(int, input().split())
for _ in range(n): array.append(list(map(int, input().split())))
array = numpy.array(array)
print(numpy.mean(array, axis=1))
print(numpy.var(array, axis=0))
print(round(numpy.std(array), 11))

-----------------------------------------------------------------------------------------------------
Challenge 18 -

import numpy

n = int(input())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)
print(numpy.dot(a, b))

----------------------------------------------------------------------------------------------------------------

Challenge 19- 
import numpy

A = numpy.array(input().split(), int)
B = numpy.array(input().split(), int)

print(numpy.inner(A, B))
print(numpy.outer(A, B))

--------------------------------------------------------------------------------------------------------------------
 Challenge 20- 
 
 import numpy

coefs=list(map(float,input().split()))
x=float(input())
print(numpy.polyval(coefs,x))

-------------------------------------------------------------------------------------------------------------------
 Challenge 21-  
 
 import numpy
array=[list(map(float,input().split())) for i in range(int(input()))]
print(round(numpy.linalg.det(array),2))

--------------------------------------------------------------------------------------------------------------------
 Challenge 22- 
  
from itertools import product
A = input().split()
A = list(map(int,A))
B = input().split()
B = list(map(int, B))
output = list(product(A,B))
for i in output:
    print(i, end = " ")

----------------------------------------------------------------------------------------------------------------------
Challenge 23- 

from itertools import permutations

s,k = input().split()

words = list(permutations(s,int(k)))
words = sorted(words, reverse=False)
for word in words:
    print(*word,sep='')
    
--------------------------------------------------------------------------------------------------------------------------    
 Challenge 24- 
 
from itertools import combinations

io = input().split()
S = io[0]
k = int(io[1])
for i in range(1,k+1):
    for j in combinations(sorted(S),i):
        print("".join(j))
        
-------------------------------------------------------------------------------------------------------------------------
Challenge 25- 
from itertools import combinations_with_replacement

io = input().split();
char = sorted(io[0]);
N = int(io[1]);

for i in combinations_with_replacement(char,N):
    print(''.join(i))
    
--------------------------------------------------------------------------------------------------------------------------
Challenge 26-

from itertools import *

io = input()
for i,j in groupby(map(int,list(io))):
    print(tuple([len(list(j)), i]) ,end = " ")
    
------------------------------------------------------------------------------------------------------------------
Challenge 27-   

N = int(input())
D = input().split()
K = int(input())


from itertools import combinations

contain = 0
total = 0

for c in combinations(D, K):
    if "a" in c:
        contain += 1
    total += 1
print(contain/total)

----------------------------------------------------------------------------------------------------------------------
CONGRATULATION !!!!! YOU HAVE WON 5 STARS 

        
 '''