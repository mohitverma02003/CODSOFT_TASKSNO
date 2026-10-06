import streamlit as st
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# 1. Page Configuration
st.set_page_config(
    page_title="AI Image Captioning",
    page_icon="📷",
    layout="centered"
)

# 2. Load the Model and Processor (Cached so it only loads once)
@st.cache_resource
def load_model():
    # We use the BLIP model from Hugging Face for state-of-the-art image captioning
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

# 3. User Interface
st.title("📷 AI Image Captioning")
st.write("Upload an image, and the AI will generate a descriptive caption using Computer Vision and Natural Language Processing.")

# Display a loading message while the model downloads/loads
with st.spinner("Loading AI Model (This may take a minute on first run)..."):
    processor, model = load_model()

# 4. File Uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 5. Display the uploaded image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # 6. Generate Caption Button
    if st.button("Generate Caption"):
        with st.spinner("Analyzing image features and generating caption..."):
            try:
                # Preprocess the image (Computer Vision)
                inputs = processor(image, return_tensors="pt")
                
                # Generate text tokens (NLP / Transformer)
                out = model.generate(**inputs, max_new_tokens=50)
                
                # Decode the tokens into a readable string
                caption = processor.decode(out[0], skip_special_tokens=True)
                
                # Display the result
                st.success("Caption Generated Successfully!")
                st.markdown(f"### 📝 **Caption:** {caption.capitalize()}")
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
