import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

# ！！！！！！！！！
# 使用说明：
#     1:参数说明：1）X_in_path:xml文件夹路径
#               2）T_out_path:输出txt文件的路径
#               3）P_out_path:输出标签对应图片的路径存入pic.txt列表（要训练的有效图片的路径）
#               3）classes：类别

X_in_path = r"C:\Users\WJY\Desktop\false_example0528\label"
T_out_path = r"C:\Users\WJY\Desktop\false_example0528\txt"
P_out_path = r"C:\Users\WJY\Desktop\false_example0528\pic"
classes = ["laji","outManagement","FlowManagement","Illegal_parking","Garbage_accumulation","Heapmaterial","Non-vehicle","sun_cure","Greening_damage","Illegal_billboards","Garbage_overflowing","Illegal_umbrella"]

def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x,y,w,h)

def convert_annotation(in_path,filename,out_path):
    in_file = open(in_path+'/%s.xml'%(filename),encoding='UTF-8')
    out_file = open(out_path+'/%s.txt' % (filename), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

def Processing(X_in_path,T_out_path,P_out_path):
    xml_files = os.listdir(X_in_path)
    list_file = open(P_out_path+'/pic.txt', 'w')
    temp = []
    pic_files = os.listdir(P_out_path)
    for pic in pic_files:
        str = pic.split('.')[0]
        temp.append(str)
    for line in xml_files:
        str1= line.split('.')[1]
        str2 = line.split('.')[0]
        if str1 != "xml":
            continue
        if str2 not in temp:
            continue
        list_file.write(P_out_path+'\\%s.jpg\n' % (str2))
        convert_annotation(X_in_path, str2,T_out_path)
    list_file.close()

Processing(X_in_path,T_out_path,P_out_path)
