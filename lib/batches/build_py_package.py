"""
package builder script

Whow! Batch files are such a pain. Petter keep them as short as possible.
"""
import os
import shutil
import compileall
from os.path import join, dirname, abspath, isfile


a2path = abspath(join(dirname(__file__), '..', '..'))
distpath = join(a2path, '_ package')
print('distpath: %s' % distpath)
distui = join(distpath, 'ui')
os.rename(join(distpath, 'a2app'), distui)
print('copying root files ...')

for item in os.listdir(a2path):
    if item in ['a2_init.ahk', 'a2_settings.ahk']:
        continue
    path = join(a2path, item)
    if isfile(path):
        if item.endswith('.ahk') or item.endswith('.exe')or item in ['LICENSE']:
            shutil.copy2(path, distpath)


print('copying lib files ...')
distlib = join(distpath, 'lib')
a2lib = join(a2path, 'lib')
os.mkdir(distlib)
for item in os.listdir(a2lib):
    if item == 'batches':
        continue

    path = join(a2lib, item)
    if isfile(path):
        if item.endswith('.ahk'):
            shutil.copy2(path, distlib)
    else:
        shutil.copytree(path, join(distlib, item))

print('copying ui files ...')
a2uipath = join(a2path, 'ui')
def ui_ignore(path, items):
    if path.endswith('\\siding'):
        return ['docs', 'examples']
    else:
        return [f for f in items if f.endswith('.ui')] + ['__pycache__', 'demo', 'work']
for folder in ['a2ctrl', 'a2widget', 'a2element', 'siding', 'res']:
    shutil.copytree(join(a2uipath, folder), join(distui, folder), ignore=ui_ignore)

for folder in ['examples', 'docs', 'include', 'translations']:
    shutil.rmtree(join(distui, 'PySide', folder), ignore_errors=True)

#compileall
