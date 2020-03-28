import json
import os
import sys
import time
import math
import cv2
import numpy as np
print(sys.path)
sys.path.append('/root/openpose/build/python')

from openpose import pyopenpose as op

if __name__ == '__main__':
    params = dict()
    params["model_folder"] = "/root/openpose/models/"
    params["hand"] = True
    params["hand_detector"] = 3
    params["hand_scale_number"] = 6
    params["hand_render_threshold"] = 0.2
    params["hand_render"] = -1

    params["write_json"] = "/output/"
    params["model_pose"] = "BODY_25"
    # Paths - should be the folder where Open Pose JSON output was stored
    filepath = "/output/"
    # Starting OpenPose
    opWrapper = op.WrapperPython()
    opWrapper.configure(params)
    opWrapper.start()
    # Process Image
    datum = op.Datum()
    keypointdict={}
    outerdict={}
    keypointlist = []
    #Clean the output folder
    for filename in os.listdir(filepath):
        if filename.endswith(".json"):
            os.remove(os.path.join(filepath,filename))

    #Video capture from webcam
    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    fps = cap.get(cv2.CAP_PROP_FPS)
    print("The current fps is " ,fps)
    name= 1 #name of the json file
    if (cap.isOpened()== False):
        print("Error opening video stream or file")
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            # Display the resulting frame
            #cv2.imshow('Frame',frame)
            datum.cvInputData = frame
            opWrapper.emplaceAndPop([datum])
            writepath = os.path.join(filepath,"keypoint_{:08d}.json".format(name))
            mode = 'w' if os.path.exists(writepath) else 'w+'
            # Display Image
            outerdict["people"]=keypointlist
            keypointdict['pose_keypoints_2d'] = datum.poseKeypoints.flatten().tolist()
            keypointdict['hand_left_keypoints_2d'] = datum.handKeypoints[0].flatten().tolist()
            keypointdict['hand_right_keypoints_2d'] = datum.handKeypoints[1].flatten().tolist()
            keypointlist.append(keypointdict.copy())#must be the copy!!!
            cv2.imshow("OpenPose 1.5.0 - Tutorial Python API", datum.cvOutputData)
            #print("pose_keypoints_2d " ,datum.poseKeypoints.flatten().tolist())
			# Custom Params (refer to include/openpose/flags.hpp for more parameters)
            #print("hand_left_keypoints_2d " ,str(datum.handKeypoints[0]))
            with open(writepath, mode) as f :
                json.dump(outerdict, f, indent=0 )
            
            outerdict.clear()
            keypointlist.clear()
            keypointdict.clear()
            print("keypointdict " ,keypointdict)
            name = name + 1
            cv2.waitKey(1)
                    
            # Press Q on keyboard to  exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        # Break the loop
        else:
             break
    # When everything done, release the video capture object
    cap.release()
    # Closes all the frames
    cv2.destroyAllWindows()










