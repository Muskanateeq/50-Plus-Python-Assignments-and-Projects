import qrcode
import cv2

def generate_qr(data, filename="qrcode.png"):
    """Generates a QR code and saves it as an image."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"QR code saved as {filename}")

def decode_qr(image_path):
    """Decodes a QR code from an image file."""
    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(img)
    
    if data:
        print(f"Decoded QR Code data: {data}")
    else:
        print("No QR Code detected!")

# Main Program
if __name__ == "__main__":
    choice = input("Enter '1' to generate QR code, '2' to decode a QR code: ")

    if choice == "1":
        text = input("Enter the text/URL to encode: ")
        generate_qr(text)
    elif choice == "2":
        image_path = input("Enter the path of the QR code image: ")
        decode_qr(image_path)
    else:
        print("Invalid choice. Please enter '1' or '2'.")
