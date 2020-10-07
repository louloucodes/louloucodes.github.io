---
layout: post
author: louloucodes
title: Directory Tree Generator Challenge -- Recursive Solution
category: python
tags: python challenge project portfolio CLI recursion
---
# Application of recursion

On first glance, I thought the hardest part of the [Directory Tree Generator challenge](https://realpython.com/intermediate-python-project-ideas/#directory-tree-generator) would be traversing the directory structure. My instincts turned out to be wrong, as I solved the general problem with the os package and a single, recursive function.

The os package provides the functionality to explore the file structure, and in particular `os.path.listdir` and `os.path.isdir`. As I wrote it, the directory tree generator allows the user to choose which directory to be the root of the tree and how deep to traverse the file structure.

I did not *intend* to solve this problem recursively, but it turned out to be the natural solution, as nested for-loops have their limits -- this would have been fine if I had been satisfied with hard-coding in the depth of the tree. But no, I wanted the user to determine that, not the coder. (The fact that I am both the user and the coder does not matter -- what I want tomorrow may not be what I want today.)

My biggest fear with recursion is getting stuck in an infinite loop. My habit is to put the kick-out condition [see note below] at the top of the function so that I won't forget to do it later. Also, when I say habit -- it's been a minute since the last time I wrote a recursive function. If I think about it, it was before I had children, back when I taught computer science to high school students. My own children are now both in high school, and yet this habit came right back to me.

Satisfied with my solution to the base problem, the next challenge was to figure out how to visually distinguish the files from the directories. And that will be the next post.

Note: the technical term, which did not come back to me but was easy enough to look up, is *base case*.



