# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Thanks to the Authors of the base code
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# modified by: ximix
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.xiMix'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "PLjfOXikiCHxbNnE7REQWECKMi_nSgaNVl" 	# Top Hitet Shqip
YOUTUBE_CHANNEL_ID_2 = "UC7bX_RrH3zbdp5V4j5umGgw" 		# Relax Musik
YOUTUBE_CHANNEL_ID_3 = "PLvHNYTx1DepULhTDpLvwLrSNiQIA7tx5z" 	# O Sa Mir
YOUTUBE_CHANNEL_ID_10 = "digitalb" 	                        # DigitAlb
YOUTUBE_CHANNEL_ID_4 = "PL2ygqgSFvmrpsQ7AV0TC1l16RO5YsyFdb" 	# Çka ka Shpija
YOUTUBE_CHANNEL_ID_5 = "PL9c8GLaNaMYjmF3_jjFf2VSiFREDS58D9" 	# Filma Shqip
YOUTUBE_CHANNEL_ID_6 = "VEVO" 	       				# VEVO
YOUTUBE_CHANNEL_ID_7 = "ArkivaShqip" 	                        # ArkivaShqip
YOUTUBE_CHANNEL_ID_8 = "jazznbluesexperience" 	                # Jazz and Blues
YOUTUBE_CHANNEL_ID_9 = "UC-TisQC3PTaqdFV6FGc-pQg" 	        # doku deutch
YOUTUBE_CHANNEL_ID_11 = "UCk5x1qwIX-CejQRfSAE3h8w" 	        # n'Kosove  Show

# Entry point
def run():
    plugintools.log("docu.run")

    # Get params
    params = plugintools.get_params()

    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"

    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item(
        #action="",
        title="Top Hitet Shqip",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://yt3.ggpht.com/a-/AAuE7mCHlokFKDfGN8x1W32TlWmp3umfC6-X3Tii1w=s288-mo-c-c0xffffffff-rj-k-no",
		fanart="",
        folder=True )

    plugintools.add_item(
        #action="",
        title="Relax Musik",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://yt3.ggpht.com/a-/AAuE7mDKuihCdUyXxcRfA0V1p5KZQ0fAkaQZyJ4JJA=s288-mo-c-c0xffffffff-rj-k-no",
		fanart="",
        folder=True )

    plugintools.add_item(
        #action="",
        title="O Sa Mir",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://yt3.ggpht.com/a-/AAuE7mANc4uWkepW5e24Z_UgSu6GjW79HNLqTkqj=s288-mo-c-c0xffffffff-rj-k-no",
		fanart="",
        folder=True )

    plugintools.add_item(
        #action="",
        title="DigitAlb",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="https://yt3.ggpht.com/a-/AAuE7mAT6ceLGjmMnwBHLTEVif9ycNV5wLl6C1dYgQ=s288-mo-c-c0xffffffff-rj-k-no",
		fanart="",
        folder=True )

    plugintools.add_item(
        #action="",
        title="n'Kosove Show",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://yt3.ggpht.com/a/AGF-l78rsykupQ1NP12TioS1cAcLbMdldzPWN5XJ0Q=s288-mo-c-c0xffffffff-rj-k-no",
		fanart="",
        folder=True )

    plugintools.add_item(
        #action="",
        title="Çka ka Shpija",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://yt3.ggpht.com/a-/AAuE7mDzDkiJRPEuHtk6Ws1jyLcfJj-QJGcau5YT4g=s288-mo-c-c0xffffffff-rj-k-no",
		fanart="",
        folder=True )

    plugintools.add_item(
            #action="",
            title="Filma Shqip",
            url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
            thumbnail="https://yt3.ggpht.com/a-/AAuE7mB0IYluo1vs9mJkNSOIs3_fcU5lpwCaMdMz1w=s288-mo-c-c0xffffffff-rj-k-no",
    		fanart="",
            folder=True )

    plugintools.add_item(
            #action="",
            title="VEVO",
            url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_6+"/",
            thumbnail="https://yt3.ggpht.com/a-/AAuE7mANv-dE05bxW3mFWr1lrq_eruFEaUbN2JCGSw=s288-mo-c-c0xffffffff-rj-k-no",
    		fanart="",
            folder=True )

    plugintools.add_item(
            #action="",
            title="ArkivaShqip",
            url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_7+"/",
            thumbnail="https://yt3.ggpht.com/a-/AAuE7mAp1-innFTSbdD2b_DhpBRSisbtCmFEApH-gQ=s288-mo-c-c0xffffffff-rj-k-no",
    		fanart="",
            folder=True )

    plugintools.add_item(
            #action="",
            title="Jazz and Blues",
            url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_ID_8+"/",
            thumbnail="https://yt3.ggpht.com/a-/AAuE7mBAhM7LbybXVnGxxl0sz6IATIN10dDByN8-7Q=s288-mo-c-c0xffffffff-rj-k-no",
    		fanart="",
            folder=True )

    plugintools.add_item(
            #action="",
            title="Jantzonmai Doku",
            url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_9+"/",
            thumbnail="https://yt3.ggpht.com/a-/AAuE7mDju3hP0etmQhz1kKmUDlAEq_0hkhY8inyKMw=s288-mo-c-c0xffffffff-rj-k-no",
    		fanart="",
            folder=True )


run()
