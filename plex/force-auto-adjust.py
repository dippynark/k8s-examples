import os
import time
from plexapi.myplex import MyPlexAccount

plex_email_address = ""
plex_password = ""
plex_server_name = "Dippystreams"

account = MyPlexAccount(plex_email_address, plex_password)
plex = account.resource(plex_server_name).connect()

forceAutoAdjustQuality = plex.settings.get("forceAutoAdjustQuality")
if not forceAutoAdjustQuality.value:
  forceAutoAdjustQuality.set(True)
  plex.settings.save()
print(forceAutoAdjustQuality.value)
