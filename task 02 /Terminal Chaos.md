# Part 1 
used `cd` to enter the Eolian Caves. On using `tree` , was able to view all the contents in the directory. `cat parchemnt.txt` provided the required code.

Code : aHR0cHM6Ly9naXRo

# Part 2 
Got to understand the use of grep and combined the holy and good herbs. I took time to figure out the spell required both holy and good herbs. 
Used `grep -lr "holy"|xargs -0 grep -lr "good"`, grep -lr command is used to search for files that contain a specific text pattern within a directory and its subdirectories.
From there , on decoding moonbloom and mistveil , you get

Code : LnnmknnlLhrsdhk
Code : CSigVmaroAn is used in the Khanrock the Bloodforged part for the Celestial Veil Amulet.

# Part 3 
Used `git checkout` to switch to the different realms and obtained 3 codes.

Lightbook - dWIuY29tL2FtYW5ze

DarkbookI - GNhbGlidXIvVGVyb

DarkBookII - WluYWwtQ2hhb3MtR29kU3VpdGU=

# Part 4 
All together the 4 codes is a base 64 encoded URL  which on decoding leads to a github repository : Terminal-Chaos-GodSuite

# Part 5 
Here The repository is cloned. Commits are used and checked to see any changes. 
I used the follwoing the git commits : 

git add -p : to view changes 
git show : To view the details of a specific commit, including the commit message, author, date, and the changes introduced .
This leads to another base 54 encoded URL

Code : aHR0cHM6Ly9naXRodWIuY29tL2FuZ3JlemljaGF0dGVyYm94L1RvLXRoZS1zdGFycy1hbmQtcmVhbG1zLXVuc2Vlbg==

ON decoding , it takes you to the another github repository where the final victory message is giving . Once cloned , i used `python3 victory.py --run` to see the final message.

![Screenshot from 2024-08-22 07-29-21](https://github.com/user-attachments/assets/2fd8726a-4bcf-4658-8b53-ba9fe33c3ee3)

