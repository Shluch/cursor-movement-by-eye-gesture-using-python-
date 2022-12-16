import mediapipe #to detect face
import cv2 #cv2 have camera driver to open and work with system cammera
import mediapipe as mp
import pyautogui


cam = cv2.VideoCapture(0) #0 = default cammera
face_mesh=mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)  #face hai ye
screen_w, screen_h = pyautogui.size()
while True: #(to read every fps from cam
    _, frame = cam.read()
    frame = cv2.flip(frame, 1) #1= vertical
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #converting color for eye
    output = face_mesh.process(rgb_frame)
    points = output.multi_face_landmarks
   # print(points)
    frame_h,frame_w,_= frame.shape #to get height and weidth
    if points:
        landmarks = points[0].landmark #point [0] == one face
        for id,landmarks in enumerate(landmarks[474:478]): #range is for eyes
            x =int(landmarks.x * frame_w)
            y = int(landmarks.y * frame_h)
            cv2.circle(frame,(x,y),3,(0,255,0)) #drawing circle on frame (0->red)
           # print(x,y)
            if id == 1:
                screen_x = int(landmarks.x*screen_w)
                screen_y = int(landmarks.y*screen_h)
                pyautogui.moveTo(screen_x, screen_y)
        #left = [landmarks[145],landmarks[159]]
        #for id ,landmarks in enumerate(landmarks[145:159]):
            #x = int(landmarks.x * frame_w)
           # y = int(landmarks.y * frame_h)
            #cv2.circle(frame, (x, y), 2, (0, 255, 255))

    cv2.imshow('Looking Good', frame) #output dega
    cv2.waitKey(2) #kitna wait karega after start