# installer for the weewx-sdr driver
# Copyright 2016-2021 Matthew Wall
# Distributed under the terms of the GNU Public License (GPLv3)

from weecfg.extension import ExtensionInstaller

def loader():
    return SDRInstaller()

class SDRInstaller(ExtensionInstaller):
    def __init__(self):
        super(SDRInstaller, self).__init__(
            version="0.85",
            name='sdr',
            description='Capture data from rtl_433',
            author="Matthew Wall",
            author_email="mwall@users.sourceforge.net",
            files=[('bin/user', ['bin/user/sdr.py'])]
            )
