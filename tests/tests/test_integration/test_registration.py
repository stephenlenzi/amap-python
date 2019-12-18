import os
import sys
import pytest

import pandas as pd

from brainio.brainio import load_nii

from amap.config.config import get_config_ob
from amap.tools.general import get_text_lines
from amap.download.cli import main as amap_download
from amap.cli import run as amap_run

data_dir = os.path.join(os.getcwd(), "tests", "data", "brain",)
test_output_dir = os.path.join(
    os.getcwd(), "tests", "data", "registration_output",
)

x_pix = "40"
y_pix = "40"
z_pix = "50"


TEST_ATLAS = "allen_2017_100um"


def download_atlas(directory):
    download_args = [
        "amap_download",
        "--atlas",
        TEST_ATLAS,
        "--install-path",
        directory,
        "--no-amend-config",
    ]
    sys.argv = download_args
    amap_download()
    return directory


def generate_test_config(atlas_dir):
    config = os.path.join(os.getcwd(), "tests", "data", "config", "test.conf")
    config_obj = get_config_ob(config)
    atlas_conf = config_obj["atlas"]
    orig_base_directory = atlas_conf["base_folder"]

    with open(config, "r") as in_conf:
        data = in_conf.readlines()
    for i, line in enumerate(data):
        data[i] = line.replace(
            f"base_folder = '{orig_base_directory}",
            f"base_folder = '{os.path.join(atlas_dir, TEST_ATLAS)}",
        )
    test_config = os.path.join(atlas_dir, "config.conf")
    with open(test_config, "w") as out_conf:
        out_conf.writelines(data)

    return test_config


@pytest.mark.slow
def test_register(tmpdir):
    atlas_directory = str(tmpdir)
    download_atlas(atlas_directory)
    test_config = generate_test_config(atlas_directory)

    output_directory = os.path.join(atlas_directory, "output")
    amap_args = [
        "amap",
        data_dir,
        output_directory,
        "-x",
        x_pix,
        "-y",
        y_pix,
        "-z",
        z_pix,
        "--n-free-cpus",
        "0",
        "--registration-config",
        test_config,
    ]

    sys.argv = amap_args
    amap_run()

    image_list = [
        "affine_registered_atlas_brain.nii",
        "annotations.nii",
        "boundaries.nii",
        "brain_filtered.nii",
        "control_point_file.nii",
        "downsampled.nii",
        "downsampled_filtered.nii",
        "freeform_registered_atlas_brain.nii",
        "hemispheres.nii",
        "inverse_control_point_file.nii",
        "inverse_freeform_registered_brain.nii",
        "registered_atlas.nii",
        "registered_hemispheres.nii",
    ]

    for image in image_list:
        are_images_equal(image, output_directory, test_output_dir)

    assert get_text_lines(
        os.path.join(output_directory, "affine_matrix.txt")
    ) == get_text_lines(os.path.join(test_output_dir, "affine_matrix.txt"))

    assert get_text_lines(
        os.path.join(output_directory, "invert_affine_matrix.txt")
    ) == get_text_lines(
        os.path.join(test_output_dir, "invert_affine_matrix.txt")
    )

    assert (
        (
            pd.read_csv(os.path.join(output_directory, "volumes.csv"))
            == pd.read_csv(os.path.join(test_output_dir, "volumes.csv"))
        )
        .all()
        .all()
    )


def are_images_equal(image_name, output_directory, test_output_directory):
    image = load_nii(os.path.join(output_directory, image_name), as_array=True)
    test_image = load_nii(
        os.path.join(test_output_directory, image_name), as_array=True
    )

    assert (image == test_image).all()
