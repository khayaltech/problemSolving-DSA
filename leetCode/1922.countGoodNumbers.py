# def isPrimeNumber(num):
#   flag=False
#   if(num>1):
#     for i in range(2,num):
#       if(num%i==0):
#         flag=True
#         break
#   if flag:
#     return False
#   else:
#     return True


# def isEven(num):
#   if(num%2==0):
#     return True
#   return False


# def countsGoodNumber(n):
#   if(n==1):
#     return 5
#   else:
  
  
  


def count(n):
  i=n
  if (n==1):
    return 5
  i-=1
  return count(n-2)+ count(n-1)

#5 20 100 400

print(count(4))



belowTen=["zero","one","two","three","four","five","six","seven","nine"]
belowTwenty=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
belowHundred=["twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]



def checkNum(a):
  if(len(str(a))==2):
    return 10
  elif(len(str(a))==3):
    return 100
  elif(len(str(a))==4):
    return 1000
  elif(len(str(a))==7):
    return 1_000_000
  elif(len(str(a))==4):
    return 1_000_000_000


def integerToEnglish(num):
  if len(len(str(num))==1):
    return belowTen[num]
  elif(len(str(num))==2 and(num in list(range(10,20,1))):
    return belowTwenty[num]