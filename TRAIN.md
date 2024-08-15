# Generating synthetic data for training docTR OCR

This is a fork of the TextRecognitionDataGenerator. 

The fork is used for generating syntehic data for training a the excellent [docTR OCR](https://github.com/mindee/doctr) engine.

I would use the original lib but it had outdated dependencies and I could not get it to work.

I just updated the `arabic-reshaper` to 3.0.0 and it seems to work for my purpose. 

When `TextRecognitionDataGenerator` is updated I will switch back to the original lib.

## Install

    git clone https://github.com/diversen/TextRecognitionDataGenerator.git
    cd TextRecognitionDataGenerator
    python3 -m venv venv
    source venv/bin/activate 
    pip install -r requirements.txt

## generate synth images

### generate some words from wikipedia**

This will generate at least `1000` words in a sqlite3 `database.db` placed in `train-data-da`. 
Using docTR vocab `danish` and wiki lang `da`. 

    python generate-words.py --num-words 1000 --output-dir train-data-da --vocab danish --lang da

### generate images from database words

In the `train-data-da/images` generate `1000 x 2` images using `da` words. 

    python generate-img.py --num-words 1000 --num-images-per-word 2 --output-dir train-data-da --lang da

### generate labels

    python generate-labels.py --output-dir train-data-da --num-words 2000 --lang da


