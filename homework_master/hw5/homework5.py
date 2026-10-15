"""
2.1 

Git vs. Github
Git is a version control system that allows developers to track changes in their codebase, collaborate with others, and manage different versions of their projects. It is a command-line tool that can be used locally on a developer's machine. 
Git Hub is a web-based platform that provides hosting for Git repositories, along with additional features such as issue tracking, project management, and collaboration tools. 

Terminal vs. Command Line
The terminal is a text-based interface that allows users to interact with their computer's operating system. 
The command line is a specific interface within the terminal that allows users to enter commands and receive text

Local vs. Remote Repositories
A local repository is a copy of a Git repository that is stored on a developer's local machine
A remote repository is a copy of a Git repository that is stored on a remote server, such as GitHub.

Version Control
Version control is a system that allows developers to track changes to their codebase over time and collaborate.

Staging Area
The staging area is a place where developers can prepare changes to be committed to the repository.

git add
The git add command is used to add changes to the staging area in Git.

git commit
The git commit command is used to save changes to the local repository in Git.

git push
The git push command is used to upload changes from the local repository to a remote repository in Git

git status
The git status command is used to display the current state of the repository, including which files have been modified, added, or deleted.

git pull
The git pull command is used to fetch and merge changes from a remote repository into the local repository

pwd
The pwd command is used to display the current working directory in the terminal.

ls
The ls command is used to list the files and directories in the current working directory in the terminal.

cd
The cd command is used to change the current working directory in the terminal.

nano
The nano command is used to open the nano text editor in the terminal, which allows users to create and edit text files.

touch
The touch command is used to create a new empty file in the terminal.

mv
The mv command is used to move or rename files and directories in the terminal.

rm
The rm command is used to remove files and directories in the terminal.

cat
The cat command is used to display the contents of a file in the terminal.

"""

"""
2.2

pwd will tell me what current working directory I am in.
ls will list the files and directories in the current working directory.
first use cd to change the current working directory to the brianna repository folder, then use git pull. 
us mv command. mv homework.py python_decal/judy_decal/homework
cd python_decal/judy_decal/homework
navigage to homework.py and use cat homeowork.py to display the contents of the file in the terminal. 
to save changes and push to remote repository, use git add homework.py, then git commit -m "Finish this week's homework", then git push.
the error means that Judy's local repositroy is out of sync with the remote repositroy on GitHub. She was likely on someone else's computer. She needs to itegrate the remote changes into her local homework file befoer she can push. She should run 'git pull origin main'.
to move to recents, she should use 'cd ~/Recent' 
"""

"""
2.3 

the png is in the hw5 folder 
/Users/lilly/Python DeCal/homework_master/hw5/homework5.py
"""

# 3.1
def checkDataType(input_data):
    return type(input_data).__name__
print(checkDataType(3.14))
print(checkDataType(True))


#3.2
def evenOrOdd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

print(evenOrOdd(7))
print(evenOrOdd(10))

#4.1
def sumWithLoop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
numbers = [1, 2, 3, 4, 5]
sum = sumWithLoop(numbers)
print(sum)

#5.1
def duplicate(lst):
    return [item for item in lst for _ in range(0,1)]
print(duplicate([1, 2, 3]))

#5.2
"""def square(num) the error is that the function is missing a colon.
    return num ** 2
    """

#correted version: 

def square(num):
    return num ** 2
print(square(5))


print("")
print("")
print("")
print("")




#6.2 favorite function
def checkDataType(input_data):
    return type(input_data).__name__
print(checkDataType(3.14))
print(checkDataType(True))