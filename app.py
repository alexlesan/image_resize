import os
from PIL import Image

resize_method = Image.ANTIALIAS
max_height = 262
max_width = 172
extensions = ['jpg', 'jpeg']

# specify the directory with images
path = "C:/uploads/users"

def adjust_size(width, height):
    if width > max_width or height > max_height:
        if width > height:
            return max_width, int (max_width * height/width)
        else:
            return int (max_height * width/height), max_height
    else:
        return width,height


if __name__ == "__main__":
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path,f)):
            f_text, f_ext = os.path.splitext(f)
            f_ext = f_ext[1:].lower()
            if f_ext in extensions:
                print(f"File: {f} treating...")
                image = Image.open(os.path.join(path,f))
                width, height = image.size
                image = image.resize(adjust_size(width, height))
                image.save(os.path.join(path, f))
                print(f"File: {f} saved.")
