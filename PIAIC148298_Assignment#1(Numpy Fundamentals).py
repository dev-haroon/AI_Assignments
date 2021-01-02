
# coding: utf-8

# # **Assignment For Numpy**

# Difficulty Level **Beginner**

# 1. Import the numpy package under the name np

# In[1]:


import numpy as np


# 2. Create a null vector of size 10 

# In[2]:


np.zeros(10)


# 3. Create a vector with values ranging from 10 to 49

# In[3]:


arr1 = np.arange(10,50)
arr1


# 4. Find the shape of previous array in question 3

# In[4]:


np.shape(arr1)


# 5. Print the type of the previous array in question 3

# In[5]:


type(arr1)


# 6. Print the numpy version and the configuration
# 

# In[6]:


print(np.__version__)
print(np.show_config())


# 7. Print the dimension of the array in question 3
# 

# In[7]:


arr1.ndim


# 8. Create a boolean array with all the True values

# In[8]:


np.ones((2, 2), dtype=bool)


# 9. Create a two dimensional array
# 
# 
# 

# In[9]:


arr2 = np.arange(10).reshape(2,5)
arr2


# 10. Create a three dimensional array
# 
# 

# In[10]:


arr2 = np.arange(27).reshape(3,3,3)
arr2


# Difficulty Level **Easy**

# 11. Reverse a vector (first element becomes last)

# In[11]:


x = np.arange(10, 18)
x = x[::-1]
x


# 12. Create a null vector of size 10 but the fifth value which is 1 

# In[12]:


y = np.arange(10)
y[4]=1
y


# 13. Create a 3x3 identity matrix

# In[13]:


arr3 = np.identity(3)
arr3


# 14. arr = np.array([1, 2, 3, 4, 5]) 
# 
# ---
# 
#  Convert the data type of the given array from int to float 

# In[14]:


arr4 =np.array([1, 2, 3, 4, 5])
arr4.astype('float64')


# 15. arr1 =          np.array([[1., 2., 3.],
# 
#                     [4., 5., 6.]])  
#                       
#     arr2 = np.array([[0., 4., 1.],
#      
#                    [7., 2., 12.]])
# 
# ---
# 
# 
# Multiply arr1 with arr2
# 

# In[15]:


arr1 = np.array([[1., 2., 3.],
            [4., 5., 6.]])
arr2 = np.array([[0., 4., 1.],
           [7., 2., 12.]])
ans = arr1*arr2
ans


# 16. arr1 = np.array([[1., 2., 3.],
#                     [4., 5., 6.]]) 
#                     
#     arr2 = np.array([[0., 4., 1.], 
#                     [7., 2., 12.]])
# 
# 
# ---
# 
# Make an array by comparing both the arrays provided above

# In[16]:


arr1 = np.array([[1., 2., 3.],
            [4., 5., 6.]]) 
arr2 = np.array([[0., 4., 1.], 
            [7., 2., 12.]])
comparison= arr1 == arr2
equal_array= comparison.all()
equal_array


# 17. Extract all odd numbers from arr with values(0-9)

# In[17]:


a = np.arange(0, 10)# write your code here
condition = np.mod(a, 2)==0
z = np.extract(condition, a)
z


# 18. Replace all odd numbers to -1 from previous array

# In[18]:


arr = np.arange(0, 10)
arr[arr%2 == 1] = -1
arr


# 19. arr = np.arange(10)
# 
# 
# ---
# 
# Replace the values of indexes 5,6,7 and 8 to **12**

# In[19]:


arr = np.arange(10)
arr
arr[5] =arr[6]=arr[7]=arr[8]=12 
arr


# 20. Create a 2d array with 1 on the border and 0 inside

# In[20]:


arr1 = np.ones((5,5))
arr1[1:-1,1:-1]=0
arr1


# Difficulty Level **Medium**

# 21. arr2d = np.array([[1, 2, 3],
# 
#                     [4, 5, 6], 
# 
#                     [7, 8, 9]])
# 
# ---
# 
# Replace the value 5 to 12

# In[21]:


arr2d = np.array([[1, 2, 3],
            [4, 5, 6], 

            [7, 8, 9]])
arr2d[1][1] = 12
arr2d


# 22. arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# 
# ---
# Convert all the values of 1st array to 64
# 

# In[22]:


#ans(:,:,1)
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr3d[:,:,0] = 64
arr3d


