import base64
import sys
def text_conv(image):
	#img_recovered = base64.decodestring(image)
	#fname = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))
	#f = open("uploads/" + fname, 'w')
	#f.write(img_recovered)
	#f.close()
	with open("foo.png","wb") as f:
    		f.write(base64.decodestring(image))
text_conv(sys.argv[1])