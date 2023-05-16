
from git import Repo

git_url = 'ssh://git@gitlab.tamk.cloud:1022/server-tech-2023-a-petteri-jekunen/cmdb-stec23-petteri.git'
repo_dir = 'tmp-git-repo'

Repo.clone_from(git_url, repo_dir)