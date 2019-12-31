# mail-me
A python program which, given a fas id as input returns the user's e-mail

##### Hello,
##### In this short readme we're gonna cover up how i implemented this app,
##### First things first, i had to go to the python-fedora repo and check out the source code, after 20 minutes of struggling i finnally found the file i was searching for( lol if i had seen sooner that it was written in the readme i would not have lost this much time), The file's name was fas2.py. For more info on python-fedora follow [this](https://github.com/fedora-infra/python-fedora) link.
##### The first think that struck me was the readability of the code and how much well commented it was, then i installed the python-fedora pip package with:
```
$ pip install python-fedora

```
##### In my excitement to triy out the features of this package,i tried to `import python-fedora`, another big error, dude, i lost some other 10 minutes checking weither or not python-fedora was installed, man...i should really...really read the docs😔, when i found where was the error i was... well let's stop talking about the unnecessary things and go back to work.
###### for the info i should have imported `fedora.client.fas2` and i finnally saw it i the readme and corrected it:) 
#####
#### I found out 2 interesting ways in which, when given a username i can return the email corresponding to it.
<br>

### 1. `person_by_username()` function:

##### This way is certainly the easiest to implement, it takes only 2 or three lines of code and is very easy to understand,  <br>

##### It returns a person object and all you need is to extract the user's email
<br>

###  2. `people_by_key()` function:
##### Ok, i must admit that this one is mainly used to request many things at a time, but with proper use it almost works like the the person_by_username function(except for the dictionnary access key which is nonexistant in this function) 
<br><br><br><br>
##### That's it,, hope it was helpful :) Have a happy new year 🎉🎉🎊
