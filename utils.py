import logging

from peewee import DatabaseError, DoesNotExist

from models import Ad


def add_db_entry(url, title):
    """
    Adds the ad to the db
    :param url:
    :param title:
    :return:
    """
    row = Ad(url=url, title=title)
    try:
        row.save()
    except DatabaseError as e:
        logging.exception(e)


def is_new(url, title):
    """
    Checks if a certain ad was already added to the db
    :param url:
    :param title:
    :return:
    """
    try:
        Ad.get(Ad.url == url, Ad.title == title)
        return False
    except DoesNotExist:
        return True
