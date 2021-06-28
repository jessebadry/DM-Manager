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

        self.user_data_is_modified = False

        # Contains invidual users DM data
        # Stores discord-ids as keys and dicts as values for each individual user
        self.user_data = {}

    def add_camp():
        """Adds campaign to the DM-Manager object.

        :postcondition: if no campaign is selected on creation, 
        the newly added campaign will be set as the selected campaign
        
        """
        pass

    def add_member(user, character_name):
        """Adds character to the currently selected campaign.

        :param user: Discord User
        :param character_name: string 30 char limit

        :precondition: user must not be None
        :precondition: length of character_name <= 30
        """
        pass

    def save(self):
        """Serializes user-data to json and saves to `self.file_name`.

        :raises OsError: if any error related to file IO occurs
        """

        with open(self.file_name, 'w') as file:
            json.dump(self.user_data, file)
            self.user_data_is_modified = False

    def __save_value(self, user_id, value):
        """Writes key-value pair (user-id, value), to the DM-Manager object.

        because this operation is potentially unsafe due to

        :param user_id: string representing the DM user's discord ID number
        :postcondition: self.dungeon_masters will contain the new key-value pair  
        """
        self.user_data[user_id] = value

        self.user_data_is_modified = True
