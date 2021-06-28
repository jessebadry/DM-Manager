__all__ = ['init_add']

from . error_handler import handle_errors



@handle_errors
async def init_add(context, number_message, dm_manager):
    raise NotImplementedError()
    user_id = utils.get_user_id(context)
    current_campaign = dm_manager.get_campaign()

    dm_manager.add_init(int(number_message))
