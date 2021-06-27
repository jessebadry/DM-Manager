"""Simple module to serialize/deserialize JSON for DM data.

    This module acts as a wrapper around a dictionary to create 


"""

import json


class DMManager:

    """The Dungeon Master Manager, manages and manipulates 
       DM-Data for dnd purposes.
    """


    def __init__(self, file_name):
        """Constructs DMManager object.
    
        :param file_name: string
        :precondition: file_name must be a valid path / accessible
        """

        self.file_name = file_name

        # Contains invidual users DM data
        # Stores discord-ids as keys and dicts as values for each individual user
        self.user_data = {}


    def save(self):
        """Serializes dungeon master data to json and saves to `self.file_name`.
    
        :raises OsError: if any error related to file IO occurs
        """

        with open(self.file_name, 'w') as file:
            json.dump(self.user_data, file)

    def __save_value(self, user_id, value):
        """Writes key-value pair (user-id, value), to the DM-Manager object.
        
        because this operation is potentially unsafe due to

        :param user_id: string representing the DM user's discord ID number
        :postcondition: self.dungeon_masters will contain the new key-value pair  
        """
        self.user_data[user_id] = value
        self.save()
