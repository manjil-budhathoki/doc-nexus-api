import cv2
import json
import os
import logging
from src.services.pipeline import run_verification_pipeline

# Setup basic logging to see the "Bridge" in action
logging.basicConfig(level=logging.INFO)

def run_full_test(image_path, doc_label, user_data):
    print(f"\n{'='*20} TESTING {doc_label.upper()} {'='*20}")
    
    if not os.path.exists(image_path):
        print(f"Error: Image {image_path} not found.")
        return

    # 1. Load Image
    img = cv2.imread(image_path)
    
    # 2. Run the Pipeline
    # (Bouncer -> Registry -> Specialist -> OCR -> Matcher)
    result = run_verification_pipeline(img, user_data)
    
    # 3. Output result
    # Change the print line in Testing/test_system.py to:
    print(json.dumps(result, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    # --- TEST 1: DEMAT ---
    demat_data = {
        "name": "SAGAR SEDAI", 
        "boid": "1301520000305819"
    }
    run_full_test("Source/demat_sample.jpg", "demat", demat_data)

    # --- TEST 2: CITIZENSHIP ---
    # Put a citizenship image in your Testing folder named 'citi_sample.jpg'
    citizenship_data = {
        "name": "YOUR NAME", 
        "id_number": "12345", 
        "dob": "2000-01-01"
    }
    run_full_test("Source/random.jpeg", "citizenship", citizenship_data)