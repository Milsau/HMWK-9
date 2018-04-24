
# coding: utf-8

# In[11]:


from flask import Flask
from flask import render_template
from random import randint

with open('inspiration.txt') as fp:
    quotes = fp.readlines()

app = Flask(__name__)


@app.route('/')
def hello(): 
    random_no = randint(0,len(quotes)-1)
    quote = quotes[random_no]
    return render_template('test.html', quote=quote)

