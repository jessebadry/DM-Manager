"""Simple module to serialize/deserialize JSON for DM data.

    This module acts as a wrapper around a dictionary to create 


"""

import json
from exceptions import InvalidKeyException, NoCampaignSelectedError

CAMPAIGN_FIELDS = ("desc", "recap", "members")
USER_DATA_FIELDS = ("selected_campaign", "campaigns", "members")


def dict_from_keys(keys):
    """Initializes dict with None for each key inside `keys` iterable.

    :param keys: any string iterable
    :return: dict
    """
    return {key: None for key in keys}


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
        self.user_data = None
        self.load_user_data()

    def get_campaigns(self):
        """Returns DM-Managers dictionary of campaigns.

        :return: dict of campaign dictionaries
        """

        return self.user_data['campaigns']

    def current_campaign(self):
        """Returns the currently selected campaign object."""

        return self.get_campaigns()[self.user_data['selected_campaign']]

    def camp(self, key, value=None):
        """Get or set a field in the current campaign within user_data.


         :precondition: `key` cannot be None or empty
         :postcondition: if value is None, return the string that belongs to `key` 
         :postcondition: if value is string,set `key` to this value for the campaign data

         :return: string or None
         :raises DMError: if `key` is not a valid campaign field name

         >>> manager = DMManager('data.json')
         >>> manager.camp('desc', 'The first tale of our epic adventure')
         >>> manager.camp('desc')
         'The first tale of our epic adventure'

        """

        if not self.user_data['selected_campaign']:
            raise NoCampaignSelectedError()

        elif key not in CAMPAIGN_FIELDS:
            raise InvalidKeyException(key, 'campaign', CAMPAIGN_FIELDS)

        if value is None:

            return self.current_campaign()[key]
        else:

            self.current_campaign()[key] = value
            self.user_data_is_modified = True

    def add_camp(self, campaign_name, desc=''):
        """Adds campaign to the DM-Manager object.

        :postcondition: if no campaign is selected on creation, 
        the newly added campaign will be set as the selected campaign

        #TODO raise exception if the campaign being added already exists, will most 
        likely need a custom exception

        """

        campaigns = self.get_campaigns() or {}

        if self.user_data['selected_campaign'] is None:
            self.user_data['selected_campaign'] = campaign_name

        new_campaign = dict_from_keys(CAMPAIGN_FIELDS)
        new_campaign.update({'desc': desc})

        campaigns[campaign_name] = new_campaign

        self.user_data['campaigns'] = campaigns

        self.save()

    def add_member(user, character_name):
        """Adds character to the currently selected campaign.
d
        :param user: Discord User
        :param character_name: string 30 char limit

        :precondition: user must not be None
        :precondition: length of character_name <= 30
        """
        pass

    def load_user_data(self):
        """Deserializes user-ata to json and saves to `self.file_name`."""

        try:

            with open(self.file_name, 'r') as f:
                self.user_data = json.load(f)

        except FileNotFoundError:
            self.user_data = dict_from_keys(USER_DATA_FIELDS)
            self.save()

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


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
