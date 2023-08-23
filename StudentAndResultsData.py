#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


result = "E:/jagruthi_DA/TestCases/result.txt"
df1 = pd.read_csv(result, sep="\t", header =None, names =["Rollno","Result"])
print(df1)


# In[5]:


Student = "E:/jagruthi_DA/TestCases/Student.txt"

df2 = pd.read_csv(Student, sep=r"\t",header=None, names = ["Student_name","Rollno"],engine= 'python')

print(df2)


# In[6]:


merged_df = pd.merge(df1, df2, on="Rollno")
print(merged_df)


# In[7]:


#problem1: students names who passed the results
passed_students = merged_df[merged_df["Result"] == 'pass']['Student_name']
print("Students who have successfully cleared the exam:", list(passed_students))


# In[8]:


#Problem 2: Count Number of Students (Pass/Fail)
pass_count = merged_df[merged_df['Result'] == 'pass'].shape[0]
fail_count = merged_df[merged_df['Result'] == 'fail'].shape[0]
print("Number of students who passed:", pass_count)
print("Number of students who failed:", fail_count)


# In[9]:


# Problem 3: Arrange Student Names Alphabetically
sorted_names = df2.sort_values(by='Student_name')['Student_name']
print("Student names arranged alphabetically:", list(sorted_names))

