from upload import upload_image
from ocr import extract_text_from_image
import sys

def main():
    # upload image from command line argument
    if len(sys.argv) < 2:
        print("Missing image path argument.")
        sys.exit(1)
    else:
        image_path = sys.argv[1]
        try:
            upload_path = upload_image(image_path)
            print(f"Image uploaded successfully to {upload_path}")
        except Exception as e:
            print(f"Error uploading image: {e}")
            sys.exit(1)
        
    # clean image (not implemented yet)
    
    # run ocr processing (not implemented yet)
    ocr_data = extract_text_from_image(image_path)
    print(ocr_data)
    


if __name__ == "__main__":
    main()

