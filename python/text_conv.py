from IPython.display import Image
def fxn(image):
	return Image(url = 'data:image/png;base64,{}'.format(image)