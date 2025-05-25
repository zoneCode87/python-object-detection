import cv2
import pyttsx3
import threading
import queue
import time
import collections

class TextToSpeech:
    def __init__(self, rate=170, volume=1.0, speak_delay=3):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)
        self.text_queue = queue.Queue()
        self.spoken_objects = collections.deque(maxlen=50) 
        self.speak_delay = speak_delay
        self.speech_thread = threading.Thread(target=self._speech_worker, daemon=True)
        self.speech_thread.start()

    def _speech_worker(self):
        while True:
            text = self.text_queue.get()
            if text == "EXIT":
                break
            self.engine.say(text)
            self.engine.runAndWait()
            self.text_queue.task_done() 

    def speak(self, text):
        current_time = time.time()

        for t, timestamp in list(self.spoken_objects): 
            if t == text and (current_time - timestamp < self.speak_delay):
                return 
        self.spoken_objects.append((text, current_time))
        self.text_queue.put(text)

    def shutdown(self):
        self.text_queue.put("EXIT")
        self.text_queue.join()
        self.speech_thread.join()


class ObjectDetector:
    def __init__(self, config_path, weights_path, class_file, input_size=(320, 230)):
        self.net = cv2.dnn_DetectionModel(weights_path, config_path)
        self.net.setInputSize(*input_size)
        self.net.setInputScale(1.0 / 127.5)
        self.net.setInputMean((127.5, 127.5, 127.5))
        self.net.setInputSwapRB(True)

        with open(class_file, 'rt') as f:
            self.class_names = f.read().rstrip('\n').split('\n')

    def detect(self, img, conf_threshold=0.67):
        class_ids, confs, bbox = self.net.detect(img, confThreshold=conf_threshold)
        
        detected_objects_names = []
        if len(class_ids) != 0:
            for class_id, confidence, box in zip(class_ids.flatten(), confs.flatten(), bbox):
                obj_name = self.class_names[class_id - 1]
                detected_objects_names.append(obj_name)
                

                cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                cv2.putText(img, obj_name, (box[0] + 10, box[1] + 20),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), thickness=2)
        return img, detected_objects_names


def run_camera_detection():
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Cant  open cam")
        return

    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 740)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 580)


    tts_engine = TextToSpeech()

    detector = ObjectDetector(
        config_path='ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt',
        weights_path='frozen_inference_graph.pb',
        class_file='coco.names'
    )

    last_spoken_detection_time = time.time()
    speaking_interval = 2 

    while True:
        success, img = cam.read()
        if not success:
            print("Cam  not found !!")
            break


        cv2.putText(img, "object detection", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        img, detected_objects = detector.detect(img)

        current_time = time.time()
        if detected_objects and (current_time - last_spoken_detection_time > speaking_interval):

            unique_objects = list(dict.fromkeys(detected_objects)) 
            speak_message = " و ".join(unique_objects)
            print(f"{speak_message}")
            tts_engine.speak(speak_message)
            last_spoken_detection_time = current_time

        cv2.imshow('Object Detection', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
    tts_engine.shutdown() 


if __name__ == "__main__":
    run_camera_detection()