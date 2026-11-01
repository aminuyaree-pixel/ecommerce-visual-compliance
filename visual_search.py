
import streamlit as st
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch

MODEL_NAME = "openai/clip-vit-base-patch32"


# Load CLIP only once and reuse it
@st.cache_resource(show_spinner="Loading CLIP model...")
def load_clip_model():

    model = CLIPModel.from_pretrained(MODEL_NAME)
    processor = CLIPProcessor.from_pretrained(MODEL_NAME)

    model.eval()

    return model, processor


def search_product(image_path):

    # Load cached model
    model, processor = load_clip_model()

    # Open product image
    image = Image.open(image_path).convert("RGB")

    descriptions = [
        "A leather handbag",
        "A school backpack",
        "A travel suitcase",
        "A shoulder bag",
        "A shopping bag"
    ]

    inputs = processor(
        text=descriptions,
        images=image,
        return_tensors="pt",
        padding=True
    )

    with torch.no_grad():
        outputs = model(**inputs)

    scores = outputs.logits_per_image.softmax(dim=1)[0]

    results = sorted(
        zip(descriptions, scores.tolist()),
        key=lambda item: item[1],
        reverse=True
    )

    return [
        {
            "description": description,
            "score": round(score, 4)
        }
        for description, score in results
    ]
