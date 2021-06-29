"""Contains miscellaneous utility functions """

from inspect import currentframe


def line():
    """Get current line number from called location.


    :return: `int` of line number
    """

    cf = currentframe()
    
    return cf.f_back.f_lineno


def get_user_id(member):
    """Extract user-id from Member Object."""

    return member.author.id
