import rospy
from turtlesim.srv import Spawn
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt

def Turn_and_Go(X,Y):
    try:
        Des_point.x = X
        Des_point.y= Y 
        distancetogoal = sqrt(pow((Des_point.x - pose.x), 2) + pow((Des_point.y - pose.y), 2))
        angle_to_rotate = atan2(Des_point.y - pose.y, Des_point.x - pose.x) - pose.theta
        return (distancetogoal,angle_to_rotate)
    except Exception as e:
        print(e)

def Turn_and_Go_1(X,Y):
    try:
        Des_point.x = X
        Des_point.y= Y 
        distancetogoal_1 = sqrt(pow((Des_point.x - pose_1.x), 2) + pow((Des_point.y - pose_1.y), 2))
        angle_to_rotate_1 = atan2(Des_point.y - pose_1.y, Des_point.x - pose_1.x) - pose_1.theta
        return (distancetogoal_1,angle_to_rotate_1)
    except Exception as e:
        print(e)

#Update the destination point when a messages is published 
def update_des_pose(data):  
    try:
        pose = data
        pose.x = round(pose.x,4)
        pose.y = round(pose.y,4)
    
    except Exception as e2: #Error in Updating Pose
        print(e2)

#Update the destination point when a messages is published 
def update_des_pose_1(data):  
    try:
        pose_1 = data
        pose_1.x = round(pose_1.x,4)
        pose_1.y = round(pose_1.y,4)
    
    except Exception as e2: #Error in Updating Pose
        print(e2)

def turtle_spawn():
	
    rospy.init_node('turtle_spawn')
    rospy.wait_for_service('/spawn')
    try:
        add_turtle = rospy.ServiceProxy('/spawn', Spawn)
        response = add_turtle(0.0, 0.0, 0.0, "turtle4")
        return response.name
    except rospy.ServiceException as e: 
        print("Service call failed: %s"%e)



def multiple_bot():
    
    bot_2=[(10,10),(10,1),(1,1),(1,2),(9,2),(9,9),(0.5,9),(0.5,8),(8,8),(8,3),(1,3),(1,4),(7,4)]
    bot_1=[(0.5,5.5),(0.5,0.5),(10.5,0.5),(10.5,10.5),(0.5,10.5),(0.5,10)]

    for i in range(len(bot_1)):
        a = bot_1[i][0] 
        b = bot_1[i][1] 
        distancetogoal,angle_to_rotate=Turn_and_Go(a,b)
        while not rospy.is_shutdown():
                
            while abs(distancetogoal) >= Dis_tolerance:
                vel_command.linear.x = 0.0
                vel_command.angular.z = angular_vel * angle_to_rotate
                pub_1.publish(vel_command)   

                if abs(angle_to_rotate) <= angular_tolerance:
                    vel_command.linear.x = linear_vel * distancetogoal
                    vel_command.angular.z = 0.0
                    pub_1.publish(vel_command)
            break

    for i in range(len(bot_2)):
        a = bot_2[i][0] 
        b = bot_2[i][1] 
        distancetogoal_1,angle_to_rotate_1=Turn_and_Go_1(a,b)
        while not rospy.is_shutdown():
                
            while abs(distancetogoal_1) >= Dis_tolerance:
                 
                vel_command.linear.x = 0.0
                vel_command.angular.z = angular_vel * angle_to_rotate_1
                pub_2.publish(vel_command) 

                if abs(angle_to_rotate_1) <= angular_tolerance:
                    
                    vel_command.linear.x = linear_vel * distancetogoal_1
                    vel_command.angular.z = 0.0
                    pub_2.publish(vel_command) 
            break

if __name__ == "__main__":
    #Creates a node with name 'Turtlesim_Navigation',
    # unique node (using anonymous=True).
    rospy.init_node('Turtlesim_Multiple_vacuum_cleaner', anonymous=True)
    # Subscriber which will Subscrib to '/turtle1/pose'
    sub_1 = rospy.Subscriber('/turtle1/pose',Pose,update_des_pose)
    sub_2 = rospy.Subscriber('/turtle2/pose',Pose,update_des_pose_1)
    
    # Publisher which will publish to '/turtle1/cmd_vel'
    pub_1= rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    pub_2 = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)
    
    
    rate = rospy.Rate(100)
    
    rospy.loginfo("Started publishing values")
    #rospy.loginfo("Spwan turtle successfully [name:%s]" %(turtle_spawn()) )

    #Initialized Variable
    vel_command = Twist()
    pose = Pose()
    pose_1 = Pose()
    Des_point=Pose()
    Dis_tolerance = 0.1
    angular_tolerance = 0.0000
    linear_vel = 3.0
    angular_vel = 5.0
    turtle_spawn()
    multiple_bot()

    
    
