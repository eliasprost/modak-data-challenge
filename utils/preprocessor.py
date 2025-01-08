# -*- coding: utf-8 -*-
import json
import os

import pandas as pd
from loguru import logger


class FileIO:
    """
    Convenience class for saving and loading data in parquet and json formats
    to/from disk.
    """

    @staticmethod
    def _file_exists(file_path: str) -> bool:
        """
        Checks if a file exists on disk.

        Args:
            file_path (str): path to file
        """
        return os.path.exists(file_path)

    @staticmethod
    def load_json(file_path: str, flatten: bool = True) -> pd.DataFrame:
        """
        Loads json file from disk and returns it as a pandas DataFrame.

        Args:
            file_path (str): path to json file
            flatten (bool): whether to normalize the json file
        """

        if not FileIO._file_exists(file_path):
            logger.error(f"File {file_path} does not exist.")
            raise FileNotFoundError(f"File {file_path} does not exist.")

        data = json.load(open(file_path))
        df = pd.json_normalize(data) if flatten else pd.DataFrame(data)
        logger.info(f"Loaded json file from {file_path}.")

        return df

    @staticmethod
    def load_csv(file_path: str, **kwargs) -> pd.DataFrame:
        """
        Loads csv file from disk and returns it as a pandas DataFrame.

        Args:
            file_path (str): path to csv file
        """

        if not FileIO._file_exists(file_path):
            logger.error(f"File {file_path} does not exist.")
            raise FileNotFoundError(f"File {file_path} does not exist.")

        df = pd.read_csv(file_path, **kwargs)
        logger.info(f"Loaded csv file from {file_path}.")

        return df


class Preprocessor:
    """
    Convenience class for preprocessing data.
    """

    @staticmethod
    def parse_date(value: str) -> pd.Timestamp:
        """
        Parse date from mixed formats.

        Args:
            value (str): date string
        """
        try:
            # Attempt to parse ISO format (with Z at the end)
            return pd.to_datetime(value, utc=True)
        except ValueError:
            try:
                # If ISO fails, attempt to parse as UNIX epoch (in seconds)
                return pd.to_datetime(int(value), unit="s", utc=True)
            except (ValueError, OverflowError):
                # Handle any other parsing errors gracefully
                return pd.NaT
