import rospy
import cv2
import os

from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class camera:

  def __init__(self):
    self.image_sub = rospy.Subscriber("/camera/image_raw", Image, self.callback)
     
  def callback(self,data):

    rospy.loginfo(data.header)
  
    try:
      cv_image = bridge.imgmsg_to_cv2(data, desired_encoding="bgr8")
    except CvBridgeError as e:
      rospy.logerr(e)

    global image
    
    image = cv_image 

    cv2.imshow("Camera output", image)
    cv2.imwrite("/home/infopz/catkin_ws/saved/img.png", image)

    cv2.waitKey(3)

def read_camera():
	
    camera()

    while not rospy.is_shutdown():
      rospy.spin()
	
      #try:
	#rospy.spin()
      #except KeyboardInterrupt:
	#rospy.loginfo("Shutting down")

    #cv2.imwrite("image.jpg", image)
	
    cv2.destroyAllWindows()

if __name__ == '__main__':
    rospy.init_node('camera_reader', anonymous=True)
    bridge = CvBridge()
    read_camera()
