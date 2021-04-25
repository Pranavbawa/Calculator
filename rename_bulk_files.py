import os

path = "C:/Users/Pranav Bawa/Pictures/Camera Roll/"

def rename_file():
    i = 0
    for filename in os.listdir(path):
        my_destination = "img" + str(i)+".jpg"
        my_source = path + filename
        my_destination = path + my_destination
        os.rename(my_source, my_destination)
        i = i+1
rename_file()