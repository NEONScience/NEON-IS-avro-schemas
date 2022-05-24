#requirements
# python 3.6.8
# pip3 install python-pachyderm
# pip3 install certifi


import python_pachyderm
import io
import os

print('Hello, the current working directory is:')
print(os.getcwd())

config = '''{
  "v2": {
    "active_context": "pachd1sandbox",
    "contexts": {
      "pachd1sandbox": {
        "pachd_address": "grpcs://pachd1.sandbox.gcp.neoninternal.org:30650",
        "cluster_deployment_id": "49fGuUbnKSwAee8Pdyfx2AEFnyUaZrK3"
      }
    }
  }
}'''
client = python_pachyderm.Client.new_from_config(io.StringIO(config))

# Put the updated files in Git into Pachyderm
# Similar to `pachctl put file empty_files_test@master:/dir_a/data.txt`
with client.commit("empty_files_test", "master") as commit:
        python_pachyderm.put_files(client, "empty_files/prt/", commit, "/prt/")

