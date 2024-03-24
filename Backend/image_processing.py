import os
import numpy as np
from skimage import io, color, filters, measure

def detect(input_image_path, output_dir='static/output'):
	try:
		os.makedirs(output_dir, exist_ok=True)

		image = io.imread(input_image_path)
		image_rgb = color.rgba2rgb(image)
		gray_image = color.rgb2gray(image_rgb)
		edges = filters.sobel(gray_image)
		contours = measure.find_contours(edges, 0.1)
		min_area = 500
		max_area = 5000
		vehicle_contours = []
		for contour in contours:
			area = measure.regionprops(measure.label(contour))[0].area
			if min_area < area < max_area:
			    vehicle_contours.append(contour)
		for contour in vehicle_contours:
			y, x = contour.T
			min_x, min_y = np.min(x), np.min(y)
			max_x, max_y = np.max(x), np.max(y)
			image_rgb[min_x:max_x, min_y] = [255, 0, 0]
			image_rgb[min_x:max_x, max_y] = [255, 0, 0]
			image_rgb[min_x, min_y:max_y] = [255, 0, 0]
			image_rgb[max_x, min_y:max_y] = [255, 0, 0]
		output_image_path = os.path.join(output_dir, os.path.basename(input_image_path))
		io.imsave(output_image_path, image_rgb.astype(np.uint8))
	except:
		output_image_path = os.path.join(output_dir, os.path.basename('error.jpeg'))
	return output_image_path

