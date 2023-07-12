import rospy
from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv import SetModelState, SpawnModel
from geometry_msgs.msg import Pose

import sys
import random

def insert_camera():
	rospy.init_node('camera_inserter', anonymous=True)

	# Create a service client to set the model state
	#set_model_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)

	spawn_model_client = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
        
	model_xml = open("camera_model.sdf", 'r').read()
	pos = Pose()
	#+0.25
	pos.position.x = 0.4
	pos.position.y = 0
	#+1.25
	pos.position.z = 1
	#conversione ZYX
	pos.orientation.w= 0.5353686
	spawn_model_client(model_name="camera", model_xml=model_xml, initial_pose=pos, reference_frame="world")


if __name__ == '__main__':
	insert_camera()

