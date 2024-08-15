# Training docTR OCR

This is a fork of the TextRecognitionDataGenerator. 

The fork is used for generating syntehic data for training the excellent [docTR OCR](https://github.com/mindee/doctr) engine.

I would use the original lib, but some dependencies seems outdated and I could not get it to work.

I just updated the dependency `arabic-reshaper` to 3.0.0 and it seems to work for my purpose. 

If `TextRecognitionDataGenerator` is updated I will switch back to the original lib.

## Install

    git clone https://github.com/diversen/TextRecognitionDataGenerator.git
    cd TextRecognitionDataGenerator
    python3 -m venv venv
    source venv/bin/activate 
    pip install -r requirements.txt

## generate synth images

You may edit the `settings.py` file to change the `font` and `font_size` used for generating the images.

You may also alter the fonts in the `fonts` folder.

There is also a bunch of other settings you may alter.

### generate some words from wikipedia

This will generate at least `1000` words in a sqlite3 `database.db` placed in `train-data`. 
Using docTR vocab `danish` and wiki lang `da`. 

    python generate-words.py --num-words 1000 --output-dir train-data --vocab danish --lang da

### generate images from database words

In the `train-data/images` generate `1000 x 2` images using `da` words. 

    python generate-img.py --num-words 1000 --num-images-per-word 2 --output-dir train-data --lang da

### generate labels

    python generate-labels.py --output-dir train-data --num-words 2000 --lang da


If you have followed the above steps you should have a `train-data` folder with images and labels, 
which can be given as input to the `docTR OCR` training script.

In practice you will have to generate many more images and labels.

Likewise you would generate a folder with `validation-data` for validating the training. 

## Training

I think the easiest way to train is to use the `docTR OCR` training script.
In the following there is instructions for pytorch training. 

Clone the docTR repo and run the training script.

    git clone https://github.com/mindee/doctr
    cd doctr
    python3 -m venv venv
    source venv/bin/activate 
    pip install "python-doctr[tf]"
    pip install -r references/requirements.txt

### train danish from scratch

    python references/recognition/train_pytorch.py crnn_vgg16_bn --vocab danish --train_path train-data --val_path validation-data --epochs 5 

### resume from french model

    python references/recognition/train_pytorch.py crnn_vgg16_bn --max-chars 32 --vocab danish --train_path train-data --val_path validation-data --epochs 5 --pretrained

### resume on local trained model

    python references/recognition/train_pytorch.py crnn_vgg16_bn --max-chars 32 --vocab danish --train_path train-data --val_path validation-data --epochs 5 --pretrained --resume crnn_vgg16_bn_20240316-233300.pt

### resume on crn_vgg16_bn 

    python references/recognition/train_pytorch.py crnn_vgg16_bn --vocab danish --train_path train-data --val_path validation-data --epochs 1 --resume /home/dennis/.cache/doctr/models/crnn_vgg16_bn-9762b0b0.pt

# push to hub

 python references/recognition/train_pytorch.py crnn_vgg16_bn --max-chars 32 --vocab danish --train_path train-data --val_path validation-data --epochs 1 --pretrained --resume crnn_vgg16_bn_20240317-095746.pt --push-to-hub --name doctr-torch-crnn_vgg16_bn-danish-v1

# example convert from .pt to .bin

    python convert.py


