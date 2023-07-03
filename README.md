# Ai_Ml_Caption_Generator

This is an AI tool that create multiple captions based on the image provided by the user.
The tool has interface built on Flask-HTML for uploading images and generating captions.
The video of the assignment working is given in this github.

### Model Information
The appication has been build on a pre-trained model [**'blip-image-captioning-large**](https://huggingface.co/Salesforce/blip-image-captioning-large) - (BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation)' from huggingface website.

### Further Developments
* The application can make three captions for the input. The accuracy of the caption prediction can be further developed by fine-tuning the model.
* The creativity of captions can be implemented by giving some input text along with the model so that it can create captions related to the text. This feature is best implemented after fine-tuning the model.
