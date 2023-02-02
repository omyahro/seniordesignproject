#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pwnedpasswords


# In[2]:


import pwnedpasswords


# In[3]:


def pwnedpasswordFunction():
    print("Welcome to the Perfect Password! We're here to ensure you have the perfect passphrase for your sensitive information. Type in your perfect passphrase and we'll let you know if its already been leaked!")
    passphrase = input("Enter your desired passphrase:")
    print ("Your desired passphrase is", passphrase)
    entries = pwnedpasswords.check(passphrase)
    
    print ("This passphrase has", entries, "entries within the Pwned Passwords database! Would you like to try again?")
    tryAgain = input("Would you like to try again?(Yes/No)")
    if tryAgain == "Yes":
        pwnedpasswordFunction()
    else:
        ("Thanks for using Perfect Password, come again!")
    
pwnedpasswordFunction()


# In[ ]:





# In[ ]:




