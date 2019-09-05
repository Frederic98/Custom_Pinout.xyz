#!/usr/bin/env python
import os
import shutil
import subprocess
import sys

reload(sys)
sys.setdefaultencoding('utf8')

CUSTOM_REPO = os.environ.get('BOARDS_URL', None)
CUSTOM_REPO_DIR = '/usr/share/pinout.custom'
REPO_DIR = '/usr/share/Pinout.xyz'
os.chdir(REPO_DIR)

if CUSTOM_REPO is not None:
    sys.path.append(REPO_DIR)
    import markjaml

    OVERLAY_DIR = 'src/en/overlay'
    overlays = [os.path.join(OVERLAY_DIR, f) for f in os.listdir(OVERLAY_DIR)]

    devnull = open(os.devnull, 'w')

    print('Removing boards...')
    for overlay in overlays:
        data = markjaml.load(overlay)['data']
        if data['class'] != 'interface':
            name = os.path.basename(overlay).split('.', 1)[0]
            cmd = '{}/draft/unpublish.sh {}'.format(REPO_DIR, name)
            subprocess.call(cmd, shell=True, stdout=devnull, stderr=subprocess.STDOUT)

    print('Adding boards...')
    subprocess.call(['git', 'clone', CUSTOM_REPO, CUSTOM_REPO_DIR])
    shutil.rmtree('draft/boards')
    shutil.rmtree('draft/overlay')
    shutil.copytree(os.path.join(CUSTOM_REPO_DIR, 'boards'), 'draft/boards')
    shutil.copytree(os.path.join(CUSTOM_REPO_DIR, 'overlay'), 'draft/overlay')

    for overlay in os.listdir('draft/overlay'):
        name = overlay.split('.', 1)[0]
        cmd = '{}/draft/publish.sh {}'.format(REPO_DIR, name)
        subprocess.call(cmd, shell=True, stdout=devnull, stderr=subprocess.STDOUT)

subprocess.call(['make', 'serve'])
