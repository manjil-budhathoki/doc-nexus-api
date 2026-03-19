import cv2
import json
import os
import sys

sys.path.append(os.getcwd())
from src.services.pipeline import run_verification_pipeline

def test_system_layers(image_path):
    print(f"\n🔍 ANALYZING DOCUMENT LAYERS: {image_path}")
    
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found.")
        return

    # Run the pipeline
    result = run_verification_pipeline(img, {})

    # Print results with indentation and Nepali support
    print("\n" + "="*50)
    print("STRUCTURED EXTRACTION REPORT")
    print("="*50)
    print(json.dumps(result, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    test_system_layers("Testing/benchmarks/random.jpeg")