
# coding: utf-8

# # 標準偏差と分散

# In[12]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

incomes = np.random.normal(100.0, 50.0, 10000)

plt.hist(incomes, 50)
sns.distplot(incomes, bins=50)


# In[13]:


incomes.std()


# In[17]:


incomes.var()


# ## アクティビティ

# 上記の正規関数に対して、様々なパラメータを試してみよう。そして、パラメータが正規関数の形にどのような影響を与えるのか確かめる実験をしてみましょう。正規関数の形と、標準偏差や分散にはどのような関係があるのでしょうか？
