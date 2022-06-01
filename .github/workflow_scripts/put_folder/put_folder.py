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
    pach_url = urlparse(os.environ["PACHYDERM_CLUSTER_URL"])
    host = pach_url.hostname
    port = pach_url.port
    if port is None:
        port = 80
    if pach_url.scheme == "https":
        tls = True
    else:
        tls = False
    return python_pachyderm.Client(host=host, port=port, tls=tls)



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


