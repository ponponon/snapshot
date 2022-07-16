import unittest
from loguru import logger
from mark import BASE_DIR
from pathlib import Path
from PIL import Image
from PIL.Image import Image as PIL_Image
import sys
import io
from utils.image_helpers import *


class TestCompress(unittest.TestCase):
    def test_compress_on_memory_2(self):
        """
        python -m unittest testing.test_compress.TestCompress.test_compress_on_memory_2
        """

        src_file_path = BASE_DIR/'static/img/94dcb906ff774e7ab4d6e8b1abcc147b.png'

        png_image = Image.open(src_file_path)

        png_stream = png_image_2_png_stream(png_image)
        jpg_stream = png_image_2_jpg_stream(png_image, quality=50)

        # logger.debug(png_stream)
        logger.debug(type(png_stream))
        logger.debug(len(png_stream))

        logger.debug(type(jpg_stream))
        logger.debug(len(jpg_stream))

        logger.debug(f'压缩比: {round(len(jpg_stream)/len(png_stream)*100)}%')
