from os import listdir
from PIL import Image
import math
import os

# IMAGEパース
os.chdir('step_screenshot') 
# IMAGEタイプ
IMAGES_FORMAT = '.png'
# IMAGE転換結果ファイル
IMAGE_SAVE_PATH = '../final.jpg'

# ファイル名取得する
images = [Image.open(fn) for fn in listdir() if fn.endswith(IMAGES_FORMAT)]

# 列
IMAGE_COLUMN = 4
# 行
IMAGE_ROW = int(math.ceil(len(images)/IMAGE_COLUMN))
# サイズ
WIDTH, HEIGHT = images[0].size

BRODER = 10

#IMAGEを新規する
to_image = Image.new(images[0].mode, (IMAGE_COLUMN*(WIDTH+BRODER), IMAGE_ROW*(HEIGHT+BRODER)))
# IMAGEを組み合わせる
for i, image in enumerate(images):
    to_image.paste(image, box=(int(i%IMAGE_COLUMN*(WIDTH+BRODER)), int(math.floor(i/IMAGE_COLUMN)*(HEIGHT+BRODER))))
# IMAGEを保存する
to_image.save(IMAGE_SAVE_PATH)