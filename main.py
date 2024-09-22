from PIL import Image
import os

def convert_images_to_pdf(image_paths, output_pdf_path):
    images = []
    for image_path in image_paths:
        img = Image.open(image_path)
        img = img.convert('RGB')  # Convert to RGB if not already
        images.append(img)

    if images:
        # Save as PDF
        images[0].save(output_pdf_path, save_all=True, append_images=images[1:])
        print(f"PDF saved as {output_pdf_path}")
    else:
        print("No images to convert.")

def sort_images(image_files):
    # Sort images based on filename
    return sorted(image_files)

# Example usage
if __name__ == "__main__":
    image_folder = "path/to/your/images"
    output_pdf = "output1.pdf"

    # Collect all image paths
    image_files = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    
    # Sort images to maintain order
    sorted_image_files = sort_images(image_files)
    
    convert_images_to_pdf(sorted_image_files, output_pdf)
