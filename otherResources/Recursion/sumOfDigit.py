
def sumOfDigits(num):

  assert num>=0 ,"Number has to be positive  integer only"
  if(num==0):
    return num

  return num%10 + sumOfDigits(num//10)

#Here 
# Recursive step: num%10 + sumOfDigits(num//10)
# Base Case num==0
# Constraints Number >=0