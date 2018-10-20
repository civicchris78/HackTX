import cv2


class Camera:

    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        cv2.namedWindow("First Person")
        self.img_counter = 0
        self.initialize()

    def isOpen(self):
        ret, frame = self.cam.read()
        cv2.imshow("First Person", frame)
        if not ret:
            return 0
        k = cv2.waitKey(1)

        if k % 256 == 27:
            print("Stopping Camera")
            return 0
        elif k % 256 == 32:
            img_name = "darknet/data/fp_img_{}.jpg".format(self.img_counter)
            cv2.imwrite(img_name, frame)
            print("{} Written".format(img_name))
            self.img_counter += 1
        return 1

    def initialize(self):
        while True:
            if not self.isOpen():
                break

    def __End(self):
        self.cam.release()
        cv2.destroyAllWindows()
