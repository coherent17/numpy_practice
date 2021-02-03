import numpy as np

#1. numpy calculation
print("1.")
a=np.arange(1,10).reshape(3,3)
b=np.arange(10,19).reshape(3,3)
print(a)
print(b)
#所有元素都加1
print(a+1)

#所有元素都平方
print(a**2)

#判斷式輸出boolen
print(a<5)

#相對應的元素相加
print(a*b)

#矩陣內積
print(np.dot(a,b))

#2. function i numpy and statistic
c=np.arange(1,10).reshape(3,3)
print(c)
#[[1 2 3]
# [4 5 6]
# [7 8 9]]
print(np.min(a),np.max(a))      #1 9

