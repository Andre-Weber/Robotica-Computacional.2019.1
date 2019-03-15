#! /usr/bin/env python
#coding: utf-8

import rospy
from geometry_msgs.msg import Twist, Vector3
from math import pi

v = 0.3  # Velocidade linear
w = pi/3  # Velocidade angular
stop = 0
if __name__ == "__main__":
    rospy.init_node("roda_exemplo")
    pub = rospy.Publisher("cmd_vel", Twist, queue_size=3)

    try:
        while not rospy.is_shutdown():

        	vel_forw = Twist(Vector3(v,0,0), Vector3(0,0,0))
        	vel_turn = Twist(Vector3(0,0,0), Vector3(0,0,w))
        	vel_stop = Twist(Vector3(0,0,0), Vector3(0,0,0))



        	if stop == 0:
        		pub.publish(vel_stop)
        		rospy.sleep(2)

        	while stop <= 4:
        		pub.publish(vel_stop)
	        	rospy.sleep(2)

	        	pub.publish(vel_forw)
	        	rospy.sleep(1.8)


	        	pub.publish(vel_stop)
	        	rospy.sleep(2)


	        	pub.publish(vel_turn)
	        	rospy.sleep(1.5)

	        	pub.publish(vel_stop)
	        	rospy.sleep(2)

            

        		stop += 1








    except rospy.ROSInterruptException:
        print("Ocorreu uma exceção com o rospy")