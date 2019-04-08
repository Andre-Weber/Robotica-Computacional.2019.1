#! /usr/bin/env python
# -*- coding:utf-8 -*-

import rospy
import numpy as np

from geometry_msgs.msg import Twist, Vector3
from std_msgs.msg import UInt8


def bumperzou(dado):
    print("Numero: ", dado.data)
    dados = dado
    global dados
    #print("Intensities")
    #print(np.array(dado.intensities).round(decimals=2))

    


if __name__=="__main__":

    rospy.init_node("le_scan")

    velocidade_saida = rospy.Publisher("/cmd_vel", Twist, queue_size = 3 )
    recebe_bumper = rospy.Subscriber("/bumper", UInt8, bumperzou)



    while not rospy.is_shutdown():
        vel_forw = Twist(Vector3(0.1,0,0), Vector3(0,0,0))
        vel_back = Twist(Vector3(-0.1,0,0), Vector3(0,0,0))
        vel_turn_right = Twist(Vector3(0,0,0), Vector3(0,0,1))
        vel_turn_left = Twist(Vector3(0,0,0), Vector3(0,0,-1))
        vel_stop = Twist(Vector3(0,0,0), Vector3(0,0,0))
        # velocidade = Twist(Vector3(0, 0, 0), Vector3(0, 0, 1))
        velocidade_saida.publish(vel_forw)
        rospy.sleep(2)

        if dados.data == 1:
            velocidade_saida.publish(vel_back)
            rospy.sleep(2)
            velocidade_saida.publish(vel_turn_right)
            rospy.sleep(2)
            velocidade_saida.publish(vel_stop)
            rospy.sleep(2)
            velocidade_saida.publish(vel_forw)
            rospy.sleep(2)
            velocidade_saida.publish(vel_turn_left)
            rospy.sleep(2)
        if dados.data == 2:
            velocidade_saida.publish(vel_back)
            rospy.sleep(2)
            velocidade_saida.publish(vel_turn_left)
            rospy.sleep(2)
            velocidade_saida.publish(vel_stop)
            rospy.sleep(2)
            velocidade_saida.publish(vel_forw)
            rospy.sleep(2)
            velocidade_saida.publish(vel_turn_right)
            rospy.sleep(2)
        if dados.data == 3:
            velocidade_saida.publish(vel_forw)
            rospy.sleep(2)
            velocidade_saida.publish(vel_turn_left)
            rospy.sleep(2)
            velocidade_saida.publish(vel_stop)
            rospy.sleep(2)
            velocidade_saida.publish(vel_back)
            rospy.sleep(2)
            velocidade_saida.publish(vel_turn_right)
            rospy.sleep(2)
        if dados.data == 4:
            velocidade_saida.publish(vel_forw)
            rospy.sleep(2)
            velocidade_saida.publish(vel_turn_right)
            rospy.sleep(2)
            velocidade_saida.publish(vel_stop)
            rospy.sleep(2)
            velocidade_saida.publish(vel_back)
            rospy.sleep(2)
            velocidade_saida.publish(vel_turn_left)
            rospy.sleep(2)



