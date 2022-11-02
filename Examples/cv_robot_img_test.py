from CV_Robot import vision
img = vision.load_image("Samples/busy_street.jpg")

vision.show_image(img)
print(vision.get_object_locations(img))
print(vision.find_objects(img))
vision.show_objects(img)
