
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")


def detect_product(image_path):

    results = model.predict(
        source=image_path,
        conf=0.25,
        save=True
    )

    detections = []

    for result in results:

        if result.boxes is None:
            continue

        for box in result.boxes:

            class_id = int(box.cls[0])
            confidence = float(box.conf[0])

            detections.append({
                "object": model.names[class_id],
                "confidence": round(confidence, 2)
            })

    return detections
