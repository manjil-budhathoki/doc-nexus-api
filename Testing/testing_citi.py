import cv2
import json
import os
import sys

sys.path.append(os.getcwd())
from src.services.pipeline import run_verification_pipeline

def run_single_detection_test(image_path):
    print(f"\n🚀 STARTING DETECTION TEST ON: {image_path}")
    
    img = cv2.imread(image_path)
    if img is None:
        print(f"❌ Error: Could not find image at {image_path}")
        return

    result = run_verification_pipeline(img, {})

    # DEBUG: See what keys we actually got
    # print(f"DEBUG: Result keys received: {list(result.keys())}")

    if "extraction" in result:
        data = result["extraction"]
        
        print("\n--- DETECTION JSON ---")
        # Print everything except the raw image array
        json_output = {k: v for k, v in data.items() if k != "visual_result"}
        print(json.dumps(json_output, indent=4))

        if "visual_result" in data:
            output_name = "Testing/detection_layers_result.jpg"
            cv2.imwrite(output_name, data["visual_result"])
            print(f"\n✅ Visual Result saved to: {output_name}")
    else:
        # If 'extraction' is missing, show the error or the whole result
        error_msg = result.get('error', 'Unknown Error (Check pipeline.py keys)')
        print(f"❌ Pipeline Failed: {error_msg}")

if __name__ == "__main__":
    # The data we expect to find on the card
    user_input = {
        "name": "Manjil Budhathoki",
        "citizenship_no": "05-02-78-02811", # Based on your screenshot
        "dob": "2056-10-15"
    }
    
    # Run the test
    run_single_detection_test("Testing/benchmarks/random.jpeg", user_input)