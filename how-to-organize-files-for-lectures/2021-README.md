# How to organizes files for lectures
(author: Stefan Harmeling, created: 2021-02-19, license: CC BY-SA 4.0)

Notes: sciebo is a cloud solution for universities in NRW/Germany which you can replace with any other cloud storage solution.

# before the semester

Create a sciebo subfolder and a git repository:

    sciebo/2021-SS-Deep-learning
    git/2021-SS-Deep-learning-repo
    
Use `sciebo` for the following folders:

    public      # to publish slides, exercises, notebooks, code, data
    orga        # to collect lists of points, syllabus, exam results
    submission  # where students can drop of their homeworks
    workspace   # where tutors correct homeworks
    slides      # if powerpoint slides, for my local edits, maybe in another git if tex
    
Use `git` for the following stuff:

    exercises   # latex sources, no PDFs committed (they go to sciebo)
    notebooks   # without evaluation (otherwise to `public`)
    code        # access data only via sciebo in public/data
    
It is better to keep the checked-out git repo separate from the sciebo folder, since it keeps trying to sync the hidden stuff and chokes.  If you use more than one machine, you should always `git pull` at the beginning and `git push` at the end of your edits.

# during the semester

Students have read access to 

    sciebo/2021-SS-Deep-learning/public
    
Assistents have read/write access to 

    sciebo/2021-SS-Deep-learning/public
    git/2021-SS-Deep-learning-repo

For copying stuff from older lectures, checkout old repositories or give read access to the older sciebo folder.

# after the semester

1. checkout final version of the git repository
2. copy the subfolders to sciebo
3. remove the access rights of assistents from sciebo
