#!/bin/bash

# generate 200k words, 1M images, 1M labels
# This stops when the number of images is exceeded
python generate-words.py --num-words 250000 --output-dir train-data --vocab danish --lang da

# There is no count for the number of images generated
# python generate-img.py --num-words 20 --num-images-per-word 5 --output-dir train-data --lang da

# This will generate the exact number of images
# python generate-labels.py --output-dir train-data --num-images 100 --lang da
