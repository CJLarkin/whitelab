import base64
import sys

data = r'iVBORw0KGgoAAAANSUhEUgAAASwAAAEsCAIAAAD2HxkiAAAElUlEQVR4nO3cy27bMBRAwaro//%2By%0Au0hQFKiTyrakQ9Izq6wi0rpHzNPb7Xb7AXR%2B1guAdydCiIkQYiKEmAghJkKIiRBiIoSYCCEmQoiJ%0AEGIihJgIISZCiIkQYiKEmAghJkKIiRBiIoSYCCEmQoiJEGIihJgIISZCiIkQYiKEmAghJkKIiRBi%0AIoSYCCEmQoiJEGIihJgIISZCiIkQYiKEmAghJkKIiRBiIoSYCCEmQoiJEGIihJgIISZCiIkQYiKE%0AmAghJkKIiRBiIoSYCCEmQoiJEGIihJgIISZCiIkQYiKEmAghJkKIiRBiIoSYCCEmQoiJEGIihJgI%0AISZCiIkQYiKEmAghJkKIiRBiIoSYCCEmQoiJEGIihJgIISZCiIkQYiKEmAghJkKIiRBiIoSYCCEm%0AQoiJEGIihJgIISZCiIkQYiKEmAghJkKIiRBiIoSYCCEmQoiJEGIihJgIISZCiIkQYiKEmAghJkKI%0AiRBiIoSYCCEmQoiJEGIihJgIISZCiIkQYiKEmAghJkKIiRBiIoSYCCEmQoiJEGIihJgIISZCiIkQ%0AYiKEmAgfsG1bvQQW9KtewBw%2B8rvdbn8%2BqFfEOjbz9L271W2b143DGKYvfX/oORI5igjv2B/YjEei%0Ax8do5puhUz0xoBPN9N9LnWjZyxPhpxeHcvAj8avdDb7sN%2BEeHHYmjHm2/HdVYy57j2WeIIts4zln%0AzN84k/HQ7sZZ9h7zPjjumumlP9Z5Y5ePyHMLyJe9xxSLfNQ7RnjNjUzOlte3NuyRuGR%2BHwZ9xU9y%0A8Y288nIHXmu0cR9tPYd7lwjDG3n2pU/6/CMcicvn96F/oc82yI08Y6YnzXvwS19v5QhHu5GTfsV4%0A8ZE42l27wJoRjnwjX5zpZGuX/SjrgqsMaLUIp7iRk/4K4dQFjPAtaGWdnecz%2Bqj9YzfU1g6vZajd%0AJRaJcNLn6KR/U7b2H/pdb8rZXczdJ8j4A/rKg2/83V1JhEOY9J%2BM1v7Pr8uIcCCTDujOI3HS3V1A%0AhBzAW4G8QoQc5t8jUX57iJAjeW/IJ4iQ4036G6OKd%2BDmeAp8iAghJkKIiRBiIoSYCCEmQoiJEGIi%0AhJgIISZCiIkQYiKEmAghJkKIiRBiIoSYCCEmQoiJEGIihJgIISZCiIkQYiKEmAghJkKIiRBiIoSY%0ACCEmQoiJEGIihJgIISZCiIkQYiKEmAghJkKIiRBiIoSYCCEmQoiJEGIihJgIISZCiIkQYiKEmAgh%0AJkKIiRBiIoSYCCEmQoiJEGIihJgIISZCiIkQYiKEmAghJkKIiRBiIoSYCCEmQoiJEGIihJgIISZC%0AiIkQYiKEmAghJkKIiRBiIoSYCCEmQoiJEGIihJgIISZCiIkQYiKEmAghJkKIiRBiIoSYCCEmQoiJ%0AEGIihJgIISZCiIkQYiKEmAghJkKIiRBiIoSYCCEmQoiJEGIihJgIISZCiIkQYiKEmAghJkKIiRBi%0AIoSYCCEmQoiJEGIihJgIISZCiIkQYiKEmAghJkKIiRBiIoSYCCEmQoiJEGIihJgIISZCiIkQYiKE%0AmAghJkKIiRBiIoTYbx6MbQaSP2GzAAAAAElFTkSuQmCC%0A'

def decode_base64(data):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += b'='* missing_padding
    return base64.decodestring(data)

def text_conv(image):
	#img_recovered = base64.decodestring(image)
	#fname = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))
	#f = open("uploads/" + fname, 'w')
	#f.write(img_recovered)
	#f.close()
	with open("foo.png","wb") as f:
    		f.write(decode_base64(image))
text_conv(data)