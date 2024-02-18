import cv2
import numpy as np
import os

def hex_to_rgb(hex_code):
    # Remove '#'
    if hex_code.startswith('#'):
        hex_code = hex_code[1:]
    # hex to RGB
    r = int(hex_code[0:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)
    return (r, g, b)

def create_image():
    # size
    print('')
    print("Choose the image size ratio:")
    print("1) 1:1")
    print("2) 4:3")
    print("3) 16:9")
    size_choice = input("Enter your choice (1/2/3): ")

    if size_choice == '1':
        size = (400, 400)
    elif size_choice == '2':
        size = (800, 600)
    elif size_choice == '3':
        size = (1600, 900)
    else:
        print("Invalid choice. Using default size (400x400).")
        size = (400, 400)

    # bg color
    print('')
    print("Choose a background color:")
    print("1) Red")
    print("2) Green")
    print("3) Blue")
    print("4) Yellow")
    print("5) Black")
    print("6) Enter custom HEX color")
    color_choice = input("Enter your choice (1/2/3/4/5/6): ")

    if color_choice == '1':
        background_color = (0, 0, 255)  # Red
    elif color_choice == '2':
        background_color = (0, 255, 0)  # Green
    elif color_choice == '3':
        background_color = (255, 0, 0)  # Blue
    elif color_choice == '4':
        background_color = (0, 255, 255)  # Yellow
    elif color_choice == '5':
        background_color = (0, 0, 0)  # Black
    elif color_choice == '6':
        background_color = hex_to_rgb(input("Enter HEX color code (e.g., #RRGGBB): "))
    else:
        print("Invalid choice. Using default color (white).")
        background_color = (255, 255, 255)  # White

    # text
    print('')
    text = input("Enter the text you want on the image: ")

    #text color
    print('')
    print("Choose a text color:")
    print("1) White")
    print("2) Black")
    print("3) Red")
    print("4) Green")
    print("5) Blue")
    print("6) Enter custom HEX color")
    text_color_choice = input("Enter your choice (1/2/3/4/5/6): ")

    if text_color_choice == '1':
        text_color = (255, 255, 255)  # White
    elif text_color_choice == '2':
        text_color = (0, 0, 0)  # Black
    elif text_color_choice == '3':
        text_color = (0, 0, 255)  # Red
    elif text_color_choice == '4':
        text_color = (0, 255, 0)  # Green
    elif text_color_choice == '5':
        text_color = (255, 0, 0)  # Blue
    elif text_color_choice == '6':
        text_color = hex_to_rgb(input("Enter HEX color code (e.g., #RRGGBB): "))
    else:
        print("Invalid choice. Using default color (black).")
        text_color = (0, 0, 0)  # Black

    # text size
    print('')
    text_size = int(input("Enter the text size (integer value): "))

    # blank image
    image = np.ones((size[1], size[0], 3), np.uint8)
    image[:, :] = background_color

    # Add text
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_width, text_height = cv2.getTextSize(text, font, text_size, 2)[0]
    text_x = (image.shape[1] - text_width) // 2
    text_y = (image.shape[0] + text_height) // 2
    cv2.putText(image, text, (text_x, text_y), font, text_size, text_color, 2)

    # Create a directory named "images" if it doesn't exist
    if not os.path.exists("images"):
        os.makedirs("images")

    # image name
    print('')
    image_name = input("Enter the name for your image (without extension): ")

    # Save 
    cv2.imwrite(f"images/{image_name}.png", image)
    print('')
    print('')
    print(f"Your image has been saved as images/{image_name}.png")

if __name__ == "__main__":
    print("==========================")
    print("  Simple Thumb - CHXRITH  ")
    print("==========================")
    create_image()
