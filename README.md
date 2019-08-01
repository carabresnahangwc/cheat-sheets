# cheat-sheets

## Using GitHub in Atom Text Editor

### Add changes to git
1. Click on the Git icon in the lower right hand corner.
2. Under the Unstaged Changes, select the files you want to update in git and hit ENTER key. Your file should now appear under Staged Changes.
3. In the text box that says Commit message, type the reason for the commit/what changes in the files you made.
4. Click on Commit to master button.
5. At the bottom of the window, click on the up arrow that says Pull (near the Git icon from step 1)

### Get changes from git
1. Click on the Pull icon in the lower right hand corner. 

## Basic Git Commands for Terminal

- git clone [url]: copy repository
- git status: show status of files in repository

### Add changes to git
1. Navigate to the project folder/repository
2. Type in ```git status``` to see the files changed
3. Use ```git add [filename]``` to add each file one by one and prepare file for next commit
4. Commit your changes as seen below, replace commit message with a short description of the files changed
``git commit -m "[commit message]" ``
5. Type in ```git push``` to update files with changes from commit

### Get changes from git
- git pull: get changes and update local repository

https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf
