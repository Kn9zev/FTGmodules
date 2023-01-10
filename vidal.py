# -*- coding: utf-8 -*-

# Module author: @vova_knyazev

import requests

from .. import loader, utils


@loader.tds
class VidalMod(loader.Module):
    """Vidal Поиск препарата"""
    strings = {"name": "VidalMod"}

    async def wcmd(self, m):
        """.vi <препарат>"""
        lek = utils.get_args_raw(m).replace(" ", "%20")
        r = requests.get("https://www.vidal.ru/search?q=" + lek + "&bad=on")

        await utils.answer(m, r.text)
