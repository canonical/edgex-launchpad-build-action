import os
from launchpadlib.launchpad import Launchpad

consumer_name = os.environ['CONSUMER_NAME']  # aka. consumer key
access_token = os.environ['ACCESS_TOKEN']
access_secret = os.environ['ACCESS_SECRET']
snap_name = os.environ['SNAP_NAME']
arch = os.environ['ARCH']

ubuntu_series = os.getenv('UBUNTU_SERIES')
# default to Ubuntu 20.04 (Focal)
if not ubuntu_series:
    ubuntu_series = "20.04"
    print("Ubuntu Series not set, will use: {0}".format(ubuntu_series))

launchpad = Launchpad.login(consumer_name, access_token, access_secret,
                            service_root='production', version='devel')

ubuntu = launchpad.distributions["ubuntu"]
release = ubuntu.getSeries(name_or_version=ubuntu_series)
arch = release.getDistroArchSeries(archtag=arch)

snap = launchpad.snaps.getByName(name=snap_name,
                                 owner=launchpad.people["canonical-edgex"])

request = snap.requestBuild(archive=ubuntu.main_archive,
                            distro_arch_series=arch,
                            pocket='Updates',
                            channels={"snapcraft": "latest/stable"})  # launchpad uses latest/stable/launchpad-buildd channel by default

print("Build request has been submitted: {0}".format(request))
