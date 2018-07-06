#!/usr/bin/env python  
import rospy

import tf
from sensor_msgs.msg import JointState
from std_msgs.msg import String

names = [ 'leg_left_1_joint', 'leg_left_2_joint', 'leg_left_3_joint', 'leg_left_4_joint', 'leg_left_5_joint', 'leg_left_6_joint', 'leg_right_1_joint', 'leg_right_2_joint', 'leg_right_3_joint', 'leg_right_4_joint', 'leg_right_5_joint', 'leg_right_6_joint', 'torso_1_joint', 'torso_2_joint', 'arm_left_1_joint', 'arm_left_2_joint', 'arm_left_3_joint', 'arm_left_4_joint', 'arm_left_5_joint', 'arm_left_6_joint', 'arm_left_7_joint', 'gripper_left_inner_double_joint', 'gripper_left_fingertip_1_joint', 'gripper_left_fingertip_2_joint', 'gripper_left_inner_single_joint', 'gripper_left_fingertip_3_joint', 'gripper_left_joint', 'gripper_left_motor_single_joint', 'arm_right_1_joint', 'arm_right_2_joint', 'arm_right_3_joint', 'arm_right_4_joint', 'arm_right_5_joint', 'arm_right_6_joint', 'arm_right_7_joint', 'gripper_right_inner_double_joint', 'gripper_right_fingertip_1_joint', 'gripper_right_fingertip_2_joint', 'gripper_right_inner_single_joint', 'gripper_right_fingertip_3_joint', 'gripper_right_joint', 'gripper_right_motor_single_joint', 'head_1_joint', 'head_2_joint',] 
positions = [ 0.0, 0.0, -0.411354, 0.859395, -0.448041, -0.001708, # leg_left \
        0.0, 0.0, -0.411354, 0.859395, -0.448041, -0.001708, # leg_right \
        0, 0.006761, # torso \
        0.25847, 0.173046, -0.0002, -0.525366, 0, 0, 0.1, # arm_left \
        0, 0, 0, 0, 0, 0, 0, # gripper_left \
        -0.25847, -0.173046, 0.0002, -0.525366, 0, 0, 0.1, # arm_right \
        0, 0, 0, 0, 0, 0, 0, # gripper_right \
        0, 0, # head \
        ]

robot_link = (
        (0,0,1.0192720229567027),
        (0,0,0,1),
        "base_link"
        )
object_link = (
        (0.45,0,1.4),
        (-0.5,-0.5, 0.5, 0.5),
        "mire"
        )


if __name__ == '__main__':
    rospy.init_node('tf_test')
    rate = rospy.Rate(10)

    # pub = rospy.Publisher ("/motion_planning/param/init_position_mode", String, queue_size=1)
    # pub.publish ("estimated")

    js_pub = rospy.Publisher ("/joint_states", JointState, queue_size=2)
    br = tf.TransformBroadcaster()

    while not rospy.is_shutdown():
        now = rospy.Time.now()
        js_pub.publish (JointState (name=names, position=positions))
        br.sendTransform (
                robot_link[0],
                robot_link[1],
                now,
                robot_link[2],
                "world")
        br.sendTransform (
                object_link[0],
                object_link[1],
                now,
                object_link[2],
                "world")
        rate.sleep()
