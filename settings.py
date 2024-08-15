import os
import random


def get_fonts():
    """
    Get all .ttf files in ./fonts
    """
    fonts = []
    for root, dirs, files in os.walk("./fonts"):
        for file in files:
            if file.endswith(".ttf"):
                fonts.append(os.path.join(root, file))

    return fonts


fonts = get_fonts()
couri_fonts = [font for font in fonts if "Couri" in font]
type_writer_fonts = [font for font in fonts if "SpecialElite-Regular" in font]

text_colors = [
    "#000000",  # Black
    "#FF0000",  # Red
    "#00FF00",  # Green
    "#0000FF",  # Blue
    "#FFFF00",  # Yellow
    "#00FFFF",  # Cyan
    "#FF00FF",  # Magenta
    "#C0C0C0",  # Silver
    "#808080",  # Gray
    "#800000",  # Maroon
    "#808000",  # Olive
    "#008000",  # Dark Green
    "#800080",  # Purple
    "#008080",  # Teal
    "#000080",  # Navy
]


def get_use_fonts():
    """
    Get the font to use for the text.
    1 in 5 chance to use couri_fonts, 1 in 5 chance to use type_writer_fonts,
    otherwise use all fonts.
    """
    choice = random.randint(1, 5)
    if choice == 1:
        return couri_fonts
    elif choice == 2:
        return type_writer_fonts
    else:
        return fonts


# Other configurations
def get_font():
    """
    From the list of fonts, choose a random font.
    """
    use_fonts = get_use_fonts()
    return random.choice(use_fonts)


def get_text_color():
    """
    Get a random text color from the list of text_colors.
    """
    return random.choice(text_colors)


def get_size():
    """
    Get a random font size
    """
    return random.randint(32, 124)


def get_space_width():
    """
    Get a random space width
    """
    return random.uniform(0.5, 2.5)


def get_character_spacing():
    """
    Get a random character spacing
    """
    return random.randint(0, 25)


def get_skewing_angle():
    """
    Get a random skewing angle
    """
    return random.randint(0, 5)


def get_blur():
    """
    Get a blur value
    """
    return random.choice([0, 1, 2])


def get_background_type():
    """
    Get a background type
    """
    return random.choice([0, 1, 2])


def transform_word(word):
    """
    1 out of 10 chance to transform the word to uppercase.
    """
    word_cased = word
    if random.randint(0, 9) == 0:
        word_cased = word.upper()

    return word_cased


def get_distorsion_orientation():
    """
    Get a distorsion orientation
    """
    return random.choice([0, 1])


def get_distorsion_type():
    """
    Get a distorsion type
    distorsion_type =  [0, 1, 2, 3] which means ["none", "sine", "cosine", "random"]
    """
    return random.choice([0, 1, 2, 3])


def get_orientation():
    """
    orientation is 0 for horizontal, 1 for vertical
    In this case, we will always use horizontal orientation.
    """
    return random.choice([0])
