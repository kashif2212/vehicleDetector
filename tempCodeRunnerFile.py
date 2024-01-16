import numpy as np
import cv2

cap = cv2.VideoCapture('video.mp4')
min_width_rect = 80
min_height_rect = 80
count_line_postion = 550
# initialize Sustructor
algo = cv2.createBackgroundSubtractorMOG2()

def centre_handle(x, y, w, h):
    x1 = int(w/2)
    y1 = int(h/2)
    cx = x + x1
    cy = y + y1
    return cx, cy

detect = []
offset = 6  # Allowable error between pixels
counter = 0

while True:
    ret, frame1 = cap.read()

    gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 5)

    # applying on each frame
    img_sub = algo.apply(blur)
    dilat = cv2.dilate(img_sub, np.ones((5, 5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilatada = cv2.morphologyEx(dilat, cv2.MORPH_CLOSE, kernel)
    dilatada = cv2.morphologyEx(dilatada, cv2.MORPH_CLOSE, kernel)
    counterShape, hierarchy = cv2.findContours(dilatada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.line(frame1, (25, count_line_postion), (1200, count_line_postion), (255, 127, 0), 3)

    for (i, c) in enumerate(counterShape):
        (x, y, w, h) = cv2.boundingRect(c)
        validate_counter = (w >= min_width_rect) and (h >= min_height_rect)
        if not validate_counter:
            continue

        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)

        center = centre_handle(x, y, w, h)
        detect.append(center)
        cv2.circle(frame1, center, 4, (0, 0, 255), -1)

    for (x, y) in detect:
        if count_line_postion - offset < y < count_line_postion + offset:
            counter += 1
            print("Vehicle Counter:" + str(counter))

    detect = []  # Clear detect list after processing

    cv2.putText(frame1, "VEHICLE COUNTER : " + str(counter), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)

    cv2.imshow("videoOriginal", frame1)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
