#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Initialize Otter
import otter
grader = otter.Notebook("Otter-sample-assignment.ipynb")


# # Instructions
# 
# First, make sure to run the first cell in the notebook. This will initialize the autograder. Then, go through each question and provide a solution for it. Finally, go through the final section that tells you what you need to submit.

# # Sample Question (read these instructions)
# 
# The solution for this question is a function called `hello_inst447()` that takes no parameter and returns the string `Hello INST447!`. 
# 
# To solve this problem, replace in the cell below the line with `...` with the following code:
# 
# ```python
# def hello_inst447():
#     return "Hello INST447!"
# ```

# In[8]:


def hello_inst447():
    return "Hello INST447!"


# You can run this cell to make sure that the solution works as intended.

# In[9]:


hello_inst447()


# Now, run the cell below to test that your solution is correct.

# In[10]:


grader.check("sample")


# # What you need to submit
# 
# First, run the cell below. Then run the final cell in the notebook. This cell will generate the ZIP file you need to submit. It will run all the tests in the notebook (in this case just the one above), and then display a link on the last line of text. Click on that link, and save the ZIP file on your computer. Finally, go back to ELMS to complete the submission of the ZIP file.

# In[11]:


get_ipython().system('jupyter nbconvert --to script Otter-sample-assignment.ipynb')


# ## Submission
# 
# Make sure you have run all cells in your notebook in order before running the cell below, so that all images/graphs appear in the output. The cell below will generate a zip file for you to submit.

# In[ ]:


grader.export(pdf=False, force_save=True, run_tests=True, files=['Otter-sample-assignment.py'])


#  
