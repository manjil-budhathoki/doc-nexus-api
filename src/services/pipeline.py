import logging
from src.ml.bouncer import DocumentBouncer
from src.processors.registry import get_processor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bouncer = DocumentBouncer()

def run_verification_pipeline(image, user_data):
    logger.info("Pipeline started.")
    
    # 1. Route
    doc_type = bouncer.get_document_type(image)
    logger.info(f"Detected document type: {doc_type}")
    
    if not doc_type:
        logger.error("Bouncer failed to detect document type.")
        return {"error": "Document type not identified"}

    # 2. Processor
    processor = get_processor(doc_type)
    if not processor:
        logger.error(f"No processor registered for: {doc_type}")
        return {"error": "Processor not found"}
    
    # 3. Process
    try:
        extracted = processor.extract_and_verify(image, [], user_data)
        report = processor.validate(extracted, user_data)
        return {"status": "success", "data": extracted, "report": report}
    except Exception as e:
        logger.exception("Pipeline failed during extraction/validation.")
        return {"error": str(e)}