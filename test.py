# import numpy as np
# import cv2


# # minimum dimensons to filter detected objects
# min_height_rect = 80
# min_width_rect = 80

# cap = cv2.VideoCapture("video.mp4")
# algo = cv2.createBackgroundSubtractorMOG2()
# count_line_postion = 550
# detect = []

#  # Allowable error
# offset = 6

# # Counts the number of vehicle passing the line
# counter=0

# def centre_handle(x,y,w,h):
#     x1 = int(w/2)
#     y1 = int(h/2)

#     # centreX cordinate
#     cx = x+x1
#     # centreY cordinate
#     cy = y+y1
#     return cx, cy 
    

   



# while True:

#     ret,frame1 = cap.read()

#     #coverting the input to gray colour
#     gray = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)

#     # Apply a Gaussian blur to reduce noise
#     blur = cv2.GaussianBlur(gray,(3,3),5)

#     # Use the background subtractor to obtain a binary image highlighting moving objects
#     img_sub = algo.apply(blur)

#     # Dilate the binary image(img_sub) to enhance object boundaries 
#     dilat = cv2.dilate(img_sub,np.ones((5,5)))

#     # Create a kernel for morphological operations.
#     kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))

#     # Apply morphological closing to further enhance object shapes (dilatada).
#     dilatdata = cv2.morphologyEx(dilat,cv2.MORPH_CLOSE,kernel)
#     dilatdata = cv2.morphologyEx(dilatdata,cv2.MORPH_CLOSE,kernel)

#     counterShape,h = cv2.findContours(dilatdata,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#     cv2.line(frame1,(25,count_line_postion),(1200,count_line_postion),(0,0,255),3)

#     # enumerate(counterShape) is used to iterate over the contours along with their indices (i). The variable c represents a contour.
#     for(i,c) in enumerate(counterShape):

#         # cv2.boundingRect(c) computes the bounding rectangle for the contour c. It returns the (x, y) coordinates of the top-left corner of the rectangle and its width (w) and height (h).
#         (x,y,w,h) = cv2.boundingRect(c)
#         validate_counter = (w>=min_width_rect) and (h>=min_height_rect)
#         if not validate_counter:
#             continue

#         # cv2.rectangle is used to draw a green rectangle around the detected vehicle on the original frame (frame1). The rectangle is defined by its top-left and bottom-right corners.
#         cv2.rectangle(frame1,(x,y),(x+w , y+h),(0,255,0),2)
#         center = centre_handle(x,y,w,h)
#         detect.append(center)

#         cv2.circle(frame1,center,4,(0,0,255),-1)

#     for(x,y) in detect:
#         if count_line_postion - offset < y < count_line_postion- offset:
#             counter +=1
#             print("Vehicle Counter:"+str(counter))
#     detect = []

#     cv2.putText(frame1,"VEHICLE COUNTER:"+str(counter), (450,70), cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255), 5)

#     if cv2.waitKey(1) == ord('q'):
#         break
#     cv2.imshow("videoOriginal", frame1)

# cap.release()
# cv2.destroyAllWindows()







