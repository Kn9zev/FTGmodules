# -*- coding: utf-8 -*-

# Module author: @vova_knyazev

import requests

from .. import loader, utils


@loader.tds
class VidalMod(loader.Module):
    """Поиск препарата и его описания по справочнику Видаля (vidal.ru) v0.1a / by Vova Knyazev"""
    strings = {"name": "VidalInfo"}

    async def vicmd(self, m):
        """.vi <препарат>"""
        lek = utils.get_args_raw(m).replace(" ", "%20")
        user_agent = {'User-agent': 'Mozilla/5.0'}
        r = requests.get("https://q-design.ru/vidal/?lek=" + lek, headers=user_agent)

        await utils.answer(m, r.text)
