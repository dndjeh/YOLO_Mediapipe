# import cv2
# def crop(im0, xyxy):
#     cropped_img = im0[int(xyxy[1]): int(xyxy[3]), int(xyxy[0]): int(xyxy[2])]
#     cv2.namedWindow("Cropped Image", cv2.WINDOW_NORMAL)
#     cv2.imshow("Cropped Image", cropped_img)
#     cv2.waitKey(1)  # 1 millisecond


import cv2

# def crop(im0, det):
#     for i, xyxy in enumerate(det):
#         cropped_img = im0[int(xyxy[1]): int(xyxy[3]), int(xyxy[0]): int(xyxy[2])]
#         window_name = f"Cropped Image {i + 1}"
#         cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
#         cv2.imshow(window_name, cropped_img)

#     cv2.waitKey(1)  # 0 milliseconds to wait until a key is pressed
#     cv2.destroyAllWindows()  # Close all windows after a key is pressed

def crop(im0, det):
    # Initialize a dictionary to keep track of window states for each object
    window_states = {}

    for i, xyxy in enumerate(det):
        label = f"Object {i + 1}"
        window_name = f"Cropped Image {label}"

        # Check if the window for this object is already created
        if window_states.get(label) is None:
            # If not created, create a new window and update the dictionary
            cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
            window_states[label] = window_name

        # Crop the image and display in the corresponding window
        cropped_img = im0[int(xyxy[1]): int(xyxy[3]), int(xyxy[0]): int(xyxy[2])]
        cv2.imshow(window_states[label], cropped_img)

    cv2.waitKey(1)  # 1 millisecond to wait
    cv2.destroyAllWindows()  # Close all windows after a key is pressed

    #python detect.py --weight yolov5s.pt --img 416 --source 0 --device 0 --conf 0.8