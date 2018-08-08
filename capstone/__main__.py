import cv2
import tkinter
import PyQt5
import os
import SquareFaceFrames
import HeartFaceFrames
import RoundFaceFrames
import OvalFaceFrames

def init_face_analyzer():
    os.system('python3 faceanalyzerdriver.py --output $HOME/PycharmProjects/Capstone/tf_files/tmp_img')


def get_shape():
    output = os.popen('python3 ~/PycharmProjects/Capstone/capstone/label_image.py '
                      '--graph=$HOME/PycharmProjects/Capstone/tf_files/retrained/output_graph.pb '
                      '--labels=$HOME/PycharmProjects/Capstone/tf_files/retrained/output_labels.txt '
                      '--input_layer=Mul --output_layer=final_result '
                      '--image=/Users/chrisyue/PycharmProjects/Capstone/tf_files/tmp_img/face.jpg').read()
    split = output.split('\n')
    shape = split[0].split(' ')[0]

    if shape == 'square':
        SquareFaceFrames.run()
    elif shape == 'heart':
        HeartFaceFrames.run()
    elif shape == 'round':
        RoundFaceFrames.run()
    else:
        OvalFaceFrames.run()

    print("You are closest to a", shape, "face.")


if __name__ == '__main__':
    init_face_analyzer()
    get_shape()
