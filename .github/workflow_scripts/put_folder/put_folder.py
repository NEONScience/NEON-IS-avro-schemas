#requirements
# python 3.6.8
# pip install python-pachyderm
# pip install certifi


import python_pachyderm
from urllib.parse import urlparse
import io
import os
def setup_client():
    pachd_address = os.environ["PACHD_ADDRESS"]
    return python_pachyderm.Client.new_from_pachd_address(pachd_address)


def main():
    repo = os.environ["REPO"] # The Pachyderm repo (e.g. "empty_files_prt")
    branch = os.environ["BRANCH"] # The branch of the pachyderm repo (e.g. "master")
    in_path = os.environ["IN_PATH"] # The local path to the folder that will be uploaded into pachyderm (e.g. "empty_files/prt"")
    out_path = os.environ["OUT_PATH"] # The path where the folder will be placed in the pachydemr repo (e.g. "prt")
    # Setup connection to Pachyderm
    client = setup_client()
    # Put the updated files in Git into Pachyderm
    with client.commit(repo, branch) as commit:
            python_pachyderm.put_files(client, in_path, commit, out_path)
    

if __name__ == "__main__":
    main()


