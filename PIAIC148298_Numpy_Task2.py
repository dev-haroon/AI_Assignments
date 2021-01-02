
# coding: utf-8

# # CrunchieMunchies
# 
# You work in marketing for a food company <b>myCorps</b>, which is developing a new kind of tasty, wholesome cereal called <b>CrunchieMunchies</b>. 
# 
# You want to demonstrate to consumers how healthy your cereal is in comparison to other leading brands, so you’ve dug up nutritional data on several different competitors.
# 
# Your task is to use <em>NumPy statistical calculations</em> to analyze this data and prove that your <b>CrunchieMunchies</b> is the healthiest choice for consumers.
# 
# 
# 
# 
# 

# # Task STEPS
# 

# 1.First, import numpy.

# In[1]:


# your code goes here

import numpy as np


# 2.Look over the <b><em>cereal.csv</em></b> file. This file contains the reported calorie amounts for different cereal brands. Load the data from the file and save it as <b><em>calorie_stats.</em></b>
# 
# 

# In[3]:


# your code goes here
calorie_stats = np.genfromtxt('cereal.csv',delimiter=',')
calorie_stats


# 3.There are <em>60 calories per serving of CrunchieMunchies</em>. How much <b>higher</b> is the <b>average calorie count</b> of your competition?
# 
# Save the answer to the variable <b>average_calories</b> and print the variable to the terminal to see the answer.
# 

# In[4]:


# your code goes here
average_calorie = np.mean(calorie_stats)
average_calorie


# 4.Does the <b>average calorie count</b> adequately reflect the distribution of the dataset? Let’s sort the data and see.
# 
# <b><em>Sort</em></b> the data and save the result to the variable <b>calorie_stats_sorted</b>. Print the sorted data to the terminal.
# 

# In[5]:


# your code goes here
calorie_stats_sorted = np.sort(calorie_stats)
calorie_stats_sorted


# 5.Do you see what I’m seeing? Looks like <b><em>the majority of the cereals are higher than the mean</em></b>. Let’s see if the <b>median</b> is a better representative of the dataset.
# 
# Calculate the median of the dataset and save your answer to <b><em >median_calories</em></b>. Print the median so you can see how it compares to the mean.

# In[6]:


# your code goes here

median_calorie=np.median(calorie_stats)
median_calorie


# 6.While the median demonstrates that <b><em><q>at least half of our values are over 100 calories</q></em></b>, it would be more impressive to show that a significant portion of the competition has a higher calorie count that CrunchieMunchies.
# 
# <b>Calculate different percentiles</b> and print them to the terminal until you find the lowest percentile that is greater than 60 calories. Save this value to the variable <b>nth_percentile</b>.
# 

# In[9]:


# your code goes here

first_quarter=np.percentile(calorie_stats,25)
half_percentile=np.percentile(calorie_stats,50)
third_quarter=np.percentile(calorie_stats,75)

first_quarter, half_percentile, third_quarter


# 7.While the percentile shows us that<b><em><q>the majority of the competition has a much higher calorie count</q></em></b>, it’s an awkward concept to use in marketing materials.
# 
# Instead, let’s calculate the percentage of cereals that <b><em><q>have more than 60 calories per serving</q></em></b>. Save your answer to the variable <b><em>more_calories</em></b> and print it to the terminal

# In[10]:


# your code goes here

more_calorie = np.mean(calorie_stats>60)
more_calorie


# 8.Wow! That’s a really high percentage. That’s going to be very useful when we promote CrunchieMunchies. But one question is, <b><em>how much variation exists in the dataset? </b></em></q>Can we make the generalization that most cereals have around 100 calories or is the spread even greater?
# 
# Calculate the amount of variation by finding the <b><em>standard deviation</em</b> Save your answer to <b><em>calorie_std</em></b> and print to the terminal. How can we incorporate this value into our analysis?

# In[11]:


# your code goes here

calorie_std=np.std(calorie_stats)
calorie_std


# 9.Write a short paragraph that sums up your findings and how you think this data could be used to 
# <b>myCorp’s</b> advantage when marketing CrunchieMunchies.
# 

# In[ ]:


#The competitions cereals are clearly higher in caloric stats compared to the healhty option being proposed. CrunchieMunchies is lower in calories than the competition, which should be highlighted in advertisement. We can use the percentage of cereals higher than CrunchieMunchies to highlight the comparison. This would require looking at the calorie_stat greater than 70

