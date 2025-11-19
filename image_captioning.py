import streamlit as st
from PIL import Image
from transformers import BlipProcessor, TFBlipForConditionalGeneration

@st.cache_resource
def load_model():
    """Loads and caches the BLIP model and processor."""
    processor = BlipProcessor.from_pretrained("./blip-image-captioning-base")
    model = TFBlipForConditionalGeneration.from_pretrained("./blip-image-captioning-base")
    return processor, model

def generate_caption(image):
    """
    Generates a caption for an image using the cached BLIP model.

    Args:
        image (PIL.Image.Image): The image to be captioned.

    Returns:
        str: The generated caption.
    """
    processor, model = load_model()

    # unconditional image captioning
    inputs = processor(image, return_tensors="tf")

    out = model.generate(**inputs)
    return processor.decode(out[0], skip_special_tokens=True)
