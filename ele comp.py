import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
c=0
for x in arr:
  if x=="0":
      c=c+1
  else:
      pass
if c==0:
    print("no element in array is zero")
else:
    print(c,"elements are zeros")
