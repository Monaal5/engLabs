import os
from PIL import Image

image_path = r"C:\Users\DR.RAJESH KUMAR\.gemini\antigravity-ide\brain\853c1742-ed81-447e-a67e-2bc697fee19a\media__1781086569695.jpg"
output_dir = r"d:\Kimi_Agent_3D打印平台\app\public\images"

print("Checking image...")
if os.path.exists(image_path):
    print("Found image at", image_path)
    img = Image.open(image_path)
    print("Size:", img.size)
    print("Mode:", img.mode)
else:
    print("Error: Image not found")
