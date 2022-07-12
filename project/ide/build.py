import os
import shutil
import subprocess

cwd = os.getcwd()
resdir = '\\'.join([cwd, 'assets'])
builddir = '\\'.join([cwd, 'build'])
distdir = '\\'.join([cwd, 'dist'])
datadir = '\\'.join([builddir, 'Aki_Data\\Server'])
userdir = '\\'.join([cwd, 'user'])
specfile = '\\'.join([cwd, 'Server.spec'])
pyiexecfile = '\\'.join([cwd, '.venv\\Scripts\\pyinstaller'])
srcfile = '\\'.join([cwd, 'src\\server.py'])
icofile = '\\'.join([cwd, 'assets\images\icon.ico'])

def cleanup():
    if (os.path.exists(builddir)):
        shutil.rmtree(builddir)
    if (os.path.exists(userdir)):
        os.remove(userdir)
    if (os.path.exists(specfile)):
        os.remove(specfile)

def compile():
    os.system(' '.join([pyiexecfile, '-F', srcfile, '-n', 'Server', '-i', icofile]))

def rename():
    if (os.path.exists(distdir)):
        os.rename(distdir, builddir)

def copy():
    shutil.copytree('assets', datadir)

cleanup()
compile()
cleanup()
rename()
copy()