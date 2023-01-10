# -*- coding: utf-8 -*-

# Module author: @vova_knyazev

import requests

from .. import loader, utils


@loader.tds
class VidalMod(loader.Module):
    """Поиск препарата и его описания по справочнику Видаля (vidal.ru) / by Knyazev"""
    strings = {"name": "VidalInfo"}

    async def vicmd(self, m):
        """.vi <препарат>"""
        lek = utils.get_args_raw(m).replace(" ", "%20")
        r = requests.get("https://knyazev.xyz/vidal/?lek=" + lek, headers={
"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36")
        r.close()

        await utils.answer(m, r.text)