# 23. Make a 2-Dimensional array with values 0-9 and slice out the first 1st 1-D array from it

# In[23]:


arr = np.arange(0,10).reshape(2,5)
#arr[0]
arr


# 24. Make a 2-Dimensional array with values 0-9 and slice out the 2nd value from 2nd 1-D array from it

# In[24]:


arr = np.arange(0,10).reshape(2,5)
arr[1]


# 25. Make a 2-Dimensional array with values 0-9 and slice out the third column but only the first two rows

# In[25]:


arr = np.arange(0,10).reshape(2,5)

arr[0:2,2:3] 


# 26. Create a 10x10 array with random values and find the minimum and maximum values

# In[26]:


arr3= np.random.random((5,5))
arr3
xmin,xmax = arr3.min(),arr3.max()
xmin,xmax


# 27. a = np.array([1,2,3,2,3,4,3,4,5,6]) b = np.array([7,2,10,2,7,4,9,4,9,8])
# ---
# Find the common items between a and b
# 

# In[27]:


a = np.array([1,2,3,2,3,4,3,4,5,6]) 
b = np.array([7,2,10,2,7,4,9,4,9,8])
common= np.intersect1d(a,b)
common


# 28. a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,10,2,7,4,9,4,9,8])
# 
# ---
# Find the positions where elements of a and b match
# 
# 

# In[28]:


a = np.array([1,2,3,2,3,4,3,4,5,6]) 
b = np.array([7,2,10,2,7,4,9,4,9,8])

poistions= np.where(np.in1d(a, b))[0]
poistions


# 29.  names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])  data = np.random.randn(7, 4)
# 
# ---
# Find all the values from array **data** where the values from array **names** are not equal to **Will**
# 

# In[29]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) 
data = np.random.randn(7, 4)
names, data


# 30. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) data = np.random.randn(7, 4)
# 
# ---
# Find all the values from array **data** where the values from array **names** are not equal to **Will** and **Joe**
# 
# 

# Difficulty Level **Hard**

# 31. Create a 2D array of shape 5x3 to contain decimal numbers between 1 and 15.

# In[30]:


x = np.random.randn(1,15).reshape((5,3))
x


# 32. Create an array of shape (2, 2, 4) with decimal numbers between 1 to 16.

# In[31]:


y = np.random.randn(1,16).reshape((2,2,4))
y


# 33. Swap axes of the array you created in Question 32

# In[32]:


y = np.random.randn(1,16).reshape((2,2,4))
z = np.transpose(y)
z


# 34. Create an array of size 10, and find the square root of every element in the array, if the values less than 0.5, replace them with 0

# In[33]:


x = np.arange(10)
y= np.sqrt(x)
z= np.where((y<0.5), 0, y) 
z


# 35. Create two random arrays of range 12 and make an array with the maximum values between each element of the two arrays

# In[37]:


a = np.array([1, 5, 9])
b = np.array([3, 2, 11])
y = np.maximum(a, b)
y


# 36. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
# 
# ---
# Find the unique names and sort them out!
# 

# In[38]:


z = np.unique(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
z


# 37. a = np.array([1,2,3,4,5])
# b = np.array([5,6,7,8,9])
# 
# ---
# From array a remove all items present in array b
# 
# 

# In[41]:


a = np.array([1,2,3,4,5]) 
b = np.array([5,6,7,8,9])
x = np.setdiff1d(a, b)
x


# 38.  Following is the input NumPy array delete column two and insert following new column in its place.
# 
# ---
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
# 
# 
# ---
# 
# newColumn = numpy.array([[10,10,10]])
# 

# In[48]:


sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]]) 
#sampleArray
sampleArray= np.delete(sampleArray, [1], axis=1)
newColumn = np.array([[10,10,10]])
sampleArray = np.insert(sampleArray , 1, newColumn, axis = 1)
sampleArray


# 39. x = np.array([[1., 2., 3.], [4., 5., 6.]]) y = np.array([[6., 23.], [-1, 7], [8, 9]])
# 
# 
# ---
# Find the dot product of the above two matrix
# 

# In[49]:


x = np.array([[1., 2., 3.], [4., 5., 6.]]) 
y = np.array([[6., 23.], [-1, 7], [8, 9]])
z = np.dot(x,y)
z


# 40. Generate a matrix of 20 random values and find its cumulative sum

# In[56]:


z = np.random.randn(40)
y = np.cumsum(z, axis = 0)
y

