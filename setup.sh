#!/bin/bash
mkdir -p blip-image-captioning-base && \
wget -P blip-image-captioning-base https://huggingface.co/Salesforce/blip-image-captioning-base/resolve/main/tf_model.h5 && \
wget -P blip-image-captioning-base https://huggingface.co/Salesforce/blip-image-captioning-base/resolve/main/config.json && \
wget -P blip-image-captioning-base https://huggingface.co/Salesforce/blip-image-captioning-base/resolve/main/preprocessor_config.json && \
wget -P blip-image-captioning-base https://huggingface.co/Salesforce/blip-image-captioning-base/resolve/main/tokenizer.json && \
wget -P blip-image-captioning-base https://huggingface.co/Salesforce/blip-image-captioning-base/resolve/main/special_tokens_map.json && \
wget -P blip-image-captioning-base https://huggingface.co/Salesforce/blip-image-captioning-base/resolve/main/tokenizer_config.json && \
wget -P blip-image-captioning-base https://huggingface.co/Salesforce/blip-image-captioning-base/resolve/main/vocab.txt
