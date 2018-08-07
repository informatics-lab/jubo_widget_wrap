#!/usr/bin/env python
# coding: utf-8

import jubo

# In[1]:


with jubo.cell("cell_697165274"):
    with jubo.display_patched():
        from jubo import interact
        from jubo import widgets
        from IPython.display import Image, display
        
        def show_img(index):
            imgs = {
                "yeah": "https://is4-ssl.mzstatic.com/image/thumb/Music127/v4/5e/48/a9/5e48a90c-7607-0ae0-5050-5d45f3c4613a/701649130744.png/268x0w.jpg",
                "great": "https://img00.deviantart.net/5107/i/2011/362/9/e/aww_yeah_by_sarah_tang-d4kj13w.png",
                "super": "https://imgc.allpostersimages.com/img/print/posters/booyah-comic-pop_a-G-10391412-0.jpg"
            }
            display(Image(url=imgs[index]))
        
        interact(show_img, index=widgets.Dropdown(value="yeah", options=["yeah", "great", "super"]))

