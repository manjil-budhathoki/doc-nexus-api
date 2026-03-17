from abc import ABC, abstractclassmethod


class DocumentProcessor(ABC):
    """
    Abstract Base Class for all document types.
    This ensures that every processor implements the same methods.
    """

    @abstractclassmethod
    def extract_and_verify(self,image,detections,user_input):
        """
        Input: image (cv2), detections (list), user_input (dict)
        Output: Dictionary of extracted data
        """
        pass

    @abstractclassmethod
    def validate(self, extracted_data, user_input):
        """
        Input: extracted_data (dict), user_input (dict)
        Output: Dictionary containing match status and scores
        """
        pass