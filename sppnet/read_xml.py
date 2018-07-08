import cv2
import numpy as np
import glob
from xml.etree.ElementTree import parse,dump
def read_image(path="D:\PASCAL\VOCdevkit\VOC2012\JPEGImages\*.jpg"):
    image_data=[]
    for i in glob.glob(path):# load image data
        n=cv2.imread(i,cv2.IMREAD_COLOR)
        n=cv2.cvtColor(n, cv2.COLOR_BGR2RGB)# matplotlib = RGB channel , opencv = BGR channels
        image_data.append(n)
    return image_data
def read_xml(path="D:\PASCAL\VOCdevkit\VOC2012\Annotations\*.xml"):
    xml_data=[]
    for i in glob.glob(path):# load image data
        tree = parse(i)
        xml_data.append(tree)
    return xml_data