
from pathlib import Path

from image_detection import detect_product
from visual_search import search_product
from policy_checker import check_product_description


# Locate the project folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Product image
image_path = PROJECT_ROOT / "images" / "product.jpg"


def run_product_analysis():

    print("\n================================")
    print(" E-COMMERCE PRODUCT ANALYSIS")
    print("================================")

    if not image_path.exists():
        print(f"Image not found: {image_path}")
        return

    # STEP 1: YOLO object detection
    print("\n1. YOLO OBJECT DETECTION")

    detections = detect_product(str(image_path))

    if detections:
        for item in detections:
            print(
                f"Detected: {item['object']} | "
                f"Confidence: {item['confidence']:.2f}"
            )
    else:
        print("No objects detected.")

    # STEP 2: CLIP visual search
    print("\n2. CLIP VISUAL SEARCH")

    matches = search_product(str(image_path))

    for item in matches:
        print(
            f"{item['description']}: "
            f"{item['score']:.2%}"
        )

    # STEP 3: Policy checking
    print("\n3. PRODUCT POLICY CHECK")

    description = input(
        "\nEnter your product description: "
    )

    policy_result = check_product_description(description)

    print("\nRisk level:", policy_result["risk_level"])

    for finding in policy_result["findings"]:
        print("\nCategory:", finding["category"])
        print("Matched phrase:", finding["matched_phrase"])
        print("Recommendation:", finding["recommendation"])

    if not policy_result["findings"]:
        print("No matching demonstration rules found.")

    print("\n================================")
    print(" ANALYSIS COMPLETED")
    print("================================")


if __name__ == "__main__":
    run_product_analysis()
