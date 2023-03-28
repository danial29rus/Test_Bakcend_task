import asyncio
import hashlib
import multiprocessing
import shutil
import tempfile

import git

def download_file(url, your_path):
    repo = git.Repo.clone_from(url, your_path, branch="master")
    files = repo.git.ls_files().split()

    return files

async def hash_file(url, your_path):
        result = download_file(url, your_path)

        for file in result:
            filename = f"{your_path}/{file}"
            with open(filename, "rb") as f:
                file_content = f.read()
                h = hashlib.sha256(file_content).hexdigest()
                print(f"{filename}: {h}")

        await remove_repo(your_path)
        return result


async def remove_repo(repo_path):
    shutil.rmtree(repo_path)


def main():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(hash_file(url, your_path))
    except DeprecationWarning:
        pass

    finally:
        loop.close()



if __name__ == "__main__":
    url = "https://gitea.radium.group/radium/project-configuration.git"
    your_path = '/Users/danyanara/PycharmProjects/Test_Bakcend/repo'

    main()