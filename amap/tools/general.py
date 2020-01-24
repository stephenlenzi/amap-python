"""
general
===============

General tools, used across amap

"""

import os
import logging
import pandas as pd

from imlib.system import check_path_in_dir


def initialise_df(*column_names):
    """
    Initialise a pandasdataframe with n column names
    :param str column_names: N column names
    :return: Empty pandas dataframe with specified column names
    """
    return pd.DataFrame(columns=column_names)


def delete_temp(directory, paths, prefix="tmp__"):
    """
    Removes all temp files (properties of an object starting with "tmp__")
    :param directory: Directory to delete tmp files from
    :param paths: Paths object with temp paths.
    :param prefix: String that temporary files (to be deleted) begin with.
    """
    for path_name, path in paths.__dict__.items():
        if path_name.startswith(prefix):
            if check_path_in_dir(path, directory):
                try:
                    os.remove(path)
                except FileNotFoundError:
                    logging.debug(
                        f"File: {path} not found, not deleting. "
                        f"Proceeding anyway."
                    )


def suppress_specific_logs(logger, message):
    logger = logging.getLogger(logger)

    class NoParsingFilter(logging.Filter):
        def filter(self, record):
            return not record.getMessage().startswith(message)

    logger.addFilter(NoParsingFilter())
