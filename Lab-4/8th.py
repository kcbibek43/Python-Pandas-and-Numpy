def isPrime(n):
  if(n==1 or n==0):
    return False
  for i in range(2,n//2+1):
    if(n%i==0):
      return False
  return True
  
N = int (input("Enter the value of N "))
l = []
for i in range(1,N+1):
  if(isPrime(i)):
    l.append(i)
print (l)