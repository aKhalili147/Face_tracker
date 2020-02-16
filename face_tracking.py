import cv2

class Face_tracking:

    def __init__(self,path):
        self.path = path 

    def face_tracker(self):
        face_cascade = cv2.CascadeClassifier(self.path)

        video_capture = cv2.VideoCapture(0)
        video_capture.set(1, 640) # set video widht
        video_capture.set(2, 480) # set video height

        # window size for face
        width = 0.1*video_capture.get(1)
        height = 0.1*video_capture.get(2)

        while True:
            # Capture frame-by-frame (next frame)
            ret, frame = video_capture.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            face = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(int(width), int(height)),
                flags=cv2.CASCADE_SCALE_IMAGE
            )

            # rectangle drawn around the face
            for (x, y, w, h) in face:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 0), 2)

            # Display the frame
            cv2.imshow('Video', frame)

            # press 'q' to quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()