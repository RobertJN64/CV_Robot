import CV_Robot.opencv_api as cv_api
import cv2

#https://github.com/nandinib1999/object-detection-yolo-opencv

net, classes, output_layers = cv_api.load_model()
camera = cv2.VideoCapture()
camera_active = False
is_video = False

class Objects:
    STOP_SIGN = 'STOP_SIGN'
    BIKE = 'BIKE'
    CAR = 'CAR'
    TRAFFIC_LIGHT = "TRAFFIC_LIGHT"
    FIRE_HYDRANT = "FIRE_HYDRANT"
    PERSON = "PERSON"

def activate_camera():
    """
    Activates the robot camera
    """
    global camera
    global camera_active
    global is_video
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    camera_active = True
    is_video = False

def get_camera_image(skip_frames = 5):
    """
    Retrieves current image from robot camera or video
    Returns none if the video is done or camera failed
    :param skip_frames: If playing a video, skip ahead this many frames at a time
    """
    global camera
    global camera_active
    if not camera_active:
        raise Exception("Camera is not active. Call vision.activate_camera() or vision.load_video()")
    if is_video:
        for i in range(0, skip_frames):
            camera.read()
    _, img = camera.read()
    return img


def load_image(img_path):
    """
    Loads an image file
    :param img_path: File path to image
    """
    # image loading
    with open(img_path):
        pass #Make sure image exists
    img = cv2.imread(img_path)
    img = cv2.resize(img, None, fx=0.4, fy=0.4)
    return img

def load_video(video_path):
    """
    Loads a video file to emulate camera
    :param video_path: File path to video
    """
    global camera
    global camera_active
    global is_video
    with open(video_path):
        pass #Make sure video exists
    camera = cv2.VideoCapture(video_path)
    camera_active = True
    is_video = True

def _map_objects(objs):
    d = {"stop sign": Objects.STOP_SIGN,
         "bicycle": Objects.BIKE,
         "car": Objects.CAR,
         "traffic light": Objects.TRAFFIC_LIGHT,
         "fire hydrant": Objects.FIRE_HYDRANT,
         "person": Objects.PERSON}
    return [d[obj] for obj in objs if obj in d]

def _get_objects(image, thresh=0.3):
    height, width, channels = image.shape
    blob, outputs = cv_api.detect_objects(image, net, output_layers)
    boxes, confs, class_ids = cv_api.get_box_dimensions(outputs, height, width, thresh=thresh)
    return boxes, confs, class_ids

def show_objects(image, thresh=0.3, local_loop=False):
    """
    Displays image with boxes around objects, if block=True, waits for escape to be pressed before closing image
    :param image: Image object (from load_image)
    :param thresh: Threshold to identify object, default is 30% (0.3)
    :param local_loop: Set to true if running in loop outside of colab
    """
    boxes, confs, class_ids = _get_objects(image)
    cv_api.draw_labels(boxes, confs, class_ids, classes, image, thresh=thresh, loop=local_loop)

def find_objects(image, thresh=0.3):
    """
    Runs machine learning model on image specified, returns list of identified objects
    :param image: Image object (from load_image)
    :param thresh: Threshold to identify object, default is 30% (0.3)
    """
    _, _, class_ids = _get_objects(image, thresh=thresh)
    return list(set(_map_objects([classes[x] for x in class_ids])))

