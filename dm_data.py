"""Simple module to serialize/deserialize JSON for DM data.

    This module acts as a wrapper around a dictionary to create 

"""

import json


class DMManager:

    """The Dungeon Master Manager, manages and manipulates 
       DM-Data for dnd purposes.
    """

    """Constructs DMManager object.
    
    :param file_name: string
    :precondition: file_name must be a valid path / accessible
    """
    def __init__(self, file_name):

        self.file_name = file_name

        # Contains invidual users DM data
        # Stores discord-ids as keys and dicts as values for each individual user
        self.dungeon_masters = {}

    """Serializes dungeon master data to json and saves to `self.file_name`.
    
    :raises OsError: if any error related to file IO occurs
    """
    def save(self):

        with open(self.file_name) as file:

            json.dump(self.dungeon_masters, file)

    """Writes key-value pair (user-id, value), to the DM-Manager object.
    
    :param user_id: User.id

    :postcondition: self.dungeon_masters will contain the new key-value pair
    :postcondition: self.dungeon_masters will be 
    
    """
    def save_value(self, user_id, value):
        self.dungeon_masters[user_id] = value
        self.save()
