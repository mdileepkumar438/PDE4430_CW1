#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt

#================================================================
#Calculates distance from Goal 
# (Current x to destination x coordinat)
def distancetogoal():
    try:
        Distance = sqrt(pow(Des_position.x - Current_position.x)+pow(Des_position.x - Current_position.y))
        return Distance

    except Exception as e: # Error in Getting the distance to Goal
        print(e)

#================================================================
def getHeadingError():
 
  deltaX = Des_position.x - Current_position.x
  deltaY = Des_position.y - Current_position.y

  Des_Heading = atan2(deltaY, deltaX)
  headingError = Des_Heading - Current_position.theta
   
  #Make sure heading error falls within -PI to PI range
  if (headingError > PI): 
    headingError = headingError - (2 * PI)
  
  if (headingError < -PI): 
    headingError = headingError + (2 * PI)
  
   
  return headingError




#================================================================
#sets the velocity value, only if not reached the destination
#else stop the Turtle
def set_velocity():

    try:
        distancetogoal = distancetogoal()
        heading_error = getHeadingError()

        if ( gotodestination==True & abs(distancetogoal())> Dis_tolerance):
            
            if (abs(heading_error)> angular_tolerance):            
                vel_command.linear.x = 0.0
                vel_command.angular.z = angular_vel * heading_error

            else:
                
                vel_command.linear.x = linear_vel * distancetogoal()
                vel_command.linear.x = 0.0

        else:
            rospy.loginfo("Goal has been reached")
            vel_command.linear.x = 0.0
            vel_command.angular.z= 0.0
            gotodestination == False
    
    except Exception as e1 : #Error in Settin up the velocity
        print(e1)


#================================================================
#=================================================================

#Update the destination point when a messages is published 
def update_des_pose(data):  
    try:
        Des_pose = data
        Des_position.x = Des_pose.x
        Des_position.y = Des_pose.y
        gotodestination == True

    except Exception as e2: #Error in Updating Pose
        print(e2)


#Main Function to this Program, which calls Teleop() and 
if __name__ == '__main__':
    try:
        #Creates a node with name 'Turtlesim_Navigation',
        # unique node (using anonymous=True).
        rospy.init_node('Turtlesim_Auto_Navigation', anonymous=True)

        # Publisher which will publish to '/turtle1/cmd_vel'
        velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

        # Subscriber which will Subscrib to '/turtle1/pose'
        pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, update_des_pose)
        pose = Pose()
        rate = rospy.Rate(10)
        rospy.loginfo("Started publishing values")


        vel_command = Twist()
        
        PI = 3.141592654
        
        linear_vel = 0.5
        angular_vel = 0.5
        Dis_tolerance = 0.1
        angular_tolerance = 0.1
        gotodestination = False

        #Initialized Variable
        Current_position = Pose()
        Des_position = Pose()

        Des_position.x = input("Set your x goal:")
        Des_position.y = input("Set your y goal:")

        #Des_position.x =  5.54
        #Des_position.y = 5.54

        #Initialized Twist msg
        vel_command.linear.x = 0.0
        vel_command.linear.y = 0.0
        vel_command.linear.z = 0.0
        vel_command.angular.x = 0.0
        vel_command.angular.y = 0.0
        vel_command.angular.z = 0.0
        

        
    except rospy.ROSInterruptException: 
        pass
