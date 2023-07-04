import rospy
from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv import SetModelState, SpawnModel
from geometry_msgs.msg import Pose

import sys
import random

types = ["burger", "butterfly", "cat"]


def insert_box():
	global types
	rospy.init_node('box_inserter', anonymous=True)

	# Create a service client to set the model state
	#set_model_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)

	spawn_model_client = rospy.ServiceProxy('/gazebo/spawn_urdf_model', SpawnModel)
	types = types + types
	random.shuffle(types)

	for i in range(len(types)):
		model_xml = open("./boxes/box_"+types[i]+".urdf", 'r').read()
		pos = Pose()
		pos.position.x = 0.1 + 0.2*(i%2)
		pos.position.y = 0.1 + 0.2*(i//2)
		pos.position.z = 0.0
		pos.orientation.w= 1
		spawn_model_client(model_name="box"+str(i), model_xml=model_xml, robot_namespace='/foo', initial_pose=pos, reference_frame="world")


if __name__ == '__main__':
	insert_box()

