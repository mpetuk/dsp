# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

>> pwd
>> mkdir mine
>> rm -rf mine
>> touch deletethis.py
>> rm -r deletethis.py
>> mv deletethis.py savethis.py
>> ls -ld .?*
>> cp movethis.py ../newfolder/movethis.py
>> ps -ef | grep mpetukhova #list running programs/process under user 'mpetukhova'
>> chmod #control access to directories

 



---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > `ls` lists content of the current directory in short format
    `ls -a` lists both hidden and unhidden files in short format
    `ls -l` lists content with long format -shows permissions
    `ls -lh` lists long format with readable file size
    `ls -lah` lists hidden and unhidden files in long format with readable file size
    `ls -t` lists content in ascending order by time and date
    `ls -Glp` lists in long format, suppresses group info, shows file type

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > `ls -lrt` lists content in long format in descending order by time and date (most recent - first)
    `ls -lSrh` lists content in long format in descending order by size file with readable file size 

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > `xargs`  reads items from the standard input and executes specified command
one or more times with any initial-arguments followed by items from standard input
> > Example: find ./tmp -name deletethis -type f -print | xargs /bin/rm -f
> > finds file(s) 'deletethis' in subdirectory tmp and deletes them (file names should be without spaces or new lines). 

