

class InvalidKeyException(Exception):

    def __init__(self, key_name, model_name, allowed_fields):
        """Constructs InvalidKeyException.

        :precondition: key_name must be a string containing the name of the key that was invalid.

        :precondition: model_name is the string of the data-type this exception will refer to

        :precondition: allowed_fields must be a list of strings that represent the field names for this model

        :return: InvalidKeyException
        """
        self.key_name = key_name
        self.allowed_fields = allowed_fields
        self.model_name = model_name
        super().__init__(self)


class NoCampaignSelectedError(Exception):
    """This error is for when a user doesn't select a campaign. """
    def __init__(self):
        super().__init__(self)
