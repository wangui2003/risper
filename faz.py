#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st 
st.header('''simple web app''')
st.writer(''' my app''')
f=st.slider("val")
st.write("celcius is",f*9/5*32 )


# In[ ]:




