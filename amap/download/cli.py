import os
import tempfile
from pathlib import Path

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

from amap.download import atlas
from amap.download.download import amend_cfg

home = str(Path.home())
DEFAULT_DOWNLOAD_DIRECTORY = os.path.join(home, ".amap", "atlas")
temp_dir = tempfile.TemporaryDirectory()
temp_dir_path = temp_dir.name


def atlas_parser(parser):
    parser.add_argument(
        "--install-path",
        dest="install_path",
        type=str,
        default=DEFAULT_DOWNLOAD_DIRECTORY,
        help="The path to install files to.",
    )
    parser.add_argument(
        "--download-path",
        dest="download_path",
        type=str,
        help="The path to download atlas into.",
    )
    parser.add_argument(
        "--no-atlas",
        dest="no_atlas",
        action="store_true",
        help="Don't download the atlas",
    )
    parser.add_argument(
        "--atlas",
        dest="atlas",
        type=str,
        default="allen_2017",
        help="The atlas to use",
    )
    return parser


def download_parser():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser = atlas_parser(parser)
    return parser


def main():
    args = download_parser().parse_args()
    if args.download_path is None:
        args.download_path = os.path.join(temp_dir_path, "atlas.tar.bz2")
    if not args.no_atlas:
        atlas_dir = os.path.join(args.install_path, "atlas")
        atlas.main(args.atlas, atlas_dir, args.download_path)

    amend_cfg(
        new_atlas_folder=atlas_dir, atlas=args.atlas,
    )


if __name__ == "__main__":
    main()
