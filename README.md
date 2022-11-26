# Mobile Robotics

## PDE4430_Course_work-1:

The Objective of this coursework is to perform various tasks with turtle, which includes;

- Teleoperation using the keyboard, with an option to change speed
- Autonomous Navigation to any given coordinates in the Turtlesim window 
- Avoiding Wall Collision - override the movement is wall hitting the wall 
- Vacuum Cleaner Behaviour - covering the entire window in an efficient manner



## Projects
Project folders in this repository are complete on their own and require no additional downloads.
Contents of each project should be placed in the ```src``` folder of the catkin workspace. To avoid any possible conflicts,
it's advised to have a separate workspace for every project. 

<img width="900" alt="Screenshot 2022-11-26 at 11 51 22 PM" src="https://user-images.githubusercontent.com/102908088/204106880-ad56e22b-7cdb-4493-92d3-05d1490a0ebc.png">


Every `.py` and `.launch` files needs to be an executable file. 

To do that, Open the `Terminal` Go to File location as shown in below image

<img width="640" alt="Screenshot 2022-11-26 at 11 54 15 PM" src="https://user-images.githubusercontent.com/102908088/204106887-a2aa4694-50de-45a2-af0b-136591021a0f.png">


- Type ```chmod +x filename.launch``` for execution of launch file and

<img width="640" alt="Screenshot 2022-11-26 at 11 54 55 PM" src="https://user-images.githubusercontent.com/102908088/204106901-da3f7d9f-bc00-4e07-a2d9-fc444669a1ef.png">


- Type ```chmod +x filename.py``` for `.py` files



## Setup :
1. ROS Noetic
2. Ubuntu 20.04

#

## Tasks
### Task 1: Teleoperating ROS Turtle using a keyboard

