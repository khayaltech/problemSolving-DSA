def decimalToBinary(num):
  if num==0:
     return 1
  return num%2 + 10*decimalToBinary(num//2)


