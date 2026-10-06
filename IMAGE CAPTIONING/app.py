from PIL import Image
from transformers import BlipForConditionalGeneration, BlipProcessor

print("Loading model... this might take a minute on the first run.")

# Load pre-trained processor and vision-language model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image_path):
    # Load and preprocess image
    raw_image = Image.open(image_path).convert("RGB")

    # Generate caption using the transformer model
    inputs = processor(raw_image, return_tensors="pt")
    out = model.generate(**inputs, max_new_tokens=50)

    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

# --- Test the Model ---
# Make sure you have a real image named "test_image.jpg" saved in the same folder as this script!
image_file = "test_image.jpg"  

try:
    print(f"Analyzing {image_file}...")
    caption = generate_caption(image_file)
    print(f"\nSUCCESS! Generated Caption: {caption}")
except FileNotFoundError:
    print(f"\nError: Could not find '{image_file}'. Please place an image with this name in the same folder as your Python script.")
