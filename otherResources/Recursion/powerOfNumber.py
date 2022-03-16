def powerOfNum(base,power):
  assert power>=0 and int(power)==power, "Exponent must be positive integer only"
  if(power==0):
    return 1
  return base *powerOfNum(base,power-1)


print(powerOfNum(2,10))


