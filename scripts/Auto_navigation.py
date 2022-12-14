#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist, Point
from turtlesim.msg import Pose
from math import pow, atan2, sqrt



class Move_turtle:


    def __init__(self):
        #Creates a node with name 'Turtlesim_Navigation',
        # unique node (using anonymous=True).
        rospy.init_node('Turtlesim_Auto_Navigation', anonymous=True)

        # Publisher which will publish to '/turtle1/cmd_vel'
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        
        # Subscriber which will Subscrib to '/turtle1/pose'
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose',Pose, self.update_des_pose)
        self.rate = rospy.Rate(50)
        rospy.loginfo("Started publishing values")
        #Initialized Variable
        self.linear_vel = 1.5
        self.angular_vel = 5.0
        
    #================================================================
    #sets the velocity value, only if not reached the destination
    #else stop the Turtle
    def Turn_and_Go(self):

        try:
            
            
            Dis_tolerance = 0.1
            angular_tolerance = 0.0
            #Calculates the distance between current and destination point
            #Using Pythogorus 
            def distancetogoal():
                try:
                    
                    distancetogoal = sqrt(pow((Des_point.x - self.pose.x), 2) + pow((Des_point.y - self.pose.y), 2))

                    return distancetogoal
                except Exception as e: # Error in Getting the distance to Goal
                    print(e)
            #================================================================
            #Sets the Angle / Head of the turtle to destination point
            def angle_to_rotate():
        
                try:
                    deltaX = Des_point.x - self.pose.x
                    deltaY = Des_point.y - self.pose.y
                    #Returns the values in radians
                    Des_Heading = atan2(deltaY, deltaX)
                    angle_to_rotate = Des_Heading - self.pose.theta

                    return round(angle_to_rotate,2)

                except Exception as e3: # Error in GetHeading Def.
                    print(e3)
            #================================================================
            #Publishes Twist values to Topic turtle1/cmd_vel
            def Turtle(linear,angular):
                vel_command.linear.x = linear
                vel_command.angular.z = angular
                self.velocity_publisher.publish(vel_command)
                self.rate.sleep()

            while True:
                Des_point.x = float (input("Set your x goal:"))
                Des_point.y = float(input("Set your y goal:"))
                while abs(distancetogoal()) >= Dis_tolerance:
                    #Turns the Turtle to Destination point 
                    Turtle(0.0,self.angular_vel * angle_to_rotate())   
                    
                    # if the Turtle is pointing towards the Destination point 
                    # and moves towards its Destination
                    if abs(angle_to_rotate()) <= angular_tolerance:
                        #Moving towards Destination
                        Turtle(self.linear_vel * distancetogoal(),0.0)

                #if Turtle reaches the Destination
                rospy.loginfo("Goal has been reached")
                vel_command.linear.x = 0.0
                vel_command.angular.z= 0.0
                self.velocity_publisher.publish(vel_command)
                self.rate.sleep()
                
            
        except Exception as e1 : #Error in Settin up the velocity
            print(e1)
    #=================================================================

    #Update the destination point when a messages is published 
    def update_des_pose(self,data):  
        try:
            self.pose = data
            self.pose.x = round(self.pose.x,4)
            self.pose.y = round(self.pose.y,4)
            

        except Exception as e2: #Error in Updating Pose
            print(e2)

#Main Function to this Program, which calls Teleop() and 
if __name__ == '__main__':
    try:
        
        #Testing the function
        Des_point = Pose()
        vel_command = Twist()
        x = Move_turtle()
        x.Turn_and_Go()
        rospy.spin()
    except rospy.ROSInterruptException: 
        pass
