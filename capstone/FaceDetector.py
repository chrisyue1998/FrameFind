import cv2
import dlib


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

OUTPUT_SIZE_WIDTH = 640
OUTPUT_SIZE_HEIGHT = 360

capture = cv2.VideoCapture(0)

cv2.namedWindow("base-image", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("result-image", cv2.WINDOW_AUTOSIZE)

cv2.moveWindow("base-image", 0, 100)
cv2.moveWindow("result-image", 400, 100)

cv2.startWindowThread()

rectangle_color = (0, 165, 255)

face_tracker = dlib.correlation_tracker()
tracking = 0

while True:
    rc, full_size_base_image = capture.read()
    base_image = cv2.resize(full_size_base_image, (320, 180))

    pressed_key = cv2.waitKey(1) & 0xFF
    if pressed_key == ord('q'):
        cv2.destroyAllWindows()
        break

    result_image = base_image.copy()

    if not tracking:
        gray_image = cv2.cvtColor(base_image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_image, 1.3, 5)

        max_area = 0
        x = 0
        y = 0
        w = 0
        h = 0

        for (_x, _y, _w, _h) in faces:
            if _w * _h > max_area:
                x = int(_x)
                y = int(_y)
                w = int(_w)
                h = int(_h)
                max_area = w * h

            if max_area > 0:
                face_tracker.start_track(base_image, dlib.rectangle(x - 10, y - 20, x + w + 10, y + h + 20))
                tracking = 1

    if tracking:
        quality = face_tracker.update(base_image)

        if quality >= 8.75:
            tracked_position = face_tracker.get_position()

            track_x = int(tracked_position.left())
            track_y = int(tracked_position.top())
            track_w = int(tracked_position.width())
            track_h = int(tracked_position.height())
            cv2.rectangle(result_image, (track_x, track_y),
                         (track_x + track_w, track_y + track_h), rectangle_color, 2)

            print(track_w)
    else:
        tracking = 0

    large_result = cv2.resize(result_image, (OUTPUT_SIZE_WIDTH, OUTPUT_SIZE_HEIGHT))
    cv2.imshow("base-image", base_image)
    cv2.imshow("result-image", large_result)



