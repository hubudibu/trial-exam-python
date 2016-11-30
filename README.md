# TRIAL EXAM: Python Basics

### Getting Started
 - Fork this repository under your own account
 - Clone the forked repository to your computer
 - Commit your progress frequently and with descriptive commit messages
 - All your answers and solutions should go in this repository

### What can I use?
 - You can use any resource online, but **please work individually**
 - Instead of copy-pasting your answers and solutions, write them in your own words.


# Tasks
## 1-5. Complete the tasks seen in the 1-5.py files! (~90 mins)
### Acceptance criteria
The application is accepted if:
- The solution works according to specification [1p each]
- The solution follows [styleguide](https://github.com/greenfox-academy/teaching-materials/blob/master/styleguide/python.md) [1p]
- Has proper error handling where the specification says it [1p each]
- Has the correct loops, methods, filters [1p each]
- The code is clean, without unnecessary repetition, and with descriptive names [1p each]
- You commit frequently with descriptive commit messages [1p]

## 6. Question time! (~30 mins) [6p]

### Explain the algorithm used in exercise 2. Use a flowchart, structogram or pseudo code. [2p]
#### Your answer: First the function tests whether the given file exists. If not, the returned value is zero. If it exists, it loops through the letters of the given filename and checks, whether the letter is an 'a' or not. If so, it increases the counter by 1. When it is finished with the last letter in the filename, it returns the value of the counter. You can see how it works on the flowchart: flowchart_2py.png

### How can you get a random number in python? [2p]
#### Your answer: If you import Python's random module, you can use the randint built-in function, which can generate a random integer between the borders that you allow. For example, if you call random.randint(1, 5), it will give you a random integer, which is bigger than 0, but not bigger than 5.
####An other option is to use the choice built-in function (also from the random module). With the choice function, you can choose a random element from a given list. So, if we add numbers to a list, we can choose random numbers from it.

### What does M stand for in MVC? [2p]
#### Your answer: M means the Model part of the MVC structure. The model part contains all the necessary information, how the program is built-up, how the logical elements are connected in our code.
