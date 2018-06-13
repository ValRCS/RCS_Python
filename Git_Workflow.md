## Start using the repo run in terminal: 
*git clone https://github.com/ValRCS/RCS_Python.git*
* clones whole repo in the current working directory from which you run git clone

* git log shows revision history with SHA1 hash value for each revision

## Update automagically original repo: *git pull* from the same directory
* git pull is like two commands into one
* git fetch + git merge pulls changes from default origin(this repo) into your local repo and merges them 

## Edit/Move Files in local clone from command line terminal
* git status for status
* git add . from project root to stage changes
* git status to make sure
* git commmit -m "My helpful commit message" to commmit **locally**
* git push origin to push back to master repo (Github will ask to login and pw if no SSH set)

## If you want to work on specific revision
* git clone URL 
* cd to Projectdirectory
* git reset --hard SHA1 where SHA1 is SHA1 of the revision you want


### Various workflows: https://www.atlassian.com/git/tutorials/comparing-workflows


