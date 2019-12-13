import logging

from pathlib import Path


class Run:
    """
    Determines what parts of amap to run, based on what files already exist
    """

    def __init__(
        self, paths, boundaries=True, additional_images=False, debug=False
    ):
        self.paths = paths
        self._boundaries = boundaries
        self._additional_images = additional_images
        self._debug = debug

    @property
    def affine(self):
        if self.freeform or self.inverse_transform:
            logging.info("Affine matrix already calculated, skipping")
            return False
        else:
            return True

    @property
    def freeform(self):
        if Path(self.paths.control_point_file_path).exists():
            logging.info("Freeform registration already completed, skipping.")
            return False
        else:
            return True

    @property
    def segment(self):
        if self._registered_atlas_exists:
            logging.info("Registered atlas exists, skipping segmentation")
            return False
        else:
            return True

    @property
    def hemispheres(self):
        if self._registered_hemispheres_exists:
            logging.info("Registered hemispheres exist, skipping segmentation")
            return False
        else:
            return True

    @property
    def inverse_transform(self):
        if self._inverse_control_point_exists:
            logging.info(
                "Inverse transform exists, skipping inverse registration"
            )
            return False
        else:
            return True

    @property
    def volumes(self):
        if self._volumes_exist:
            logging.info(
                "Volumes csv exists, skipping region volume calculation"
            )
            return False
        else:
            return True

    @property
    def boundaries(self):
        if self._boundaries:
            if self._boundaries_exist:
                logging.info(
                    "Boundary image exists, skipping boundary image generation"
                )
                return False
            else:
                return True
        else:
            logging.info("Boundary image deselected, not generating")
            return False

    @property
    def delete_temp(self):
        return self._debug

    @property
    def _inverse_control_point_exists(self):
        return self._exists(self.paths.inverse_control_point_file_path)

    @property
    def _registered_atlas_exists(self):
        return self._exists(self.paths.registered_atlas_path)

    @property
    def _registered_hemispheres_exists(self):
        return self._exists(self.paths.registered_hemispheres_img_path)

    @property
    def _volumes_exist(self):
        return self._exists(self.paths.volume_csv_path)

    @property
    def _boundaries_exist(self):
        return self._exists(self.paths.boundaries_file_path)

    @staticmethod
    def _exists(path):
        if isinstance(path, Path):
            return path.exists()
        else:
            return Path(path).exists()
