#!/usr/bin/env python
# coding: utf-8

import jubo

# In[9]:


with jubo.cell("cell_529194674"):
    with jubo.display_patched():
        
        from jubo import interact
        from jubo import widgets
        import datetime
        
        def date_in_days_time(num_days):
            dt = datetime.datetime.now() + datetime.timedelta(days=num_days)
            return dt.strftime("%a %d %b %y")
                               
        
        interact(date_in_days_time,
                 num_days=widgets.IntSlider(description="Date in x days", min=-10,max=30,step=1,value=10))

