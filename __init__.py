from PIL import Image
def image_to_tupper_constant(path):
    # Step 1: Load and convert image
    img = Image.open(path).convert("1")
    img = img.resize((106, 17))
    bits = []
    for x in range(105, -1, -1):
        for y in range(0, 17):
            pixel = img.getpixel((x, 16 - y))
            bits.append('1' if pixel == 0 else '0')
    binary_string = ''.join(bits)
    integer_value = int(binary_string, 2)
    tupper_constant = integer_value * 17
    return tupper_constant
if __name__ == "__main__":
    path = input("Where is the image stored: ")
    k = image_to_tupper_constant(path)
    print("Your Tupper constant:")
    print(k)
