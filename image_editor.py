from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import textwrap

def create_image(string):
    if(len(string)>500):
        string = textwrap.wrap(string, width=500)
        string[0] = string[0] + "..."
        create_image(string[0])
        return False
    else: 
        img = Image.open("assets/1.jpg")
        width, height = img.size
        draw = ImageDraw.Draw(img)
        #string = textwrap.wrap(<string>,<widtdh=>)
        textsize = 44 
        string = textwrap.wrap(string, width=40)
        #font = ImageFont.truetype(<font-file>, <font-size>)
        font = ImageFont.truetype("assets/DejaVuSans.ttf", textsize)
        h = (height - len(string)*textsize)/2
        for line in string:
            a,b = draw.textsize(line, font=font)
            draw.text(((width-a)/2,h), line,fill=(0,0,0),font=font,align='center')
            h += textsize + 8
        img.save('assets/sample-out.jpg')
        return True
   
if __name__ == '__main__':
    create_image("Saudades de ir na unicamp ter mais uma aula normal e ver o raposo vagando pelas salas ❤️")
