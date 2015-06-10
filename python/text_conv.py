from IPython.display import Image
import sys
def text_conv(image):
	return Image(url = 'data:image/png;base64,{}'.format(image))
#text_conv(sys.argv[1])
