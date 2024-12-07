#"Git Clone" = copies remote repo to local computer
    ex git clone https://github.com/whatever/.git 

#Commits are a working snapshot of what I am working on. 
#Commit stages are 
    working - changes that you are working on locally  project/
    staging - the "git add" command = are files you want committed.   project/.git/index 
        ex. git add filename.txt
    Commit - when the changes have been moved to github project/.git/object

#each commit becomes my repo history in github

#"git status" = i can check the status of the repo

#"git commit -m "message i want to add"
#"git commit --amend -m "the new (-m)message i want to send"  this amends the old message with the new message
"git commit -a" commits (-a)all the modified and deleted files
    ex. git commit -a -m "i had fun" = this would add all the changes and add the message "i had fun"

WIP = work in progress

"git revert (whatever the commit is)" = reverts the commit like a undo button
"git revert HEAD~2(2 represents how many commits behind the head commit)"  reverts the 2(represents how many commits behind the head commit) so Head~3 would be 3 commit behind the head commit on the current checked out branch

"git revert main~2" is 2 commits behind the head commit on the main branch

in the gitkraken cli "git revert" command will automatically prompt a change you message  if i dont want to change my message and can use "git revert --no-edit" to keep the same message

if i want to revert multiple commits.  older commit should come first 
ex. git revert HEAD~5..HEAD~2
this will revert these two commits plus every commit between them

if i need to make additional code changes before i undo the git commit, i will use the -n flag (i can also use --no-commit)
ex. "git revert -n 45111a"   45111a is ticket number

git revert philosophy 
    the git revert command introduces a new commit that its sole purpose is to undo the changes of a targeted commit. which means that the existing commit history prior to the newly added "undo" commit including the original error commit is preserved

    git init   initialize git
    git add (file name)
    git commit -m "what ever the message" (has to have a message) commits the file
    git branch -M main  
    git remote add origin "https://github.com/username/whateveryourreponameis.git"
    git push -u main  pushes the files to the repo

    git status  give you the status of your git

    git config --global user.name "your user name"  sets your github user name
    git config --global user.email "your email"     sets your github email 
    
    git reset --hard   clears your uncommitted files




