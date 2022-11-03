from CV_Robot import vision
img = vision.load_image("Examples/Samples/100samples/sample_005.png")

for item in vision.get_object_locations(img):
    print(item, item.Conf, item.BBox, item.Size)
vision.show_objects(img, pause=True)
