import matplotlib.pyplot as plt
import numpy as np
import cv2
import os

fig = None
ax = None

def load_model():
    """
    Loads Yolo v3 model (called automtically on import)
    """
    yolov3_path = os.path.dirname(__file__) + '/Models/Yolo v3/'
    try:
        with open(yolov3_path + 'yolov3.weights'):
            pass
    except FileNotFoundError:
        print("Downloading model...")
        import wget
        import sys
        def bar_custom(current, total, width=80):
            sys.stdout.write("\r")
            sys.stdout.write("Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total))

        wget.download('https://pjreddie.com/media/files/yolov3.weights', yolov3_path + 'yolov3.weights', bar=bar_custom)
        print()

    net = cv2.dnn.readNet(yolov3_path + "yolov3.weights", yolov3_path + "yolov3.cfg")
    with open(yolov3_path + "yolov3.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]

    output_layers = [layer_name for layer_name in net.getUnconnectedOutLayersNames()]
    return net, classes, output_layers



def detect_objects(img, net, outputLayers):
    blob = cv2.dnn.blobFromImage(img, scalefactor=0.00392, size=(320, 320), mean=(0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)
    outputs = net.forward(outputLayers)
    return blob, outputs

def get_box_dimensions(outputs, height, width, thresh=0.3):
    boxes = []
    confs = []
    class_ids = []
    for output in outputs:
        for detect in output:
            scores = detect[5:]
            class_id = np.argmax(scores)
            conf = scores[class_id]
            if conf > thresh:
                center_x = int(detect[0] * width)
                center_y = int(detect[1] * height)
                w = int(detect[2] * width)
                h = int(detect[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confs.append(float(conf))
                class_ids.append(class_id)
    return boxes, confs, class_ids

def draw_labels(boxes, confs, class_ids, classes, img, thresh=0.3, loop=False):
    global fig
    global ax
    indexes = cv2.dnn.NMSBoxes(boxes, confs, thresh, thresh)
    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = (0,0,255) #red
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label, (x, y - 5), font, 1, color, 1)


    if loop:
        if fig is None or not plt.fignum_exists(fig.number):
            fig = plt.figure(figsize=(10,10))
            ax = fig.add_subplot()
        ax.clear()
        ax.imshow(img)
        ax.axis('off')
        plt.draw()
        plt.pause(0.1)
    else:
        fig = plt.figure(figsize=(10,10))
        ax = fig.add_subplot()
        ax.imshow(img)
        ax.axis('off')
        plt.show()
