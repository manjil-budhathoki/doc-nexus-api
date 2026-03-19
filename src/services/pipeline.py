import logging
from src.ml.doc_router import DocumentBouncer
from src.processors.registry import get_processor

logger = logging.getLogger(__name__)
bouncer = DocumentBouncer()

def run_verification_pipeline(image, user_data):
    logger.info("Pipeline started.")
    
    doc_type = bouncer.get_document_type(image)
    logger.info(f"Detected document type: {doc_type}")
    
    if not doc_type:
        return {"error": "Document type not identified"}

    processor = get_processor(doc_type)
    if not processor:
        return {"error": f"Processor for {doc_type} not found"}
    
    try:
        # We use 'extraction' as the key name
        extracted = processor.extract_and_verify(image, [], user_data)
        report = processor.validate(extracted, user_data)
        
        return {
            "status": "success",
            "document_type": doc_type,
            "extraction": extracted,  # <--- CRITICAL KEY NAME
            "verification": report
        }
    except Exception as e:
        logger.exception("Pipeline failed:")
        return {"error": str(e)}