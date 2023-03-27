import asyncio
import hashlib
import multiprocessing
import os
import git


url = 'https://gitea.radium.group/radium/project-configuration.git'
your_path = '/Users/danyanara/PycharmProjects/Test_Bakcend/repo'


def download_file(url, your_path):
    repo = git.Repo.clone_from(url, your_path, branch="master")
    files = repo.git.ls_files().split()

    return files


async def remove_repo(your_path):
    os.system(f'rm -rf {your_path}')


def main():
    with multiprocessing.Pool(3) as pool:
        result = pool.apply(download_file, args=(url, your_path))
    pool.close()
    pool.join()
    for file in result:
        filename = f'repo/{file}'
        with open(filename, 'rb') as f:
            file_content = f.read()
            h = hashlib.sha256(file_content).hexdigest()
            print(f'{filename}: {h}')
    asyncio.run(remove_repo(your_path=your_path))


if __name__ == '__main__':
    main()

