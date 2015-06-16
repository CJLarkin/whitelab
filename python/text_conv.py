import 
import sys
def text_conv(image):
	img_recovered = base64.decodestring(image)
	fname = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))
	f = open("uploads/" + fname, 'w')
	f.write(img_recovered)
	f.close()
text_conv(sys.argv[1])