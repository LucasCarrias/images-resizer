from os import listdir, makedirs
from os.path import isfile, join, realpath, exists
from skimage import data, color, io
from skimage.io import imread, imsave
from skimage.transform import rescale, resize, downscale_local_mean


def resize_and_save_img(file, new_size, parent=""):
    image = imread(parent+file)
    extension = file.split(".")[-1]
    image_resized = resize(image, (image.shape[0] // (1 // new_size), image.shape[1] // (1 // new_size)), anti_aliasing=True)
    save_dir = parent + "/resized-images/"
    if not exists(save_dir):
        makedirs(save_dir)
    if extension != "png":
        imsave(save_dir + file, image_resized, quality=100)
    else:
        imsave(save_dir + file, image_resized)


def is_image(file_path):
    img_extensions = ["jpg", "png", "jpeg"]
    file = file_path.split("/")[-1]
    file_ext = file.split(".")[-1]
    return file_ext in img_extensions


def resize_imgs_in_dir():
    files = [file for file in listdir() if isfile(file)]
    current_path = realpath(".")+r"/"
    for file in files:
        if is_image(file):
            print("Processing: " + file)
            resize_and_save_img(file, 0.5, current_path)


if __name__ == "__main__":       
    resize_imgs_in_dir()