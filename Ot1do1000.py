__version__ = (1, 0, 0)

# ---------------------------------------------------------------------------------

# ( o.o )  🔓 Not licensed.

# ---------------------------------------------------------------------------------

# Commands:

# meta developer: @its_xuxanneynl

# scope: hikka_only

# ---------------------------------------------------------------------------------

from .. import loader, utils

from ..utils import answer

import asyncio 

@loader.tds

class NumbersMod(loader.Module):

    """Sends numbers from {number1} to {number2} in separate messages"""

    strings = {"name": "Numbers"}

    @loader.unrestricted

    @loader.command("numbers")

    async def numberscmd(self, message):

        """ {delay} {number1} {number2}"""

        args = utils.get_args(message)

        if len(args) != 3:

            await answer(message, "Invalid arguments. Usage: .numbers {delay} {number1} {number2}")

            return

        try:

            delay = float(args[0])

            number1 = int(args[1])

            number2 = int(args[2])

        except ValueError:

            await answer(message, "Invalid arguments. Usage: .numbers {delay} {number1} {number2}")

            return

        if number1 > number2:

            await answer(message, "Invalid arguments. number1 should be less than or equal to number2.")

            return

        for i in range(number1, number2 + 1):

            await message.client.send_message(message.to_id, str(i), reply_to=message.reply_to_msg_id)

            await asyncio.sleep(delay)

        await answer(message, "Done!")
