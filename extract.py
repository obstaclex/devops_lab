import os
import zipfile
import tempfile
import argparse
import logging
import shutil
import sys


parser = argparse.ArgumentParser()
parser.add_argument('-n', dest="name", help="Zip archive name", type=str)
args = parser.parse_args()


logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s - %(levelname)s - %(message)s', filename='log.txt')


try:
    with zipfile.ZipFile(args.name, 'r') as zf:
        tmpdir = tempfile.mkdtemp()
        zf.extractall(tmpdir)
        logging.debug(f'Temporary dir was created: {tmpdir}')
        logging.debug(f'{args.name} extracted in {tmpdir}')
except Exception as err:
    logging.error(err)
    sys.exit(1)


# Remove directory without __init__.py
for dirpath, dirnames, filenames in os.walk(tmpdir):
    if "__init__.py" not in filenames and args.name.replace(".zip", "") not in dirnames:
        shutil.rmtree(dirpath)
        logging.debug(f'Directory {dirpath} not contain required file and deleted')


# Create new archive
with zipfile.ZipFile(args.name.replace(".zip", "_new.zip"), "w") as zf:
    for dirpath, dirnames, filenames in os.walk(tmpdir):
        for file in filenames:
            filepath = os.path.join(dirpath, file)
            lentmpdir = len(tmpdir)
            zf.write(filepath, filepath[lentmpdir:])
            logging.debug(
                f'File {filepath[lentmpdir:]} added in {args.name.replace(".zip", "_new.zip")}')
