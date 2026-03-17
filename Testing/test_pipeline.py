import cv2
import json
from src.services.pipeline import run_verification_pipeline

def test_pipeline():
    # 1. Load image
    image_path = "Source/demat_sample.jpg"
    img = cv2.imread(image_path)
    
    # 2. Mock User Input (What the user claims)
    user_input = {
        "name": "SAGAR SEDAI", 
        "boid": "1301520000305819"
    }
    
    # 3. Run Pipeline
    print("Running Verification Pipeline...")
    result = run_verification_pipeline(img, user_input)
    
    # 4. Print Result
    print("\n--- FINAL JSON REPORT ---")
    print(json.dumps(result, indent=4))

if __name__ == "__main__":
    test_pipeline()