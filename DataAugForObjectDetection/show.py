import cv2
import os

def show_pic(img, bboxes=None):
    cv2.imwrite('./1.jpg', img)
    img = cv2.imread('./1.jpg')
    for i in range(len(bboxes)):
        bbox = bboxes[i]
        x_min = bbox[0]
        y_min = bbox[1]
        x_max = bbox[2]
        y_max = bbox[3]
        cv2.rectangle(img,(int(x_min),int(y_min)),(int(x_max),int(y_max)),(0,255,0),3)
    cv2.namedWindow('pic', 0)
    cv2.moveWindow('pic', 0, 0)
    cv2.resizeWindow('pic', 1200,800)
    cv2.imshow('pic', img)
    if cv2.waitKey(0) == 'q':
        cv2.destroyAllWindows()

if __name__ == '__main__':
    from xml_helper import *

    source_pic_root_path = '/home/hdd/Git/darknet/backup/bullet/new_aug/images'
    source_xml_root_path = '/home/hdd/Git/darknet/backup/bullet/new_aug/ano'

    for parent, _, files in os.walk(source_pic_root_path):
        for file in files:
            pic_path = os.path.join(parent, file)
            xml_path = os.path.join(source_xml_root_path, file[:-4]+'.xml')
            coords = parse_xml(xml_path)
            coords = [coord for coord in coords]

            img = cv2.imread(pic_path)
            show_pic(img, coords)
