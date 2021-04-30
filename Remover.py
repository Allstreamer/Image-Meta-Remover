from PIL import Image
import numpy
import os

ImagesFolderPath = "./Images"
ResultsFolderPath = "./Results"

if not os.path.exists(ImagesFolderPath):
	print(f"Missing {ImagesFolderPath} Directory Creating Directory...\n")
	os.mkdir(ImagesFolderPath)

if not os.path.exists(ResultsFolderPath):
	print(f"Missing {ResultsFolderPath} Directory Creating Directory...\n")
	os.mkdir(ResultsFolderPath)

print(f"Place images into '{ImagesFolderPath}' \nThen Press enter to Procces them")
input("...")


print("Loading Images\n")
for filename in os.listdir(ImagesFolderPath):
	print(f"Found '{filename}'")
	img = Image.open(f"{ImagesFolderPath}/{filename}")

	#This Conversion is not Necessary but removes appended data
	img_array = numpy.array(img) 
	img_final = Image.fromarray(img_array)

	img.save(f"{ResultsFolderPath}/{filename}")

print(f"Done! Check {ResultsFolderPath}")
input("Press Enter to exit...")