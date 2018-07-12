#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Draw text into images."""

import os
import re

from PIL import Image, ImageFont, ImageDraw


def draw_text_into_images(dir_name, file_name, out_dir):
    """Perform draw text into target images.

    :param dir_name: target directory
    :param file_name: target file
    :param out_dir: output directory
    :return: None
    """

    # open image file
    img = Image.open(dir_name + os.sep + file_name)
    # get size
    size = img.size
    # get extend size
    extend = size[1] * 0.1
    # font size
    font_size = round(extend / 2.1)
    # extend image region
    box = (0, 0, size[0], size[1] + extend)
    # extend image
    n = img.crop(box)

    # color black
    black = (0, 0, 0)
    # color white
    white = (255, 255, 255)

    # create draw object
    draw = ImageDraw.Draw(n)
    # fill white to extended region
    draw.rectangle([(0, size[1]), (size[0], size[1] + extend)], white)

    # get text from file name
    text = str(file_name).split('.')[0]
    # calculate text start position
    # x = (width - length of text) / 2
    coo_x = (size[0] - len(text) * font_size) / 2
    # if length of text > width then change the font size
    if coo_x < 0:
        font_size = round(size[0] / len(text))
        coo_x = 0
    # set font and size
    font = ImageFont.truetype('./SourceHanSansSC-Normal.otf', font_size)
    coo = (coo_x, size[1])

    # draw text
    draw.text(coo, text, black, font)

    # check output dir
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    # get output file name
    o_file = out_dir + os.sep + 'out_' + str(file_name)
    # save image file
    n.save(o_file)


def get_image_files(file_list):
    """Get all images inside target directory

    :param file_list: list of target files
    :return: list of images
    """
    # filter image files
    reg = re.compile('\.jpg|\.png|\.jpeg|\.gif')
    images = filter(lambda x: bool(reg.search(x)), file_list)
    return [x for x in images]


def search_file_and_draws(dir_name, out_name):
    """Match image files and do draw.

    :param dir_name: target directory
    :param out_name: output directory
    :return: None
    """
    # check if it is a dir
    if os.path.isdir(dir_name):
        # get all files list
        files = os.listdir(dir_name)
        files = get_image_files(files)
        # loop images
        for im in files:
            draw_text_into_images(dir_name, im, out_name)
        print(u'Process completed\nOutput：{}\n'.format(out_name))
    else:
        print(u'The target is not a directory\n')


if __name__ == '__main__':

    # wait for input
    d_name = input(u'Enter target directory path please\n>')
    o_name = d_name + os.sep + 'out'
    search_file_and_draws(d_name, o_name)
