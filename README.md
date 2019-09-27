# Graph_Theory_Project

## Problem statement: 
To write a program in python which builds non-deterministic finite automatons (NFA) from a regular expression, and can use the NFA to determine if the regular expression matches any given string of text.

## Projects parts: 
1. Parse the regular expression from infix to postfix notation.
2. Build a series of small NFA’s for parts of the regular expression.
3. Use the smaller NFA’s to create the overall NFA.
4. Implement the matching algorithm using the NFA. 


## Research for each project part: 
1. First I had to try and figure out how to convert an expression from it’s infix form to its postfix form, to do this I looked at the videos provided on moodle as well as looking at some websites online, particularly this one - http://condor.depaul.edu/ichu/csc415/notes/notes9/Infix.htm  
Once, I had a grasp on how to do infix to postfix notation I made a few attempts on paper to see if I had enough understanding of it to carry it out, which I did with success. I then started researching coding in Python to learn how to code better in Python as I had never coded in Python before this project and my only experiences were the video’s I had watched on the moodle page. I looked into the Python docs - https://docs.python.org/3/tutorial/  - to refresh myself on the videos I had watched previously as well as see if I could learn something extra that may be of use.

2. As seen on the videos, this part of the project was implemented using classes and as a result, I looked up the python docs again and navigated to the classes section - https://docs.python.org/3/tutorial/classes.html -  where I read about them to try and further my knowledge on them and understand how they work. They seemed fairly complex from the tutorial on Python, but I soon realised I was just over complicating them and that I simply need to look at them as a grouping of variables for this project.

3. Following the video Tutorial on how the implement Thompson’s Algorithm in Python, I looked into other operators which I could use for this project- https://www.tldp.org/LDP/Bash-Beginners-Guide/html/sect_04_01.html - + http://web.mit.edu/gnu/doc/html/regex_3.html#SEC12 -  From these sites I seen that there are many more operators available to implement and I looked into how I would go about implementing these in comparison to the ones explained in the video tutorials. I did this by trying to work out how these would work on paper first before attempting them in code as I was unsure as to how to go about implementing them in code and writing out on paper had previously helped me a lot in understanding the other operators and  how I am much better at implementing code after I understand the concept rather than diving in and coding right away.

4. During the video tutorial, I noticed that sets were being used so I paused the video and looked up the docs to see how sets work - https://docs.python.org/3/tutorial/datastructures.html#sets - From this I got a good feel as to how they work and what can be done with the sets.

5. (Extra Research): I looked at some Python docs to see what else could be added to the project in order to add more functionality to my submission and found the input() function - https://www.w3schools.com/python/ref_func_input.asp - which takes input from the user in the console and can be stored in a variable. I also looked into the while loops in Python and how booleans work in Python using the docs in order to loop the application using a boolean control. From these I added an interface which gives users options to choose from.


## Explanation for each Project part in code: 
1. Regular expressions are taken in an infix expression e.g. "a.(b|d).c*" as a parameter for the matching function and are converted using a shunt function which takes each character in the string and converts them to postfix, this is done by determining if the character read in is a bracket, special character e.g. ‘*’ or just a regular character e.g. ‘a’. If it is a special character, the according algorithm is used in correlation with the current and previous characters and the characters are added to the postfix based on their order of precedence.

2. The NFA’s are created using 2 classes, state and nfa. The nfa class uses the state class to create an NFA. the state class uses a label and a set of edges (edge1 and edge 2) depending on if the NFA needs multiple edges(may only use 1 edge). The label points to the character in postfix while the set of edges are to connect the set’s of nfa’s states. 

3. The smaller NFA’s are used to create the overall NFA using the compile function which takes the postfix expression and loops through each character and based on that character (special character - change states and append nfa’s to stack and non special characters - append as nfa’s with label of character and accept state) , it creates the smaller NFA’s which are added and removed from the stack until one NFA remains after all characters have been looped through and that is used as the overall NFA which is returned

4. The matching algorithm uses the returned NFA in order to match the expression and the string. The matching algorithm first executes both the functions shunt and compile to get the overall NFA. Then the overall NFA’s initial state is added to the current state by calling the followes function (using the NFA’s initial) which follows the edges of the NFA and returns the set of states which can be reached by following the edges. Then loop through each character in the string and each state in current set of states, if the states label is equal to the current character from the string, then call the followes function (with the state’s 1st edge) and return into next set of states. Set current set of states equal to the next set of states and clear the next set of states. When this is complete for full string, then return whether the accept state is in the current set of states, return true if so and false if it is not the case.

5. (Extra) Interface: Asks user for input, whether they want to view pre-generated infixed expressions and strings being matched or if they want to manually want to enter an infix expression and a string which are stored in variables using the input() function and matched using the match function sending the entered values as parameters. The interface is run using a while loop controlled with a boolean variable, which when the user selects the exit option, the loop control variable is set to True, which exits the loop. Also when the user enters incorrect input option the loop circles back after telling them their input is invalid.

 ## How to run program: 
 - Clone repository from github or else copy the python code into a python file.
 - In command line, cd (change directory) into the folder where the file is stored.
 - From the command line, type python followed by the file name, e.g. python ThompsonsAlgorithm.py.
 - User interface will display, which gives user 4 options to choose from,the first 2 options (activated by entering 1 or 2 respectively as input value) involve testing using pre-generated expressions and strings to test operators and see if they match, while the 3rd option allows users to enter their own input for the infix expression and string to see if they match(3 must be entered as option value in console interface to access this), when selecting this option users enter the infix expression first, followed by the string they wish to match.
 - To exit the application the user must enter 4 as the option in the console interface.

