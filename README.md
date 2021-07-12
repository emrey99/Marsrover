# Mars rover

A rover lands on a plateau on Mars. We can navigate the rover so we can see everything around.



# Description

The application allows us to have control over a rover which is landed on Mars. The rover is located on a rectangular plateau. We can move the rover without going out of the plateau.
The movements happen when we call the 'run_command' method which basically runs a for cycle with the 'L' , 'R' or 'M' letters . 'L' is when we want the rover to move left , respectively
'R' is for the rover to turn right and 'M' is the final one which helps us to move the rover forward. Moreover , the rover has its position heading one of the compass points.
To make it more clear , we can imagine a grid with x and y axis . So if the current letter is 'M' or in other words we want to move the rover forward , this depends on the point the 
rover is currently located. The rover has its own position on the plateau. So if the rover is facing 'North(N)' and we want to 'Move(M)' it forward , we will increase its position y.
Same thing another story , if it does face 'South(S)' and we want it to move forward , the method 'move' will call another method which will help us to decrease the rover's y value.
This practice helps us to have control over the rover.

# Technology

Python 3.7

# How can we run it

First, download the source code . Go to the Windows command prompt. One option is to choose Run from the Windows Start menu, type cmd, and click OK.
Use the "cd" command to change to the folder containing the program you wish to run. Run the command line program by typing its name and pressing 'Enter'.

