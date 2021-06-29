# from commands.error_handler import handle_errors

# """Wrapper functions for DMManager so errors can be transmitted to discord."""
# from . error_handler import handle_errors
# from dm_manager import DMManager


# @handle_errors
# async def camp(ctx, manager: DMManager, key: str, value: str = None):
#     """Wrapper function for camp function."""
#     print('key = ', key, value)
#     manager.camp(key, value)


# @handle_errors
# async def add_camp(ctx, manager: DMManager, campaign_name: str, desc: str = None):
#     """Wrapper function for add_camp function.
    
#     :param ctx: Discord Context
#     :param manager: DMManager Object
#     :param campaign_name: string
#     :param desc: string
#     """
#     manager.add_camp(campaign_name, desc=desc)
