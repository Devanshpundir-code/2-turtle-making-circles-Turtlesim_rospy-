#!/usr/bin/python3

import rospy 
from geometry_msgs.msg import Twist 

def funtion():

    rospy.init_node("turtle", anonymous=True)
    turtle2_publisher = rospy.Publisher("/turtle_tutorial/cmd_vel", Twist, queue_size=10)
    turtle1_publisher = rospy.Publisher("//turtle1/cmd_vel", Twist, queue_size=10)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        # this is for our turtle1_publisher
        linear_velocity = 1.5
        angular_velocity = 3.0

        # now publish them
        twist = Twist()
        twist.linear.x = linear_velocity
        twist.angular.z = angular_velocity
        turtle1_publisher.publish(twist)

        # now for second turtle 

        twist1 = Twist()
        twist1.linear.x = 2
        twist1.angular.z = 3
        turtle2_publisher.publish(twist1)
        rate.sleep()


if __name__ == "__main__":
    funtion()


