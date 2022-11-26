#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt

pose = Pose()

def move(linear,angular):
    vel_command.linear.x = linear
    vel_command.angular.z = angular
    velocity_pub.publish(vel_command)
    rate.sleep()

def Displacement():
    try:
        
        Displacement = sqrt(pow((Des_point.x - pose.x), 2) + pow((Des_point.y - pose.y), 2))
        return Displacement
    except Exception as e: # Error in Getting the distance to Goal
        print(e)


def steering_angle():
    try:
        steering_angle = atan2(Des_point.y - pose.y, Des_point.x - pose.x) - pose.theta
        return round(steering_angle,2)
    except Exception as e3: # Error in GetHeading Def.
        print(e3)

def movement():

    Des_point.x = float (input("Set your x goal:"))
    Des_point.y = float(input("Set your y goal:"))
    Dis_tolerance = 0.1
    angular_tolerance = 0.0
  
    while not rospy.is_shutdown:
        while abs(Displacement()) >= Dis_tolerance:

            move(0,angular_vel * steering_angle())
            if (abs(steering_angle())<=angular_tolerance):
                move(linear_vel * Displacement(),0)

        rospy.loginfo("Goal has been reached")
        vel_command.linear.x = 0.0
        vel_command.angular.z= 0.0
        velocity_pub.publish(vel_command)
        rate.sleep()
    


def position(data):  
    
    pose = data
    pose.x = round(pose.x,4)
    pose.y = round(pose.y,4)


#Main Function to this Program, which calls Teleop() and 
if __name__ == '__main__':
    try:
       
        rospy.init_node('Turtlesim_Auto_Navigation', anonymous=True)

        velocity_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
        pose_subscriber = rospy.Subscriber('/turtle1/pose',Pose, position)
        rate = rospy.Rate(50)
        
        rospy.loginfo("Started publishing values")

        #Initialized Variable
        linear_vel = 1.5
        angular_vel = 4.0

        #Testing the function
        Des_point = Pose()
        vel_command = Twist()
        movement()
        rospy.spin()
    except rospy.ROSInterruptException: 
        pass
