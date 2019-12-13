import logging

from pathlib import Path


class Run:
    """
    Determines what parts of amap to run, based on what files already exist
    """

    def __init__(self, paths, boundaries=True, additional_images=False):
        self.paths = paths
        self._boundaries = boundaries
        self._additional_images = additional_images

    @property
    def freeform(self):
        if Path(self.paths.control_point_file_path).exists():
            logging.info("Freeform registration allready completed, skipping.")
            return False
        else:
            return True

    @property
    def segment(self):
        if Path(self.paths.registered_atlas_path).exists():
            logging.info("Registered atlas exists, skipping segmentation")
            return False
        else:
            return True

    @property
    def hemispheres(self):
        if Path(self.paths.registered_hemispheres_img_path).exists():
            logging.info("Registered hemispheres exist, skipping segmentation")
            return False
        else:
            return True

    @property
    def inverse_transform(self):
        if Path(self.paths.inverse_control_point_file_path).exists():
            logging.info(
                "Inverse transform exists, skipping inverse registration"
            )
            return False
        else:
            return True

    @property
    def volumes(self):
        if Path(self.paths.volume_csv_path).exists():
            logging.info(
                "Volumes csv exists, skipping region volume calculation"
            )
            return False
        else:
            return True

    @property
    def boundaries(self):
        if self._boundaries:
            if Path(self.paths.boundaries_file_path).exists():
                logging.info(
                    "Boundary image exists, skipping boundary image generation"
                )
                return False
            else:
                return True
        else:
            logging.info("Boundary image deselected, not generating")
            return False
