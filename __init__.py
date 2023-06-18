import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration

#implementing the pretrained model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

#defining some parameters for captions
#num_beams = 4                         #integrity of caption
#num_return_sequences = 5     
#gen_kwargs = {"num_return_sequences": num_return_sequences}

#Initialising the flask application
app = Flask(__name__)

def generate_caption(image):
    captions=[]
    inputs = processor(image, return_tensors="pt")
    for _ in range(3):
        caption = model.generate(**inputs, num_beams=5, num_return_sequences=5,temperature=0.8)
        decoded_captions = processor.batch_decode(caption, skip_special_tokens=True)
        unique_captions = list(set(decoded_captions))
        captions.extend(unique_captions)
        if len(captions) >= 3:
            break
    captions = captions[:3]
    return captions

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        #gets the image uploaded
        image = request.files['image']
        img = Image.open(image).convert('RGB')

        caption = generate_caption(img)

        return render_template('index.html', caption=caption)
    return render_template('index.html')
