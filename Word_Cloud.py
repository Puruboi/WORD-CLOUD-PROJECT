# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 10:04:29 2020

@author: Anonymous
"""

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys


from IPython.display import display
import fileupload

uploader = fileupload.FileUploadWidget()

def _handle_upload(change):
    w = change['owner']
    with open(w.filename, 'wb') as f:
        f.write(w.data)
    print('Uploaded `{}` ({:.2f} kB)'.format(
        w.filename, len(w.data) / 2**10))

uploader.observe(_handle_upload, names='data')

display(uploader)


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    # LEARNER CODE START HERE
    non_punctuation_text=""
    for char in file_contents:
        if char not in punctuations:
            non_punctuation_text=non_punctuation_text+char
    words=non_punctuation_text.split()
    clean_words=[]
    frequencies={}

    for word in words:
        if word.isalpha():
            if word not in uninteresting_words:
                clean_words.append(word)
    for alpha_word in clean_words:
        if alpha_word not in frequencies:
            frequencies[alpha_word]=1
        else:
            frequencies[alpha_word]+=1
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()


# Display your wordcloud image
myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()