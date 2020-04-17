#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: MIT

import pihole as ph
from papirus import PapirusTextPos
import configparser

# set up text writer
text = PapirusTextPos(autoUpdate=False)
fontPath = '/usr/share/fonts/opentype/b612/B612-Regular.otf'

# authenticate with the given password
config = configparser.ConfigParser()
config.read('secrets.ini')
pihole = ph.PiHole('localhost')
pihole.authenticate(config['pihole']['password'])

# get top 5 sites
pihole.refresh()
pihole.refreshTop(5)

# display counts
ads = pihole.top_ads
msg = []
for host in ads.keys():
    msg.append(f'{ads[host]:4d} {host}')
    
text.AddText('\n'.join(msg),size=10,fontPath=fontPath)
text.WriteAll()