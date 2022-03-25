
def kidsWithCandies(candies,extraCandies):
    newA=[]
    flag=True

    for x in range(0, len(candies)):
      z=candies[x]+extraCandies
      for y in candies:
         if z<y:
            flag=False
      print(flag)      
      newA.append(flag)
      flag=True
    return newA
                
            
print(kidsWithCandies([2,3,5,1,3],3))