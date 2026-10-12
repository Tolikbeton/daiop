import cv2
from PIL import Image
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
image = cv2.imread("manface.png")
faces = face_cascade.detectMultiScale(image)

human = Image.open("manface.png").convert("RGBA")
glasses = Image.open("glasses.png").convert("RGBA")

for (x, y, w, h) in faces:
    glasses_resized = glasses.resize((int(w * 1.3), int(h / 3)))
    human.paste(glasses_resized, (int(x - w * 0.15), int(y + h / 4.0)), glasses_resized)

human.show()