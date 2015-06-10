from image_script import *
from text_conv import text_conv
import json

def img_rtv(pic):
	wjson = main(pic)
	wjdata = json.loads(wjson)
	img_list = []
	for i in range(0,len(wjdata)):
		for k,v in wjdata[i][1].items():
			img_list.append(v)
	return img_list

def txt2img(pic): #use this fuction when importing to other programs
	img_txt = img_rtv(pic)
	images = []
	for strg in img_txt:
		images.append(text_conv(strg))
	return images

print txt2img('Good_pic_copy.jpg')