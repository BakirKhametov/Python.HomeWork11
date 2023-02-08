#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30

# Определить корни

# Найти интервалы, на которых функция возрастает

# Найти интервалы, на которых функция убывает

# Построить график

# Вычислить вершину

# Определить промежутки, на котором f > 0

# Определить промежутки, на котором f < 0


# In[4]:


from sympy import *
from sympy.plotting import plot


# In[5]:


x = Symbol('x')


# In[6]:


fx = -5*x**2 + 10*x - 150
fx


# In[7]:


plot(fx)


# In[8]:


x1, x2 = solve(fx)
round(x1.evalf(),3), round(x2.evalf(),3)


# In[9]:


solve(fx > 0)


# In[10]:


solve(fx < 0)


# In[11]:


diff(fx)


# In[14]:


solve(diff(fx) < 0)


# In[15]:


solve(diff(fx) > 0)


# In[ ]:




