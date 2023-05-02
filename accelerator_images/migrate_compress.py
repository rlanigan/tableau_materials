import os
import shutil
from pathlib import Path
from PIL import Image

def compress_png(input_file, output_file, n_colors=256):
    image = Image.open(input_file)
    image = image.quantize(colors=n_colors)
    image.save(output_file, "PNG", optimize=True)

def process_files_in_directory(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for root, _, files in os.walk(input_directory):
        for file in files:
            input_file_path = os.path.join(root, file)
            relative_path = os.path.relpath(root, input_directory)
            output_subfolder = os.path.join(output_directory, relative_path)
            os.makedirs(output_subfolder, exist_ok=True)
            output_file_path = os.path.join(output_subfolder, file)

            # Replace spaces with underscores in PNG file names
            if file.lower().endswith('.png'):
                file = file.replace(" ", "_")
            output_file_path = os.path.join(output_subfolder, file)

            if file.lower().endswith('.png'):
                compress_png(input_file_path, output_file_path)
                print(f"Compressed: {input_file_path} -> {output_file_path}")
            else:
                shutil.copy2(input_file_path, output_file_path)
                print(f"Copied: {input_file_path} -> {output_file_path}")


input_directory = "./original_images"
output_directory = "./compressed_images"

process_files_in_directory(input_directory, output_directory)
