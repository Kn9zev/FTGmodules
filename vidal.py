# -*- coding: utf-8 -*-

# Module author: @vova_knyazev

import requests

from .. import loader, utils


@loader.tds
class VidalMod(loader.Module):
    """Поиск препарата и его описания по справочнику Видаля (vidal.ru) v0.2alpha / by Vova Knyazev"""
    strings = {"name": "VidalInfo"}

    async def vicmd(self, m):
        """.vi <препарат>"""
        lek = utils.get_args_raw(m).replace(" ", "%20")
        user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
        r = requests.get("https://kn9zev.site/vidal/?lek=" + lek, headers=user_agent)

        await utils.answer(m, r.text)
