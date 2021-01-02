
# coding: utf-8

# # Numpy_Assignment_2::

# ## Question:1

# ### Convert a 1D array to a 2D array with 2 rows?

# #### Desired output::

# array([[0, 1, 2, 3, 4],
#         [5, 6, 7, 8, 9]])

# In[1]:


import numpy as np

x = np.arange(10).reshape(2,5)
x


# ## Question:2

# ###  How to stack two arrays vertically?

# #### Desired Output::
array([[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
       [1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1]])
# In[2]:


in_arr1 = np.arange(10, dtype=np.int64).reshape(2,5)  
in_arr2 = np.ones(10, dtype=np.int64).reshape(2,5) 

out_arr = np.vstack((in_arr1, in_arr2)) 
out_arr


# ## Question:3

# ### How to stack two arrays horizontally?

# #### Desired Output::
array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
       [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
# In[3]:


in_arr1 = np.array([[ 0, 1, 2, 3, 4], [1, 1, 1, 1, 1]])   
in_arr2 = np.array([[ 5, 6, 7, 8, 9], [ 1, 1, 1, 1, 1]] ) 

out_arr = np.hstack((in_arr1, in_arr2)) 
out_arr


# ## Question:4

# ### How to convert an array of arrays into a flat 1d array?

# #### Desired Output::
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# In[4]:


in_arr1 = np.array([[ 0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]) 
result = in_arr1.flatten()
result 


# ## Question:5

# ### How to Convert higher dimension into one dimension?

# #### Desired Output::
array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
# In[5]:


arr = np.arange(15)
newarr = arr.reshape(-1)
newarr


# ## Question:6

# ### Convert one dimension to higher dimension?

# #### Desired Output::
array([[ 0, 1, 2],
[ 3, 4, 5],
[ 6, 7, 8],
[ 9, 10, 11],
[12, 13, 14]])
# In[6]:


arr = np.arange(15)
newarr = arr.reshape(5,3)
newarr


# ## Question:7

# ### Create 5x5 an array and find the square of an array?

# In[7]:


x= np.arange(1,26).reshape((5,5))
y= np.square(x)
y


# ## Question:8

# ### Create 5x6 an array and find the mean?

# In[8]:


x= np.arange(1,31).reshape((5,6))
y = np.mean(x)
y


# ## Question:9

# ### Find the standard deviation of the previous array in Q8?

# In[9]:


x= np.arange(1,31, dtype=np.float64).reshape((5,6))
y = np.std(x)
y


# ## Question:10

# ### Find the median of the previous array in Q8?

# In[10]:


x= np.arange(1,31, dtype=np.float64).reshape((5,6))
y = np.median(x)
y


# ## Question:11

# ### Find the transpose of the previous array in Q8?

# In[11]:


x= np.arange(1,31).reshape((5,6))
y = np.transpose(x)
y


# ## Question:12

# ### Create a 4x4 an array and find the sum of diagonal elements?

# In[12]:


x= np.arange(1,17).reshape((4,4))
y = np.trace(x)
y


# ## Question:13

# ### Find the determinant of the previous array in Q12?

# In[13]:


x= np.arange(1,17).reshape((4,4))
y = np.linalg.det(x) 
y


# ## Question:14

# ### Find the 5th and 95th percentile of an array?

# In[14]:


x= np.arange(1,17)

fifth = np.percentile(x,5)
nintyFifth = np.percentile(x,95)
fifth, nintyFifth


# ## Question:15

# ### How to find if a given array has any null values?

# In[16]:


b = [[1,2,3],[np.nan,np.nan,2]] 
b_sum = np.sum(b)

array_with_nan = np.isnan(b_sum)
array_with_nan

