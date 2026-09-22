# File: homework2.py

# Your file path should look like:
# python_decal_fa25/yourname/homework2/homework2.py

# Questions (Answer these in the homework2.py file as comments):

# 1) What’s the difference between Git, GitHub, and Git Bash?
# the difference between Git, GitHub, and Git Bash is that Git is a version control system that allows you to track changes in your code and collaborate with others. GitHub is a web-based platform that hosts Git repositories and provides additional features for collaboration, such as issue tracking and pull requests. Git Bash is a command-line interface that allows you to use Git commands on Windows, providing a Unix-like environment for working with Git.

# 2) What’s the difference between the terminal and the command line?
# the difference between the terminal and the command line is that the terminal is a program that provides a text-based interface for interacting with the operating system, while the command line is the interface itself where you can type and execute commands. The terminal can run different command line interfaces, such as Bash or PowerShell, depending on the operating system and user preferences.

# 3) How does Windows PowerShell differ from Git Bash?
# Windows PowerShell is a command-line interface and scripting language developed by Microsoft, while Git Bash is a command-line interface for using Git commands on Windows. PowerShell is more focused on system administration and automation, whereas Git Bash is specifically designed for Git version control.

# 4) What’s the difference between Anaconda, conda, and Python?
# Anaconda is a distribution of Python and R programming languages that includes many popular data science packages. Conda is a package manager that comes with Anaconda and allows you to create isolated environments for different projects. Python is the programming language itself, which can be installed independently or as part of the Anaconda distribution.

# 5) What is VS Code? 
# VS Code (Visual Studio Code) is a open-source code editor developed by Microsoft. It provides features such as syntax highlighting, debugging, version control integration, and extensions for various programming languages and tools. It is widely used for software development and supports multiple platforms, including Windows, macOS, and Linux.

# 6) What is a Jupyter Notebook? How is it different from Jupyter Lab?
# A Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations, and narrative text. It is commonly used for data analysis, scientific computing, and machine learning. Jupyter Lab is an integrated development environment (IDE) that provides a more flexible and powerful interface for working with Jupyter Notebooks, allowing you to manage multiple notebooks, terminals, and other file types in a single workspace.

# 7) What does ~/ mean?
# ~/ means the home directory of the current user.

# 8) What’s the difference between an absolute path and a relative path?
# An absolute path is a complete path that specifies the location of a file or directory from the root directory, starting with a forward slash (/) on Unix-like systems or a drive letter (e.g., C:\) on Windows. A relative path, on the other hand, specifies the location of a file or directory in relation to the current working directory, and does not start with a forward slash or drive letter.

# 9) Imagine you're in your "yourname" repo. Write the absolute and relative paths to "course_assignments/homework2".
# Absolute path: /path/to/python_decal_fa25/yourname/course_assignments/homework2
# Relative path: course_assignments/homework2

# 10) What command lets you move from "course_assignments/homework2/" to "course_assignments/"?
# The command to move from "course_assignments/homework2/" to "course_assignments/" is cd ..

# 11) What would rm ./ do in your current directory? (Don’t try it!)
# The command rm ./ would attempt to remove the current directory (./) and all of its contents. However, since rm is typically used to delete files and not directories, it would likely result in an error message indicating that the operation is not permitted or that the directory cannot be removed. It is important to be cautious when using the rm command, as it can permanently delete files and directories without confirmation.

# 12) What do the following commands do?
# git add
# git add does not commit changes to the repository, but it stages changes to be included in the next commit. It adds the specified files or directories to the staging area, allowing you to prepare them for a commit.
# git commit
# git commit saves the changes to the local repository.
# git push
# git push uploads the changes to the remote repository.

# 13) What's the difference between "git add ." and "git add <file>"?
# "git add ." stages all changes in the current directory and its subdirectories for commit.
# "git add <file>" stages only the specified file for commit.

# 14) What do "git status" and "git log -1" do?
# "git status" shows the current state of the working directory and the staging area, including which files have been modified, added, or deleted, and whether they are staged for commit.
# "git log -1" displays the most recent commit in the repository, showing information such as the commit hash, author, date, and commit message.

# 15) What’s the difference between cloning a repository and pulling from it?
# Cloning a repository creates a local copy of the entire repository, including its history and all branches, on your machine. Pulling from a repository, on the other hand, updates your local copy with the latest changes from the remote repository, merging them into your current branch.

# 16) What has been your most frustrating bug or error in this class so far? How did you troubleshoot or fix it?
# I tend to get frustrated when I don't know where I am in the terminal. I usually troubleshoot this by using the pwd command to print the current working directory and then using ls to list the files and directories in that location. This helps me understand where I am and what files are available, allowing me to navigate to the correct directory and resolve any issues.

# 17) What’s a question you still have? What’s something you’re confused about?
# I am still sometimes confused about finding folders in my finder and how they relate to my terminal. I sometimes have trouble finding the correct path to a folder in my terminal, especially when it comes to navigating through nested directories. I would like to learn more about how to effectively use the terminal to locate and access files and folders on my computer.

# 18) Tell me a fun fact!
# A fun fact is that the word "bug" in computer programming originated from an actual moth that was found causing issues in an early computer. The term has since been used to describe errors or glitches in software.

# 19) Print your favorite math expression you've learned in Python so far. 
print(2 ** 3)  # This prints 8, which is 2 raised to the power of 3. It's a non intuitive way to do exponentiation in Python, and it's a fun expression to use in calculations.

# (Hint: Use print() and add a comment explaining what it does.)
