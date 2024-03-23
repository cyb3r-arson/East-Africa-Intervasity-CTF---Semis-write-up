from PIL import Image

def extract_lsb(image_path):
    img = Image.open(image_path)
    width, height = img.size
    flag_bits = []

    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            for channel in pixel:
                flag_bits.append(channel & 1)  # Extract LSB

    flag_bytes = [flag_bits[i:i+8] for i in range(0, len(flag_bits), 8)]
    flag_chars = [chr(int(''.join(map(str, byte)), 2)) for byte in flag_bytes]
    flag = ''.join(flag_chars)

    return flag

# Example usage
image_path = '/home/cyb3r4rs0n/Semis/myimage.png'
flag = extract_lsb(image_path)
print("Hidden Flag:", flag)
