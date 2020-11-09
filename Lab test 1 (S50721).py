#!/usr/bin/env python
# coding: utf-8

# In[11]:


num=11
print (bin(num))
print (bin(num).count("1"))


# In[43]:


test_string="An apple is not a tomato"
counter = test_string.count('a')
print(counter)


# In[60]:


test_string="I have python exam"
print("Original string: "+test_string)
res = len(test_string.split())
print("The number of word in the string is: "+str(res))


# In[56]:


def multiply_by_two(number):
    return number*2
#print(multiply_by_two(10))

print_arguments = multiply_by_two
augmented_multiply_by_two = print_arguments
number1 = augmented_multiply_by_two(10)
print(number1)

def add_numbers(num1,num2):
    return num1+num2
#print(add_numbers(3,4))
augmented_add_numbers = add_numbers
x = augmented_add_numbers(3,4)
print(x)


# In[62]:


def multiply_by_three(value):
    return value*3
#multiply_by_three(10)

multiply_output = multiply_by_three
augmented_multiply_by_three = multiply_output
x1 = augmented_multiply_by_three(100)
print(x1)


# In[ ]:




