"""Utilities Functions for Pramaan Service"""

import json
from logging import getLogger


def log_errors(name: str, message: str):
    logger = getLogger(name)
    logger.error(message)


def load_data(filepath: str) -> dict:
    """
    Load data from json file.
    :param filepath: str
    :return: dict
    """
    with open(filepath, "r") as file:
        data = json.load(file)
    return data


def get_model(app_label, model_name):
    """Returns Model Instance"""
    from django.apps import apps

    return apps.get_model(app_label=app_label, model_name=model_name)
