import rospy
from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv import SetModelState


def insert_box():
	rospy.init_node('box_inserter', anonymous=True)

	# Create a service client to set the model state
	set_model_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)

	# Create a ModelState object to define the box's properties
	box_state = ModelState()
	box_state.model_name = 'box'  # Name of the box model in Gazebo
	box_state.pose.position.x = 0.0  # X position of the box
	box_state.pose.position.y = 0.0  # Y position of the box
	box_state.pose.position.z = 1.0  # Z position of the box (height)
	box_state.pose.orientation.x = 0.0  # X orientation of the box
	box_state.pose.orientation.y = 0.0  # Y orientation of the box
	box_state.pose.orientation.z = 0.0  # Z orientation of the box
	box_state.pose.orientation.w = 1.0  # W orientation of the box

	# Set the model state using the service client
	try:
		set_model_state(box_state)
		rospy.loginfo("Box inserted successfully!")
	except rospy.ServiceException as e:
		rospy.logerr("Failed to set model state: %s" % e)


if __name__ == '__main__':
	insert_box()
