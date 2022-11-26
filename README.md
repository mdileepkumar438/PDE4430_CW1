# PDE4430_Course_work-1:

The Objective of this coursework is to perform various tasks with turtle, which includes;

- Teleoperation using the keyboard, with an option to change speed
- Autonomous Navigation to any given coordinates in the Turtlesim window 
- Avoiding Wall Collision - override the movement is wall hitting the wall 
- Vacuum Cleaner Behaviour - covering the entire window in an efficient manner



## Projects
Project folders in this repository are complete on their own and require no additional downloads.
Contents of each project should be placed in the ```src``` folder of the catkin workspace. To avoid any possible conflicts,
it's advised to have a separate workspace for every project.



## Setup :
1. ROS Noetic
2. Ubuntu 20.04

#

## Tasks
### Task 1: Teleoperating ROS Turtle using a keyboard:

In this Task, we will see how to teleoperate a robot manually using a keyboard. Using a keyboard, we can translate and rotate the robot. One of the basic example to demonstrate keyboard teleoperation is ROS turtlesim.
The launch file [Teleop_key.launch](https://github.com/mdileepkumar438/PDE4430_CW1/blob/main/launch/Teleop_key.launch).

For reference [Turtlesim.py](https://github.com/mdileepkumar438/PDE4430_CW1/blob/main/scripts/turtle_teleoperation.py)

- Type this command ```roslaunch pde4430_cw1 Teleop_key.launch```

<img width="735" alt="Screenshot 2022-11-26 at 7 12 18 PM" src="https://user-images.githubusercontent.com/102908088/204095814-9b68afec-fad1-427d-b9ba-af102ab7052b.png">

- Message is displayed in terminal 

<img width="400" alt="Screenshot 2022-11-26 at 7 17 16 PM" src="https://user-images.githubusercontent.com/102908088/204096230-bd1ed71a-bf27-42db-8831-269fe9663c9a.png">

- Final Output of this task :

<img width="640" alt="Screenshot 2022-11-26 at 7 16 44 PM" src="https://user-images.githubusercontent.com/102908088/204096289-5b25259d-1c6a-4e04-b8d2-f861a86a527d.png">

<img width="640" alt="Screenshot 2022-11-26 at 7 25 31 PM" src="https://user-images.githubusercontent.com/102908088/204096352-0f7d388a-e866-42b8-9354-4604c83f48ac.png">

Click this link for Video [Teleoperation video]

#

### Task 2: Navigate the turtlebot from a random location to an input location:

The parameter for setting linear velocity is taken as distance (always positive) from goal. It could also be (current_coordinate - goal_coordinate), 
and angel to rotate the head of the turtle towards the givien coordinate. However, this can also be resolved by setting appropriate angular velocities, which is what has been done here.
The launch file [Auto_navigation.launch](https://github.com/mdileepkumar438/PDE4430_CW1/blob/main/launch/Auto_navigation.launch) to reproduce the results.

For reference [Turtlesim.py](https://github.com/mdileepkumar438/PDE4430_CW1/blob/main/scripts/Auto_navigation.py)

- Type this command ```roslaunch pde4430_cw1 Auto_navigation.launch```

<img width="735" alt="Screenshot 2022-11-26 at 8 03 33 PM" src="https://user-images.githubusercontent.com/102908088/204098061-0c98b216-77e1-4c63-ad09-f8a64e1d410b.png">

- Enter the Coordinates Range should be between [0 - 11] in both x and y direction
```
[INFO] [1669478618.925063]: Started publishing values
Set your x goal:1
Set your y goal:1
[INFO] [1669478709.568750]: Goal has been reached
Set your x goal:1
Set your y goal:10
[INFO] [1669478866.082373]: Goal has been reached
```

- Final output of this Task

<img width="640" alt="Screenshot 2022-11-26 at 8 04 12 PM" src="https://user-images.githubusercontent.com/102908088/204098113-dd282ec7-aef5-482e-a82d-bde95d0b629b.png">


<img width="640" alt="Screenshot 2022-11-26 at 8 08 02 PM" src="https://user-images.githubusercontent.com/102908088/204098119-d8770706-0012-432f-8560-d04a8f12ade4.png">

#

### Task 3: Avoiding Wall Collion When it reaches certain pre-defined border:

This Task overwrites the position of the Turtle when ever it reaches the border and makes a turn and also using the ``Teleop_key`` to move the `Turtle`. 
The Launch file [Avoid_collision.launch](https://github.com/mdileepkumar438/PDE4430_CW1/blob/main/launch/Avoid_collision.launch) for reporduce the results.

For program reference [Avoid_collision.py](https://github.com/mdileepkumar438/PDE4430_CW1/blob/main/scripts/Avoid_collision.py)

- Type the command ``` roslaunch pde4430_cw1 Avoid_collision.launch ``` :


- Displaying this message in Terminal
``
x = [0.75, 10.5]  
y = [0.75, 10.5]
``

- Final output of this Task:












