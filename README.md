"# Thompsons_Construction" 

Name: Michael Coleman
GMIT Number: G00347650
Email: G00347650@gmit.ie

Problem statement: 
To write a program in python which builds non-deterministic finite automatons (NFA) from a regular expression, and can use the NFA to determine if the regular expression matches any given string of text.

Projects parts: 
1. Parse the regular expression from infix to postfix notation.
2. Build a series of small NFA’s for parts of the regular expression.
3. Use the smaller NFA’s to create the overall NFA.
4. Implement the matching algorithm using the NFA. 


Research for each project part: 
1. First I had to try and figure out how to convert an expression from it’s infix form to its postfix form, to do this I looked at the videos provided on moodle as well as looking at some websites online, particularly this one - http://condor.depaul.edu/ichu/csc415/notes/notes9/Infix.htm  
Once, I had a grasp on how to do infix to postfix notation I made a few attempts on paper to see if I had enough understanding of it to carry it out, which I did with success. I then started researching coding in Python to learn how to code better in Python as I had never coded in Python before this project and my only experiences were the video’s I had watched on the moodle page. I looked into the Python docs - https://docs.python.org/3/tutorial/  - to refresh myself on the videos I had watched previously as well as see if I could learn something extra that may be of use.

2. As seen on the videos, this part of the project was implemented using classes and as a result, I looked up the python docs again and navigated to the classes section - https://docs.python.org/3/tutorial/classes.html -  where I read about them to try and further my knowledge on them and understand how they work. They seemed fairly complex from the tutorial on Python, but I soon realised I was just over complicating them and that I simply need to look at them as a grouping of variables for this project.

3. Following the video Tutorial on how the implement Thompson’s Algorithm in Python, I looked into other operators which I could use for this project- https://www.tldp.org/LDP/Bash-Beginners-Guide/html/sect_04_01.html - + http://web.mit.edu/gnu/doc/html/regex_3.html#SEC12 -  From these sites I seen that there are many more operators available to implement and I looked into how I would go about implementing these in comparison to the ones explained in the video tutorials. I did this by trying to work out how these would work on paper first before attempting them in code as I was unsure as to how to go about implementing them in code and writing out on paper had previously helped me a lot in understanding the other operators and  how I am much better at implementing code after I understand the concept rather than diving in and coding right away.

4. During the video tutorial, I noticed that sets were being used so I paused the video and looked up the docs to see how sets work - https://docs.python.org/3/tutorial/datastructures.html#sets - From this I got a good feel as to how they work and what can be done with the sets.

5. (Extra Research): I looked at some Python docs to see what else could be added to the project in order to add more functionality to my submission and found the input() function - https://www.w3schools.com/python/ref_func_input.asp - which takes input from the user in the console and can be stored in a variable. I also looked into the while loops in Python and how booleans work in Python using the docs in order to loop the application using a boolean control. From these I added an interface which gives users options to choose from.


