from CV_Robot import vision

img = vision.load_image("Examples/busy_street.jpg")
print(vision.find_objects(img))
vision.show_objects(img)

vision.activate_camera()
while True:
    img = vision.get_camera_image()
    print(vision.find_objects(img))
    vision.show_objects(img, local_loop=True)

