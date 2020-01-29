import os

from brainio import brainio
from imlib.image.scale import scale_and_convert_to_16_bits
from amap.tools import image as img_tools

data_dir = os.path.join("tests", "data")

raw_img_path = os.path.join(data_dir, "signal", "signal_ch000000.tif")
despeckled_path = os.path.join(data_dir, "image_processing", "despeckled.tif")
flatfield_path = os.path.join(data_dir, "image_processing", "flatfield.tif")


def test_despeckle_by_opening():
    img_test = brainio.load_any(raw_img_path)
    despeckled = brainio.load_any(despeckled_path)
    assert (despeckled == img_tools.despeckle_by_opening(img_test)).all()


def test_pseudo_flatfield():
    despeckled = brainio.load_any(despeckled_path)
    flatfield_validation = brainio.load_any(flatfield_path)

    flatfield_test = img_tools.pseudo_flatfield(despeckled)
    flatfield_test = scale_and_convert_to_16_bits(flatfield_test)
    assert (flatfield_validation == flatfield_test).all()
