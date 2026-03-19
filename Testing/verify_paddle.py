import os
import logging
from paddleocr import PaddleOCR

# Disable the Intel MKL crash log
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

print("--- Testing PaddleOCR Import ---")
try:
    # Minimal init to check for module errors
    ocr = PaddleOCR(lang='en', use_gpu=False, show_log=False)
    print("✅ English Engine: LOADED")
    
    # Check Devanagari (The one you need for Citizenship)
    ocr_dv = PaddleOCR(lang='devanagari', use_gpu=False, show_log=False)
    print("✅ Devanagari Engine: LOADED")
    
    print("\nSUCCESS: Your OCR environment is perfectly configured.")
except Exception as e:
    print(f"❌ ERROR: {e}")