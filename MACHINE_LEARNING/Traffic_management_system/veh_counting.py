import cv2
import glob
from vehicle_detector import VehicleDetector

# Load Veichle Detector
class vc:
    def dvc():
        vd = VehicleDetector()
        # Load images from a folder
        img_path = "./images/pexels-ashley-fontana-705774.jpg"
        # img_path = "./images/pexels-jacob-morch-457418.jpg"
        vehicles_folder_count = 0
        img = cv2.imread(img_path)
        vehicle_boxes = vd.detect_vehicles(img)
        vehicle_count = len(vehicle_boxes)
        print(vehicle_boxes)
        for box in vehicle_boxes:
            x, y, w, h = box
            cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
            cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)
        # Update total count
        cv2.imshow("Cars",img)
        cv2.waitKey(0)
        return vehicle_count