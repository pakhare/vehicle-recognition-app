import cv2
import numpy as np
import os

min_contour_width = 40  
min_contour_height = 40  
offset = 10  
line_height = 550  
matches = []
vehicles = 0

def get_centroid(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy

def detect(image_path):
  global matches, vehicles

  frame1 = cv2.imread(image_path)
  grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)  # Convert image to grayscale

  if len(matches) == 0:
      frame2 = grey.copy()
  else:
      frame2 = matches[-1][0].copy()

  d = cv2.absdiff(grey, frame2)
  blur = cv2.GaussianBlur(d, (5, 5), 0)
  ret, th = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
  dilated = cv2.dilate(th, np.ones((3, 3)))
  closing = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, np.ones((15, 15)))

  contours, _ = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  processed_image = frame1.copy()

  for contour in contours:
      (x, y, w, h) = cv2.boundingRect(contour)
      contour_valid = (w >= min_contour_width) and (h >= min_contour_height)
      
      if not contour_valid:
          continue
      
      cv2.rectangle(processed_image, (x - 10, y - 10), (x + w + 10, y + h + 10), (255, 0, 0), 2)
      centroid = get_centroid(x, y, w, h)
      cv2.circle(processed_image, centroid, 5, (0, 255, 0), -1)
      
      matches.append((grey, centroid))  # Append grayscale image
      
  # Remove old frames
  if len(matches) > 10:
      matches = matches[-10:]

  processed_image = cv2.line(processed_image, (0, line_height), (frame1.shape[1], line_height), (0, 255, 0), 2)

  output_dir = 'static/output'
  os.makedirs(output_dir, exist_ok=True)
  output_path = os.path.join(output_dir, os.path.basename(image_path))
  cv2.imwrite(output_path, processed_image)

  return output_path


