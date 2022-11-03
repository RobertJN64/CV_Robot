from CV_Robot import robot
from CV_Robot import vision

vision.activate_camera()
robot.forward()
while True:
    img = vision.get_camera_image()
    vision.show_objects(img)
    if vision.Objects.PERSON not in vision.find_objects(img):
        break
robot.stop()


import os
for item in os.listdir('Examples/Samples/100samples'):
    print(item)
    img = vision.load_image("Examples/Samples/100samples/" + item)
    print(vision.find_objects(img))
    vision.show_objects(img)

img = vision.load_image("Examples/Samples/busy_street.jpg")
print(vision.find_objects(img))
vision.show_objects(img, pause=True)
#
# vision.activate_camera()
vision.load_video("Examples/Samples/pedestrians.mp4")
while True:
    img = vision.get_camera_image()
    if img is None:
        break
    print(vision.find_objects(img))
    vision.show_objects(img)


