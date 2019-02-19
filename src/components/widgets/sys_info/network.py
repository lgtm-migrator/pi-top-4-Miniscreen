#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014-18 Richard Hull and contributors
# See LICENSE.rst for details.

from ptcommon.formatting import bytes2human
import psutil
from components.widgets.common_functions import right_text, title_text, tiny_font
from components.widgets.common.base_widget_hotspot import BaseHotspot


class Hotspot(BaseHotspot):
    def __init__(self, width, height, interval, **data):
        super(Hotspot, self).__init__(width, height, interval, self.render)

        self.interface = data.get("interface")

    def render(self, draw, width, height):
        margin = 3
        title_text(draw, margin, width, text="Net:{0}".format(self.interface))
        try:
            address = psutil.net_if_addrs()[self.interface][0].address
            counters = psutil.net_io_counters(pernic=True)[self.interface]

            draw.text((margin, 20), text=address, font=tiny_font, fill="white")
            draw.text((margin, 35), text="Rx:", font=tiny_font, fill="white")
            draw.text((margin, 45), text="Tx:", font=tiny_font, fill="white")

            right_text(draw, 35, width, margin, text=bytes2human(counters.bytes_recv))
            right_text(draw, 45, width, margin, text=bytes2human(counters.bytes_sent))
        except:
            draw.text((margin, 20), text="n/a", font=tiny_font, fill="white")
