from instabot import Bot
from image_editor import create_image
import time

def print_date_time(): #example scheduled function
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))

def make_post(image_path, description, bot):
    bot.upload_photo(image_path, caption=description)
    time.sleep(2)

def post_all(spotteds):
    bot = Bot()
    
    bot.login(username=login, password=password, is_threaded=True)

    for spotted in spotteds:
        if(len(spotted['text']) < 2178):
            var = spotted['text']
            create_image(var)
            print("Postando #"+str(spotted['id']),end=' ',)
            print_date_time()
            make_post('assets/sample-out.jpg', "Spotted #" + str(spotted['id']) + "\n" + spotted['text'], bot)

if __name__ == '__main__':
    post_all([{'id':23423, 'text': 'Este spotted é para jose augusto aquele gostoso de bh'},])
