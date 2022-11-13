#!/usr/bin/env python3

import getch
import rospy
from geometry_msgs.msg import Twist


#Prints Directional message on Terminal 
info_msg= """

Reading from the keyboard  and Publishing to Twist!
---------------------------------------------------


---------------------------------------------------

Up / Down : increase/decrease max speeds
< / > : increase/decrease max angular speed

---------------------------------------------------

CTRL + C to quit
"""

#This is Teleop function, sends the Linear and angular values to Twist msg
def Teleop():
    
    try:
        print(info_msg)
        while not rospy.is_shutdown():
            key = ord(getch.getch())
            print(key)
            if key == 119:
                rospy.loginfo("Forward")
                turtle_move(linear_speed,0.0)
            if key == 115:
                rospy.loginfo("Backward")
                turtle_move(-linear_speed,0.0)
            if key == 100:
                rospy.loginfo("Right")
                turtle_move(0.0,-angular_speed)
            if key == 97:
                rospy.loginfo("Left")
                turtle_move(0.0,angular_speed)

            # Variable speed for keys Up / Down / left / Right arrows
            if key == 65:
                rospy.loginfo("Forward")
                turtle_move(var_linear_speed,0.0)

            if key == 66:
                rospy.loginfo("Backward")
                turtle_move(-var_linear_speed,0.0)

            if key == 67:
                rospy.loginfo("Right")
                turtle_move(0.0,-var_angular_speed)

            if key == 68:
                rospy.loginfo("Left")
                turtle_move(0.0,var_angular_speed)

            

    except Exception as e: # could not publish key values to cmd_vel
        print(e)


#Adds Linear and angular values to Twist message as Linear.x and Angular.z
def turtle_move(linear,angular):
    try:
        twist = Twist()
        twist.linear.x = linear
        twist.linear.y = 0
        twist.linear.z =0
        twist.angular.x = 0 
        twist.angular.y = 0
        twist.angular.z = angular
        pub.publish(twist)
        rate.sleep()

    except Exception as e: #Error In Publishing Twist Message. 
        print(e)


#Main Function to this Program, which calls Teleop() and 
if __name__ == '__main__':
    try:
        pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        rospy.init_node('Turtlesim_teleoperator', anonymous=False)
        rospy.loginfo("Started publishing values")
        rate = rospy.Rate(100) # 10hz

        #Linear and angular speed is set to 1.0 and 0.5 respectively
        linear_speed = 1.0
        angular_speed = 0.5

        #Variable Linear and agular speed is Calculated. 
        var_linear_speed = linear_speed * 3.0
        var_angular_speed = angular_speed * 4.0

        #Calls Teleop() Function
        Teleop()
        
    except rospy.ROSInterruptException: 
        pass
