#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist 
from geometry_msgs.msg import Pose2D 
from turtlesim import Pose as pose
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
def getHeadingError() {
 
  deltaX = Des_position.x - current.x
  deltaY = Des_position.y - current.y

  Des_Heading = atan2(deltaY, deltaX)
  headingError = Des_Heading - current.theta
   
  #Make sure heading error falls within -PI to PI range
  if (headingError > PI) {
    headingError = headingError - (2 * PI);
  } 
  if (headingError < -PI) {
    headingError = headingError + (2 * PI);
  } 
   
  return headingError
}



#================================================================
#sets the velocity value, only if not reached the destination
#else stop the Turtle
def set_velocity():

    try:
        distancetogoal = distancetogoal()
        heading_error = getHeadingError()

        if ( gotodestination==True & abs(distancetogoal())> Dis_tolerance):
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
        pose.x = pose.x
        pose.y = pose.y
        pose.theta = pose.theta
        

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
        PI = 3.141592654
        
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
