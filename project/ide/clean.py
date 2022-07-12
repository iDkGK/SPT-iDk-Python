import os
import shutil

cwd = os.getcwd()
builddir = '\\'.join([cwd, 'build'])
distdir = '\\'.join([cwd, 'dist'])
userdir = '\\'.join([cwd, 'user'])
specfile = '\\'.join([cwd, 'Server.spec'])

def cleanup():
    if (os.path.exists(builddir)):
        shutil.rmtree(builddir)
    if (os.path.exists(distdir)):
        shutil.rmtree(distdir)
    if (os.path.exists(userdir)):
        os.remove(userdir)
    if (os.path.exists(specfile)):
        os.remove(specfile)

cleanup()