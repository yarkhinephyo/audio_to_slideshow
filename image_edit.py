from PIL import Image, ImageDraw, ImageFont

def resize(image_pil, width, height):
    '''
    Resize PIL image keeping ratio and using white background.
    '''
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
    image_resize = image_pil.resize((resize_width, resize_height), Image.ANTIALIAS)
    background = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    offset = (round((width - resize_width) / 2), round((height - resize_height) / 2))
    background.paste(image_resize, offset)
    return background.convert('RGB')

def add_text_to_image(text, save_path, img_path=None):
    if img_path:
        writeimg = resize(Image.open(img_path), 500, 400)
        newimg = Image.new("RGB", writeimg.size)
        newimg.paste(writeimg)
    else:
        newimg = Image.new("RGB", (500, 400))
    width_image, height_image = newimg.size[0], newimg.size[1]

    draw = ImageDraw.Draw(newimg)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    for font_size in range(80, 0, -5):
        font = ImageFont.truetype("impact.ttf", font_size)
        if font.getsize(text)[0] <= width_image*0.9:
            break
    else:
        print('no fonts fit!')
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((int(0.05*width_image), int(0.75*height_image)), text, (255, 255, 255, 255), font=font)
    newimg.save(save_path)

def save_gif(img_save_paths, dest_path, duration=2000):
    fp_out = dest_path
    # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
    img, *imgs = [Image.open(f) for f in img_save_paths]
    img.save(fp=fp_out, format='GIF', append_images=imgs, save_all=True, duration=duration, loop=0)