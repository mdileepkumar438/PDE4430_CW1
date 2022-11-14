#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist 
from geometry_msgs.msg import Pose2D 
from turtlesim import Pose

#==============================================
#Calculates distance from Goal 
# (Current x to destination x coordinat)
def distancetogoal():
    return Des_position.x - Current_position.x
#==============================================






#Main Function to this Program, which calls Teleop() and 
if __name__ == '__main__':
    try:
        pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        rospy.init_node('Turtlesim_teleoperator', anonymous=False)
        rospy.loginfo("Started publishing values")
        rate = rospy.Rate(100) # 10hz
        vel_command = Twist()
        Current_position = Pose2D()
        Des_position = Pose2D()
        Goal = 1.3
        linear_vel = 1.0
        Dis_tolerance = 0.1

        #Initialized Variable
        Des_position.x =  Goal

        #Initialized Twist msg
        vel_command.linear.x = 0.0
        vel_command.linear.y = 0.0
        vel_command.linear.z = 0.0
        vel_command.angular.x = 0.0
        vel_command.angular.y = 0.0
        vel_command.angular.z = 0.0
        

        
    except rospy.ROSInterruptException: 
        pass
