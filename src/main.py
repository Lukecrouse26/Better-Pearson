from upload import upload_image
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
        finally:
            sys.exit(0)
    
    # run ocr processing (not implemented yet)
    


if __name__ == "__main__":
    main()

