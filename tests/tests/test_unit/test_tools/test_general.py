import pandas as pd
from pathlib import Path

from amap.tools import general


def test_initialise_df():
    test_df = general.initialise_df("one", "two", "3")
    df = pd.DataFrame(columns=["one", "two", "3"])
    assert df.equals(test_df)


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
