import pytest

import pandas as pd
import numpy as np

from pathlib import Path
from random import randint
from argparse import ArgumentTypeError

from amap.tools import general

test_2d_img = np.array([[1, 2, 10, 100], [5, 25, 300, 1000], [1, 0, 0, 125]])
validate_2d_img = np.array(
    [
        [65.535, 131.07, 655.35, 6553.5],
        [327.675, 1638.375, 19660.5, 65535],
        [65.535, 0, 0, 8191.875],
    ]
)


def test_check_positive_float():
    pos_val = randint(1, 1000) / 100
    neg_val = -randint(1, 1000) / 100

    assert pos_val == general.check_positive_float(pos_val)

    with pytest.raises(ArgumentTypeError):
        assert general.check_positive_float(neg_val)

    assert general.check_positive_float(None) is None

    with pytest.raises(ArgumentTypeError):
        assert general.check_positive_float(None, none_allowed=False)

    assert general.check_positive_float(0) == 0


def test_check_positive_int():
    pos_val = randint(1, 1000)
    neg_val = -randint(1, 1000)

    assert pos_val == general.check_positive_int(pos_val)

    with pytest.raises(ArgumentTypeError):
        assert general.check_positive_int(neg_val)

    assert general.check_positive_int(None) is None

    with pytest.raises(ArgumentTypeError):
        assert general.check_positive_int(None, none_allowed=False)

    assert general.check_positive_int(0) == 0


def test_initialise_df():
    test_df = general.initialise_df("one", "two", "3")
    df = pd.DataFrame(columns=["one", "two", "3"])
    assert df.equals(test_df)


def test_scale_to_16_bits():
    assert (validate_2d_img == general.scale_to_16_bits(test_2d_img)).all()


def test_scale_to_16_bits():
    validate_2d_img_uint16 = validate_2d_img.astype(np.uint16, copy=False)
    assert (
        validate_2d_img_uint16
        == general.scale_and_convert_to_16_bits(test_2d_img)
    ).all()


class Paths:
    def __init__(self, directory):
        self.one = directory / "one.aaa"
        self.two = directory / "two.bbb"
        self.tmp__three = directory / "three.ccc"
        self.tmp__four = directory / "four.ddd"


def test_delete_tmp(tmpdir):
    tmpdir = Path(tmpdir)
    paths = Paths(tmpdir)
    for attr, path in paths.__dict__.items():
        path.touch()
        print(path)
    assert len([child for child in tmpdir.iterdir()]) == 4
    general.delete_temp(tmpdir, paths)
    assert len([child for child in tmpdir.iterdir()]) == 2

    general.delete_temp(tmpdir, paths)
