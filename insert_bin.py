import rospy
from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv import SetModelState, SpawnModel
from geometry_msgs.msg import Pose

import sys



def insert_bin():
	global types
	rospy.init_node('bin_inserter', anonymous=True)

	# Create a service client to set the model state
	#set_model_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)

	spawn_model_client = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)

	model_xml = open("bigger_bin.sdf", 'r').read()
	pos = Pose()
	pos.position.x = 0.5
	pos.position.y = 0.0
	pos.position.z = 0.0
	pos.orientation.w= 1
	spawn_model_client(model_name="bin", model_xml=model_xml, robot_namespace='/foo', initial_pose=pos, reference_frame="world")


if __name__ == '__main__':
	insert_bin()

