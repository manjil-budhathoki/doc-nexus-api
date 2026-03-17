import cv2
from src.ml.bouncer import DocumentBouncer

def test_bouncer(image_path):
    # 1. Initialize Bouncer
    bouncer = DocumentBouncer()
    
    # 2. Read Image
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not load image at {image_path}")
        return

    # 3. Detect Document Type
    doc_type = bouncer.get_document_type(img)
    
    print(f"\n--- BOUNCER RESULT ---")
    print(f"Detected Document Type: {doc_type}")
    
    if doc_type:
        print("Bouncer successfully identified the document.")
    else:
        print("Bouncer could not identify the document. Check confidence/model labels.")

if __name__ == "__main__":
    # Test with a Demat image first
    test_bouncer("Testing/random.jpeg")
    test_bouncer("Testing/demat_sample.jpg")
