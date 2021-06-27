"""Contains miscellaneous utility functions """



def get_user_id(member):
    """Extract user-id from Member Object."""
    
    return member.author.id
