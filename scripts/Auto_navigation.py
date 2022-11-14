#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist 
from geometry_msgs.msg import Pose2D 
from turtlesim import Pose as pose

#================================================================
#Calculates distance from Goal 
# (Current x to destination x coordinat)
def distancetogoal():
    try:
        return Des_position.x - Current_position.x

    except Exception as e: # Error in Getting the distance to Goal
        print(e)


#================================================================
#sets the velocity value, only if not reached the destination
#else stop the Turtle
def set_velocity():

    try:
        if (abs(distancetogoal())> Dis_tolerance):
            vel_command.linear.x = linear_vel * distancetogoal()

        else:
            rospy.loginfo("Goal has been reached")
            vel_command.linear.x=0
    
    except Exception as e1 : #Error in Settin up the velocity
        print(e1)


#================================================================
#Update the current position and oreintation of Turtle
def updatepose(data):  
    try:
        pose = data
        pose.x = round(pose.x, 4)
        pose.y = round(pose.y, 4)
        pose.theta = round (pose.theta, 2)

    except Exception as e2: #Error in Updating Pose
        print(e2)


#=================================================================



#Main Function to this Program, which calls Teleop() and 
if __name__ == '__main__':
    try:
        # Publisher which will publish to the topic '/turtle1/cmd_vel'
        pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

        pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose(), updatepose())

        #Creates a node with name 'Turtlesim_Navigation',
        # unique node (using anonymous=True).
        rospy.init_node('Turtlesim_Navigation', anonymous=True)

        rospy.loginfo("Started publishing values")
        rate = rospy.Rate(10) # 10hz
        vel_command = Twist()
        Current_position = Pose2D()
        Des_position = Pose2D()
        
        linear_vel = 0.5
        angular_vel = 0.5
        Dis_tolerance = 0.1
        angular_tolerance = 0.1
        gotodestination = False
        
        #Initialized Variable
        Des_position.x =  5.54
        Des_position.y = 5.54

        #Initialized Twist msg
        vel_command.linear.x = 0.0
        vel_command.linear.y = 0.0
        vel_command.linear.z = 0.0
        vel_command.angular.x = 0.0
        vel_command.angular.y = 0.0
        vel_command.angular.z = 0.0
        

        
    except rospy.ROSInterruptException: 
        pass
