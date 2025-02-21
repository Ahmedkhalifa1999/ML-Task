from deepface import DeepFace
import sys

class UnknownFaceDetector:
    def __init__(self):
        pass

    def detect(self, input_img: str, output_img: str):
        """
        Detects all faces in the input image and labels known faces with their names and a blue box around their faces.
        Unknown faces are labeled as "Unknown" and a red box is drawn around their faces.
        :param input_img: The input image path
        :param output_img: The output image path
        :return: None

        Example:
        >>> detector = UnknownFaceDetector()
        >>> detector.detect("input.jpg", "output.jpg")
        """
        detected_faces = DeepFace.find(img_path=input_img, 
                                       db_path='./data/lfw/lfw-deepfunneled',
                                       model_name='Facenet512',
                                       detector_backend='retinaface',
                                       align=True)
        print(detected_faces)


if __name__ == "__main__":
    detector = UnknownFaceDetector()
    if len(sys.argv) > 1:
        input_image_path = sys.argv[1]
    else:
        raise ValueError("Please provide the input image path")
    
    detector.detect(input_image_path, "output.jpg")