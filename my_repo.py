from os.path import exists
from git import Repo

# What are my attributes:
# - repo name (email alias)
# - existed already
# - changed or not

root_dir = 'clonedir'

class MyRepo:
    def __init__(self, name='tmpurl', cloneurl = 'notworksurl') -> None:
        if (name):
            self.name = name        
        if (cloneurl):
            self.cloneurl = cloneurl
        self.new_repo = False
        self.repo_changed = False
        self.repodir = root_dir + '/' + name        
        pass    
    
    def getSomeId(self):
        return self.some_id
    
    def localExists(self):
        if (exists(self.repodir)):
            print("Dir exists: ", self.repodir)
            self.new_repo = True
            return True
        return False
    
    def clone(self):
        print("Cloning for ",self.name, " the url ", self.cloneurl)
        Repo.clone_from(self.cloneurl, self.repodir)

    def pull(self):
        repo = Repo(self.repodir)
        self.current = repo.head.commit
        repo.remotes.origin.pull()
        if self.current != repo.head.commit:
            self.repo_changed = True
            print("It changed - ", self.name)

    def summarize(self):
        print ("REPO: ", self.name, "NEW: ", self.new_repo, "CHANGED: ", self.repo_changed)
