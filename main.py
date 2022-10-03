import numpy as np

# arr1 = np.array([1, 2, 3, 4])
# arr2 = np.array([4, 5, 6, 7])
#
# z = np.add(arr1,arr2)
#
# sub = np.subtract(arr2,arr1)
#
# print(z)    #[ 5  7  9 11]
#
# print(sub)   #[3 3 3 3]
#
#
# mul = np.multiply(arr1,arr2)
# print(mul)
#
#
# div = np.divide(arr1, arr2)
# print(div)
#
#
# power = np.power(arr2, arr1)
# print(power)
#
#
#
# #return remainder
# remainder = np.mod(arr2, arr1)
# remainder2 = np.remainder(arr2, arr1)
# print(remainder)  #[0 1 0 3]
# print(remainder2)  #[0 1 0 3]
#
#
#
# newarr = np.divmod(arr2, arr1)
# print(newarr)
#
#
#
# arr = np.array([-1, -2, 1, 2, 3, -4])
# newarr = np.absolute(arr)
# print(newarr)










#------------------rounding decimal----------------------


# arr = np.array([-3.1666, 3.6667])
#
# round = np.around(arr,2)
#
# print(round)   #[-3.17  3.67]
#
#
#
# arr = np.floor([-3.1666, 3.6667])
#
# print(arr)   #[-4.  3.]
#
#
#
#
#
#
# arr = np.ceil([-3.1666, 3.6667])
#
# print(arr)   #[-3.  4.]



#-------------------------log-------------------------

# arr = np.array([ 5 , 7 , 9 ,11])
#
# print(np.log10(arr))
# print(np.log2(arr))
# print(np.log(arr))


#-------------------------sum-------------------

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([1, 2, 3])
#
# newarr = np.sum([arr1, arr2])
#
# print(newarr)   #12
#
#
#
#
#
#
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([1, 2, 3])
#
# newarr = np.sum([arr1, arr2], axis=1)
#
# print(newarr)    #[6 6]
#
#
#
# arr = np.array([1, 2, 3])
#
# newarr = np.cumsum(arr)
#
# print(newarr)     #[1 3 6]











#----------- lcm------------------
# num1 = 4
# num2 = 6
#
# x = np.lcm(num1, num2)
#
# print(x) #12
#
#
#
#
#
# arr = np.array([3, 6, 9])
#
# x = np.lcm.reduce(arr)
#
# print(x)   #24




#----------- gcd------------------



# num1 = 6
# num2 = 9
#
# x = np.gcd(num1, num2)
#
# print(x)    #3
#
#
#
#
#
#
# arr = np.array([20, 8, 32, 36, 16])
#
# x = np.gcd.reduce(arr)
#
# print(x)   #4




#------------------------trigonometric-------------------


#
# print(np.pi)   #3.141592653589793
#
#
#
# x = np.sin(np.pi/2)  #1
#
# print(x)
#
#
#
#
#
# arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
#
# x = np.sin(arr)
#
# print(x)
#
#
#
#
#
# arr = np.array([90, 180, 270, 360])
#
# x = np.deg2rad(arr)
#
# print(x)





#------------------hyperbolic---------------------


# x = np.sinh(np.pi/2)
#                          #sinh(x) =  (e^x − e^−x)/2     cosh(x) =  (e^x + e^−x)/2
# print(x)
#
#
#
#
# arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
#
# x = np.cosh(arr)
#
# print(x)




# x = np.arcsin(1)  #1.5707963267948966  in radian  = 90 degree
#
# print(np.rad2deg(x)) #1.5707963267948966  in radian  = 90 degree
#
#
# x = np.arcsinh(1)
#
# print(x)





#--------------------Set Operations--------------------


# arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
#
# x = np.unique(arr)     #[1 2 3 4 5 6 7]
#
# print(x)
#
#
#
#
#
# arr1 = np.array([1, 2, 3, 4])
# arr2 = np.array([3, 4, 5, 6])
#
# newarr = np.intersect1d(arr1, arr2, assume_unique=True)
#
# print(newarr)     #[3 4]
#
#
#
#
#
# set1 = np.array([1, 2, 3, 4])
# set2 = np.array([3, 4, 5, 6])
#
# newarr = np.setdiff1d(set1, set2, assume_unique=True)                   #To find only the values in the first set that is NOT present in the seconds set, use the setdiff1d() method.
#
# print(newarr) #[1 2]
#
#
#
#
#
#
#
#
#
# set1 = np.array([1, 2, 3, 4])
# set2 = np.array([3, 4, 5, 6])
#
# newarr = np.setxor1d(set1, set2, assume_unique=True)    #To find only the values that are NOT present in BOTH sets, use the setxor1d() method.
#
# print(newarr)    #[1 2 5 6]





