# PDE4430_Course_work-1:

The Objective of this coursework is to perform various tasks with turtle, which includes;
a. Teleoperation using the keyboard, with an option to change speed
b. Autonomous Navigation to any given coordinates in the Turtlesim window 
c. Avoiding Wall Collision - override the movement is wall hitting the wall 
d. Vacuum Cleaner Behaviour - covering the entire window in an efficient manner



## Setup :
1. ROS Noetic
2. Ubuntu 20.04


## Tasks
### Task 1: Teleoperating ROS Turtle using a keyboard:
In this Task, we will see how to teleoperate a robot manually using a keyboard. Using a keyboard, we can translate and rotate the robot. One of the basic example to demonstrate keyboard teleoperation is ROS turtlesim.
The launch file [Teleop_key.launch](https://github.com/mdileepkumar438/PDE4430_CW1/blob/main/launch/Teleop_key.launch)

### Task 2: Navigate the turtlebot from a random location to an input location:
The parameter for setting linear velocity is taken as distance (always positive) from goal. It could also be (current_coordinate - goal_coordinate), 
and angel to rotate the head of the turtle towards the givien coordinate. However, this can also be resolved by setting appropriate angular velocities, which is what has been done here.
The launch file [Auto_navigation.launch](https://github.com/mdileepkumar438/PDE4430_CW1/blob/main/launch/Auto_navigation.launch) to reproduce the results. 


