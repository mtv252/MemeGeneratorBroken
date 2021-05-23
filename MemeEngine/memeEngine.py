"""Creates a standardly formatted Meme by cropping an Image
and adding text to it"""

from PIL import Image, ImageDraw, ImageFont
import random

class MemeEngine():

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create properly formatted meme

        Arguments:
            img_path {str} -- the file location for the input image.
            text - the text body of the supplied Quote.
            author - the attributed author of the supplied Quote
            width {int} -- The pixel width value. Default=500.
        Returns:
            str -- the file path to the output image.
        """
        with open(img_path) as img:

            if width is not None:
                ratio = width/float(img.size[0])
                height = int(ratio*float(img.size[1]))
                img = img.resize((width, height), Image.NEAREST)

            if text is not None and author is not None:
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype('./fonts/impact.ttf', size=20)
                draw.text((200, 10), text, font=font, fill='white')
                draw.text((200, 450), body, font=font, fill='white')

        out_path = img.save(f'./{random.randint(0,100000)}.jpg')
        return out_path
