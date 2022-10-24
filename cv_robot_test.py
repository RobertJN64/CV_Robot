from CV_Robot import robot
from CV_Robot import vision

vision.activate_camera()
robot.forward()
while True:
    img = vision.get_camera_image()
    vision.show_objects(img, local_loop=True)
    if vision.Objects.STOP_SIGN in vision.find_objects(img):
        break
robot.stop()


import os
for item in os.listdir('Examples/db_lisa_tiny'):
    print(item)
    img = vision.load_image("Examples/db_lisa_tiny/" + item)
    print(vision.find_objects(img))
    vision.show_objects(img)

img = vision.load_image("Examples/busy_street.jpg")
print(vision.find_objects(img))
vision.show_objects(img)
#
# vision.activate_camera()
vision.load_video("Examples/pedestrians.mp4")
while True:
    img = vision.get_camera_image()
    if img is None:
        break
    print(vision.find_objects(img))
    vision.show_objects(img, local_loop=True)


