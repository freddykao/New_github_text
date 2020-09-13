import xml.etree.ElementTree as ET
import os
from os import getcwd

sets=[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]

classes = ["kangaroo", "raccoon"]


def convert_annotation(file_name, list_file):
    in_file = open(label_path + '/' + file_name)
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = getcwd()


list_file = open('train.txt', 'w')
train_path = input('Train Files Path:')
label_path = input('Label Files Path:')

total_files_counts = len(os.listdir(train_path))

for file_name in os.listdir(label_path):
    list_file.write(train_path + '/' + file_name[:-4] + '.jpg')
    convert_annotation(file_name, list_file)
    list_file.write('\n')
list_file.close()