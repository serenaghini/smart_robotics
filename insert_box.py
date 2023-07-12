import rospy
from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv import SetModelState, SpawnModel
from geometry_msgs.msg import Pose
import random

def insert_box():

	spawn_model_client = rospy.ServiceProxy('/gazebo/spawn_urdf_model', SpawnModel)
	
	model_xml = open("/home/infopz/Desktop/colored_box.urdf", 'r').read()
	
	pos = Pose()
	pos.position.x = 0.4
	pos.position.y = -0.5
	pos.position.z = 0
	pos.orientation.w = 1
	
	
	spawn_model_client(model_name="colored_box", model_xml=model_xml, robot_namespace='/foo', initial_pose=pos, reference_frame="world")


def insert_box_sdf():
	spawn_model_client = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)

	model_xml = open("boxes/box_burger.sdf", 'r').read()

	pos = Pose()
	pos.position.x = 0.4
	pos.position.y = -0.5
	pos.position.z = 0
	pos.orientation.w = 1

	spawn_model_client(model_name="box1", model_xml=model_xml, robot_namespace='/foo', initial_pose=pos,
					   reference_frame="world")


def insert_many():
	types = ["burger", "butterfly", "car", "cat", "coke", "lion", "sunflower", "tennis_ball", "tree", "umbrella"]
	n = 4
	assert n<=len(types)

	random.shuffle(types)
	types = types[:n] + types[:n]
	random.shuffle(types)
	print(types)

	spawn_model_client = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
	
	positions = []
	rows = 3

	for i in range(len(types)):
		model_xml = open("./boxes/box_"+types[i]+".sdf", 'r').read()
		#model_xml = open("stone2.sdf", 'r').read()
		pos = Pose()
		pos.position.x = 0.3 + 0.10*(i % rows)
		pos.position.y = - 0.15 * (n // rows) + (0.15 * (1 - n%2) / 2) + 0.15*(i // rows)
		pos.position.z = 0.0
		pos.orientation.w= 1
		spawn_model_client(model_name="box"+str(i), model_xml=model_xml, robot_namespace='/foo', initial_pose=pos, reference_frame="world")
		positions.append((pos.position.x, pos.position.y))

	return positions


if __name__ == '__main__':
	insert_many()

