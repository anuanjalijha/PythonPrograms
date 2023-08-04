def insertionSort(a):
   length=len(a)
   for i in range(1,length):
      j = i-1
      temp = a[i]
      # shifting elements till this condition holds
      while j>=0 and a[j]>temp:
         a[j+1] = a[j]
         j = j-1 
      # j+1 is correct position for ith element
      a[j+1] = temp
   return a