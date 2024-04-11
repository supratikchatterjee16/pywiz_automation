from pywizlight import PilotBuilder
def get_average_screen0_pilot():
	from PIL import ImageGrab
	INTERVALS = 10
	average_color = [0, 0, 0]
	image = ImageGrab.grab()
	num = 0
	for x_point in range(int(image.size[0] / 2), image.size[0], INTERVALS):
		for y_point in range(0, image.size[1], INTERVALS):
			color = image.getpixel((x_point, y_point))
			for x in range(3):
				average_color[x] += color[x]
			num += 1
	num /= (INTERVALS * 2 / INTERVALS)
	pilot = PilotBuilder(rgb = (int(average_color[0] / num) , int(average_color[1] / num), int(average_color[2] / num)), brightness=255)
	return pilot

def get_average_screen1_pilot():
	from PIL import ImageGrab
	INTERVALS = 5
	average_color = [0, 0, 0]
	image = ImageGrab.grab()
	num = 0
	for x_point in range(0, int(image.size[0] / 2), INTERVALS):
		for y_point in range(0, image.size[1], INTERVALS):
			color = image.getpixel((x_point, y_point))
			for x in range(3):
				average_color[x] += color[x]
			num += 1
	num /= (INTERVALS * 2 / INTERVALS)
	val = [0, 0, 0]
	for i in range(3):
		val[i] = int(average_color[i] / num)
		val[i] = val[i] if val[i] < 255 else 255

	pilot = PilotBuilder(rgb = val, brightness=255)
	return pilot
