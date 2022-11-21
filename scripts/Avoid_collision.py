#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose



   
def avoid_collision(linear,angular):
    cmd_value=Twist()
    cmd_value.linear.x = linear
    cmd_value.angular.z = angular 
    pub.publish(cmd_value)
    rate.sleep()
     
    
#Update the destination point when a messages is published 
def pose_update(data):  
    try:

        pose = data
        pose.x = round(pose.x,2)
        pose.y = round(pose.y,2)
        #rospy.loginfo("hit on wall 1")
        
        if ((pose.x == 0.5) or (pose.y == 10.5)):
            rospy.loginfo("hit")
            avoid_collision(0.0,1.0)
    except Exception as e2: #Error in Updating Pose
        print(e2)

if __name__ == '__main__':
    try:
        rospy.init_node('Turtlesim_Avoid_collision', anonymous=True)
        # Publisher which will publish to '/turtle1/cmd_vel'
        pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        pose_subs = rospy.Subscriber('/turtle1/pose',Pose, pose_update)
        rate = rospy.Rate(10)
        #avoid_collision()
        #Testing the function
        #avoid_collision()
        

        rospy.spin()
    except rospy.ROSInterruptException: 
        pass