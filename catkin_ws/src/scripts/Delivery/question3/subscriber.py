#!/usr/bin/env python

import random
import rospy
import json

from paho.mqtt import client as mqtt_client
from geometry_msgs.msg import Twist

broker = 'broker.emqx.io'
port = 1883
topic = "python/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
# username = 'emqx'
# password = 'public'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    rospy.init_node('turtle_teleop')
    turtlebot3_model = rospy.get_param("model", "burger")
    topic_type = rospy.get_param("topic_type", "turtlebot")
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    def on_message(client, userdata, msg):
        #print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        msg=msg.payload.decode()
        l=msg.split()
        l.reverse()
        #a=l.pop()
        #print(a)
        twist = Twist()
        n_msg = len(l)
        print(n_msg)
        while len(l)>1 and n_msg>10:
           l.pop()
           l.pop()
           twist.linear.x = l.pop()
           twist.linear.x = twist.linear.x.replace(",","")
           print(twist.linear.x)
           twist.linear.x = float(twist.linear.x)
           l.pop() 
           twist.linear.y = l.pop()
           twist.linear.y = twist.linear.y.replace(",","")
           twist.linear.y = float(twist.linear.y)
           l.pop()
           twist.linear.z = l.pop()
           twist.linear.z = twist.linear.z.replace(",","")
           twist.linear.z = float(twist.linear.z)
           l.pop()
           twist.angular.x = l.pop()
           twist.angular.x = twist.angular.x.replace(",","")
           twist.angular.x = float(twist.angular.x)
           l.pop()
           twist.angular.y = l.pop()
           twist.angular.y = twist.angular.y.replace(",","")
           twist.angular.y = float(twist.angular.y)
           l.pop()
           twist.angular.z = l.pop()
           twist.angular.z = twist.angular.z.replace("}","")
           twist.angular.z = float(twist.angular.z)
        pub.publish(twist)        

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    
    run()
