import sys
sys.path.append('.')

import os

from utilities import utilities
from releases import releases
from config import config
from manager import manager

class update(object):

    @classmethod
    def fetch(cls):
        logging_helper.getLogger().info('Updating package data...')

        hashes_plist_url = os.path.join(config.getUpdateURL(), 'hashes.plist')
        hashes_plist_path = utilities.getlookupplistpath('hashes')
        manager.DownloadFileFromURLToPath(hashes_plist_url, hashes_plist_path)

        release_plist_url = os.path.join(config.getUpdateURL(), 'releases.plist')
        release_plist_path = utilities.getreleaseplistpath()
        manager.DownloadFileFromURLToPath(release_plist_url, release_plist_path)
        if os.path.exists(release_plist_path) == True:
            for release_type in releases.get():
                release_type_plist_url = os.path.join(config.getUpdateURL(), release_type+'.plist')
                release_type_plist_path = utilities.getlookupplistpath(release_type)
                manager.DownloadFileFromURLToPath(release_type_plist_url, release_type_plist_path)
