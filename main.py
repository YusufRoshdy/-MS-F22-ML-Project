import time

import cv2
import yolov5


def get_yolov5_model(size='n'):
    model_name = f'yolov5{size}.pt'
    model = yolov5.load(model_name)
    # set model parameters
    model.conf = 0.25  # NMS confidence threshold
    model.iou = 0.45  # NMS IoU threshold
    model.agnostic = False  # NMS class-agnostic
    model.multi_label = False  # NMS multiple labels per box
    model.max_det = 3  # maximum number of detections per image

    return model


def yolov5_process(model, frame):
    results = model(frame)
    new_frame = results.render()[0]
    return new_frame


if __name__ == '__main__':
    # load pretrained model
    model = get_yolov5_model(size='l')


    cap = cv2.VideoCapture('Innopolis University.mp4')


    # Read until video is completed
    while (cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break

        old_time = time.time()
        frame = yolov5_process(model, frame)
        new_time = time.time()

        fps = 1 / (new_time - old_time)

        fps = f'FPS:{fps: 0.2f}'
        cv2.putText(frame, fps, (7, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)

        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

