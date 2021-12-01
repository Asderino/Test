#Using Pytorch and Hugging Transformers to generate text with an AI
#Python versions 3.10.x are NOT supported by Pytorch

#install Pytorch using pip (default installation, no CUDA
pip install torch torchvision torchaudio

#We need to install transformers to work with Pytorch
pip install transformers

#importing Pipeline from transformers
from transformers import pipeline

#var creation
text_generator = pipeline("text-generation")

#you can create some variables to store differnt parameters, we are going to directly print the result
print(text_generator("This is a test",max_lenght=200,do_sample = True,temperature = 0.8))
                     
