from math import sqrt
N=int(input())
t1=()
t2=()
for i in range(2,N+1):
       if N % i == 0:
              t1=t1+(i,)
              sr = sqrt(i)
              if sr-int(sr)==0:
                     t2=t2+(i,)
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return n

t3=list(filter(isPrime,t1))
print(t1)
print(t2)

if all(i <= 19 for i in t3):
       final=lambda t1,t2: len([i for i in t1 if all(i%j!=0 for j in t2)])
       print(final(t1,t2))
