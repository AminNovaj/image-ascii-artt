from PIL import Image

# Convert an image to ASCII
def image_to_ascii(image_path, width=100):
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        return "Error: Image file not found. Please check the path."
    except Exception as e:
        return f"Error: Could not open image.  Reason: {e}"

    # Resize image to fit terminal
    aspect_ratio = img.height / img.width
    height = int(aspect_ratio * width)
    img = img.resize((width, height))
    
    # Convert image to grayscale
    img = img.convert("L")
    
    # Define ASCII characters to map the pixels
    pixels = img.getdata()
    ascii_str = ""
    for pixel in pixels:
        if pixel < 85:
            ascii_str += "#"
        elif pixel < 170:
            ascii_str += "*"
        else:
            ascii_str += " "
    
    ascii_str = ascii_str[:width * height]  # Limit to correct size
    return "\n".join([ascii_str[i:i+width] for i in range(0, len(ascii_str), width)])

# Get image path from user input
image_path = input("Enter the path to your image: ")

ascii_art = image_to_ascii(image_path)
print(ascii_art)