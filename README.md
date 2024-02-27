# yolov5와 mediapipe를 활용함.
# anaconda prompt에서 .\YOLO\content\yolov5로 이동 후 detect3.py를 webcam으로 실행하면 됨 -> python detect3.py --weight yolov5s.pt --img 416 --source 0 --device 0 --conf 0.8
# detect3.py에서 272-307라인이 연구 했던 코드(주석 참고), 174라인은 특정 class번호만 추출 하는 것, class 번호는 .\YOLO\content\yolov5\data\coco.yaml를 참고하기
# Media.py가 crop한 window창에 미디어 파이프를 적용하는 모듈
# detect3_1.py는 switch현상을 해결하려고 작성중. (.\YOLO\content\yolov5\sortdir\sort.py) 활용중,,
# detect3.py 실행