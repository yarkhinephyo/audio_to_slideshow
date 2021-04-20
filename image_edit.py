from PIL import Image, ImageDraw, ImageFont

from config import WIDTH, HEIGHT


def resize(image_pil, width, height):
    """Resize image keeping the ratio and using white background

    Args:
        image_pil (Image): Image Object,
        width (int),
        height (int),

    Returns:
        [Image]: Image Object
    """
    ratio_w = width / image_pil.width
    ratio_h = height / image_pil.height
    if ratio_w < ratio_h:
        # It must be fixed by width
        resize_width = width
        resize_height = round(ratio_w * image_pil.height)
    else:
        # Fixed by height
        resize_width = round(ratio_h * image_pil.width)
        resize_height = height
    image_resize = image_pil.resize(
        (resize_width, resize_height), Image.ANTIALIAS)
    background = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    offset = (round((width - resize_width) / 2),
              round((height - resize_height) / 2))
    background.paste(image_resize, offset)
    return background.convert('RGB')


def add_text_to_image(text, save_path, img_path=None):
    """Given a text string and file path of an image
    Add the text to image and save it in a new path

    Args:
        text (str): Text to embed into image
        save_path (str): Path to save the new image
        img_path (str, optional): Path of the original image. Defaults to None.
    """
    if img_path:
        writeimg = resize(Image.open(img_path), WIDTH, HEIGHT)
        newimg = Image.new("RGB", writeimg.size)
        newimg.paste(writeimg)
    else:
        newimg = Image.new("RGB", (WIDTH, HEIGHT))
    width_image, height_image = newimg.size[0], newimg.size[1]

    draw = ImageDraw.Draw(newimg)

    for font_size in range(80, 0, -5):
        font = ImageFont.truetype("impact.ttf", font_size)
        if font.getsize(text)[0] <= width_image*0.9:
            break
    else:
        print('no fonts fit!')

    draw.text((int(0.05*width_image), int(0.75*height_image)),
              text, (255, 255, 255, 255), font=font)
    newimg.save(save_path)


def save_gif(img_save_paths, dest_path, duration=2000):
    """Given paths of images, save a GIF image after concatenating them

    Args:
        img_save_paths (list): List of image paths
        dest_path (str): File path to save to
        duration (int, optional): Milliseconds between frames. Defaults to 2000.
    """
    fp_out = dest_path
    # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
    img, *imgs = [Image.open(f) for f in img_save_paths]
    img.save(fp=fp_out, format='GIF', append_images=imgs,
             save_all=True, duration=duration, loop=0)
