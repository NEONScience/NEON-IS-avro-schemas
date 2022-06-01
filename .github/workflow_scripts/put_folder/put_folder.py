#requirements
# python 3.6.8
# pip install python-pachyderm
# pip install certifi


import python_pachyderm
from urllib.parse import urlparse
import io
import os

print('Hello, the current working directory is:')
print(os.getcwd())


def setup_client():
    pachd_address = os.environ["PACHD_ADDRESS"]
    return python_pachyderm.Client.new_from_pachd_address(pachd_address)


def main():
    repo = os.environ["REPO"]
    branch = os.environ["BRANCH"]
    in_path = os.environ["IN_PATH"]
    out_path = os.environ["OUT_PATH"]
    # Setup connection to Pachyderm
    client = setup_client()
    # Put the updated files in Git into Pachyderm
    with client.commit(repo, branch) as commit:
            python_pachyderm.put_files(client, in_path, commit, out_path)
    

if __name__ == "__main__":
    main()


