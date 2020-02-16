import sys
from face_tracking import Face_tracking

if __name__ == '__main__':
    path = sys.argv[1]
    fc = Face_tracking(path) 
    fc.face_tracker()