In this Task, we will see how to teleoperate a robot manually using a keyboard. Using a keyboard, we can translate and rotate the robot. One of the basic example to demonstrate keyboard teleoperation is ROS turtlesim.
The launch file [Teleop_key.launch](https://github.com/mdileepkumar438/PDE4430_CW1/blob/main/launch/Teleop_key.launch).

For reference [Turtlesim.py](https://github.com/mdileepkumar438/PDE4430_CW1/blob/main/scripts/turtle_teleoperation.py)



- Type this command ```roslaunch pde4430_cw1 Teleop_key.launch```

<img width="735" alt="Screenshot 2022-11-26 at 7 12 18 PM" src="https://user-images.githubusercontent.com/102908088/204095814-9b68afec-fad1-427d-b9ba-af102ab7052b.png">

- Message is displayed in `terminal` 

```
#Prints Directional message on Terminal 
info_msg= """
Reading from the keyboard  and Publishing to Twist!
---------------------------------------------------
Moving around:
    w
a   s   d
---------------------------------------------------
Up / Down : increase/decrease max speeds
< / > : increase/decrease max angular speed
---------------------------------------------------
CTRL + C to quit
"""

```

<img width="400" alt="Screenshot 2022-11-26 at 7 17 16 PM" src="https://user-images.githubusercontent.com/102908088/204096230-bd1ed71a-bf27-42db-8831-269fe9663c9a.png">

- Final `Output` of this task :

<img width="640" alt="Screenshot 2022-11-26 at 7 16 44 PM" src="https://user-images.githubusercontent.com/102908088/204096289-5b25259d-1c6a-4e04-b8d2-f861a86a527d.png">

<img width="640" alt="Screenshot 2022-11-26 at 7 25 31 PM" src="https://user-images.githubusercontent.com/102908088/204096352-0f7d388a-e866-42b8-9354-4604c83f48ac.png">

- RQT Graph : type ```rqt_graph```

<img width="640" alt="Screenshot 2022-11-26 at 11 33 43 PM" src="https://user-images.githubusercontent.com/102908088/204106268-1deb0893-a85e-42fc-ac2b-ab313dd729ac.png">

#

### Task 2: Navigate the turtlebot from a random location to an input location

The parameter for setting linear velocity is taken as distance (always positive) from goal. It could also be (current_coordinate - goal_coordinate), 
and angel to rotate the head of the turtle towards the givien coordinate. However, this can also be resolved by setting appropriate angular velocities, which is what has been done here.
The launch file [Auto_navigation.launch](https://github.com/mdileepkumar438/PDE4430_CW1/blob/main/launch/Auto_navigation.launch) to reproduce the results.

For reference [Turtlesim.py](https://github.com/mdileepkumar438/PDE4430_CW1/blob/main/scripts/Auto_navigation.py)



- Type this command ```roslaunch pde4430_cw1 Auto_navigation.launch```

<img width="735" alt="Screenshot 2022-11-26 at 8 03 33 PM" src="https://user-images.githubusercontent.com/102908088/204098061-0c98b216-77e1-4c63-ad09-f8a64e1d410b.png">

- Enter the Coordinates Range should be between `[0 - 11]` in both `x`and `y` direction
```
[INFO] [1669478618.925063]: Started publishing values
Set your x goal:1
Set your y goal:1
[INFO] [1669478709.568750]: Goal has been reached
Set your x goal:1
Set your y goal:10
[INFO] [1669478866.082373]: Goal has been reached
```

- Final `Output` of this Task

<img width="640" alt="Screenshot 2022-11-26 at 8 04 12 PM" src="https://user-images.githubusercontent.com/102908088/204098113-dd282ec7-aef5-482e-a82d-bde95d0b629b.png">


<img width="640" alt="Screenshot 2022-11-26 at 8 08 02 PM" src="https://user-images.githubusercontent.com/102908088/204098119-d8770706-0012-432f-8560-d04a8f12ade4.png">

- RQT Graph : type ```rqt_graph```

<img width="640" alt="Screenshot 2022-11-26 at 11 34 41 PM" src="https://user-images.githubusercontent.com/102908088/204106275-da6e0506-a874-4410-947d-5e8938b9a232.png">

#

### Task 3: Avoiding Wall Collion When it reaches certain pre-defined border

This Task overwrites the position of the `Turtle` when ever it reaches the border and makes a turn and also using the ``Teleop_key`` to move the `Turtle`. 
The Launch file [Avoid_collision.launch](https://github.com/mdileepkumar438/PDE4430_CW1/blob/main/launch/Avoid_collision.launch) for reporduce the results.

For program reference [Avoid_collision.py](https://github.com/mdileepkumar438/PDE4430_CW1/blob/main/scripts/Avoid_collision.py)



- Type the command ``` roslaunch pde4430_cw1 Avoid_collision.launch ``` :

<img width="735" alt="Screenshot 2022-11-26 at 8 36 08 PM" src="https://user-images.githubusercontent.com/102908088/204099895-e509fe3f-6e10-491b-9164-a55f9431160e.png">

- Displaying this message in `Terminal`
```
Borders of the wal to avoid :
x = [0.75, 10.5]  
y = [0.75, 10.5]
```

<img width="300" alt="Screenshot 2022-11-26 at 8 37 04 PM" src="https://user-images.githubusercontent.com/102908088/204099902-d703c56d-9b8d-4dce-9e94-6ce38b884550.png">

- Final `output` of this Task:


<img width="640" alt="Screenshot 2022-11-26 at 8 43 41 PM" src="https://user-images.githubusercontent.com/102908088/204099931-f7a37943-1536-49b7-b5d2-043530ab7589.png">


<img width="640" alt="Screenshot 2022-11-26 at 8 39 05 PM" src="https://user-images.githubusercontent.com/102908088/204099935-1c550fcd-ca9d-4b5a-9f4f-8f2377a49ba4.png">

- RQT Graph : type ```rqt_graph```

<img width="640" alt="Screenshot 2022-11-26 at 11 38 48 PM" src="https://user-images.githubusercontent.com/102908088/204106347-cd6a3e5f-9eca-494b-bfe9-dd7eecbc64a8.png">


#

### Task 4: Implementing Vaccum Cleaning Behaviour with maximum accelerations and form a grid path

This Task is mainly focused on the covering the `Turtlesim window` in a `Grid` path, Using the Pre-defined coordinates. The launch file [Vacuum_cleaner.launch](https://github.com/mdileepkumar438/PDE4430_CW1/blob/main/launch/Vacuum_cleaner.launch)

For program reference : [Vacuum_cleaner.py](https://github.com/mdileepkumar438/PDE4430_CW1/blob/main/scripts/vacuum_cleaner.py)



*Grid*

The grid task can be though as `discrete` sections.
1.	From any random location, go to the starting position in fastest way possible.
2.	Thereafter, grid points are `defined` which have to be followed. Hence, `fastest` way would give a curvature and not follow lines. Thus, grid corners are defined.
3.	Finally, the grid function is defined. Grid_corners contain x,y coordinates,


- Type to Launch file ```roslaunch pde4430_cw1 Vacuum_cleaner.launch```

<img width="735" alt="Screenshot 2022-11-26 at 9 13 28 PM" src="https://user-images.githubusercontent.com/102908088/204101927-1a64217c-6f9f-4522-afe3-042521de0a91.png">

- It covers the window in Grid path:

<img width="700" alt="Screenshot 2022-11-26 at 9 14 10 PM" src="https://user-images.githubusercontent.com/102908088/204101932-d59aa282-d7dd-4357-b3ec-e0c75c493786.png">

<img width="200" alt="Screenshot 2022-11-26 at 9 15 00 PM" src="https://user-images.githubusercontent.com/102908088/204101973-b84ed5c9-c0f9-47c0-878d-9b2f428d442b.png"> <img width="200" alt="Screenshot 2022-11-26 at 9 16 04 PM" src="https://user-images.githubusercontent.com/102908088/204101977-8964bf0d-6454-43fc-a1f7-6ea048e1e839.png"> <img width="200" alt="Screenshot 2022-11-26 at 9 16 58 PM" src="https://user-images.githubusercontent.com/102908088/204102069-6e8f2c1a-2296-4cc1-a031-a529be3776e7.png">

- Final Output of this Task


<img width="640" alt="Screenshot 2022-11-26 at 9 17 48 PM" src="https://user-images.githubusercontent.com/102908088/204102059-f59c24f6-9eb8-4b80-b59a-07bd569dd09e.png">

- RQT Graph : type ```rqt_graph```

<img width="640" alt="Screenshot 2022-11-26 at 11 39 40 PM" src="https://user-images.githubusercontent.com/102908088/204106371-c657dc8e-5da2-4c8b-b09f-e4125eeb447f.png">


#
## Click this link for Video [Mobile_robotics_CW_video](https://youtu.be/UmdqTGg1WU8)
#
 


