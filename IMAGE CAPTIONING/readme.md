# CODSOFT Task 3 — AI Image Captioning

## Project Overview
This project is an AI-powered Image Captioning web application built for the CODSOFT Artificial Intelligence Internship. It leverages pre-trained deep learning models to bridge the gap between Computer Vision and Natural Language Processing (NLP), automatically generating descriptive captions for uploaded images.

## Objective
To build a functional AI system that takes an image as input, extracts visual features using a pre-trained vision model, and generates a contextually accurate text caption using a transformer-based language model.

## Features
- **Upload Functionality:** Supports JPG, JPEG, and PNG formats.
- **Real-Time Preview:** Displays the uploaded image within the UI.
- **Fast AI Inference:** Utilizes Hugging Face transformers for optimized, local CPU processing.
- **Clean UI:** Built with Streamlit for a professional, interactive user experience.

## Technologies Used
- **Python** 
- **Streamlit** (Frontend GUI)
- **PyTorch** (Machine Learning framework)
- **Hugging Face Transformers** (Pre-trained model pipeline)
- **Pillow (PIL)** (Image processing)

## How It Works (Model Architecture)
The application uses the **BLIP (Bootstrapping Language-Image Pre-training)** model.
1. **Computer Vision Component:** A Vision Transformer (ViT) acts as the feature extractor (serving the same structural purpose as classic CNNs like ResNet/VGG but with modern transformer architecture). It analyzes the image and extracts semantic embeddings.
2. **NLP Component:** A Transformer-based text decoder takes the visual embeddings and auto-regressively predicts the most logical sequence of words to describe the scene.

## Project Structure
```text
Task3_Image_Captioning/
├── app.py               # Main application code
├── requirements.txt     # Python dependencies
├── .gitignore           # Git ignore rules
└── README.md            # Project documentation
