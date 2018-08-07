
# coding: utf-8

# In[1]:


from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import datetime

def date_in_days_time(num_days):
    dt = datetime.datetime.now() + datetime.timedelta(days=num_days)
    return dt.strftime("%a %d %b %y")
                       

interact(date_in_days_time, 
         num_days=widgets.IntSlider(min=-10,max=30,step=1,value=10))


# In[2]:


interact(date_in_days_time, 
         num_days=widgets.IntSlider(min=-10,max=30,step=1,value=10))

