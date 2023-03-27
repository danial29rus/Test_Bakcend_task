import hashlib

import os

from app.main import download_file, main, remove_repo


url = 'https://gitea.radium.group/radium/project-configuration.git'
your_path = '/Users/danyanara/PycharmProjects/Test_Bakcend/repo'


def test_download_file():
    result = download_file(url, your_path)
    for file in result:
        filename = f'repo/{file}'
        with open(filename, 'rb') as f:
            file_content = f.read()
            h = hashlib.sha256(file_content).hexdigest()
    assert len(h) == 64
    assert isinstance(result, list)
    assert len(result) > 0
    assert os.path.isdir(your_path)
    remove_repo(your_path)










