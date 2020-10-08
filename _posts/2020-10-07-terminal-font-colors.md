---
layout: post
author: louloucodes
title: Directory Tree Generator Challenge -- Customizing
category: python
tags: python challenge project portfolio CLI recursion
---
# Directory Tree Generator: Making it mine

So one advantage of [making this tool](https://louloucodes.github.io/python/2020/10/05/Real-Python-Project.html) for myself is that I can make it do what I want and look how I want, and what I wanted was colorful printing to the terminal to help distinguish the files from the directories.

The Real Python folks suggested the [pypi `colored` package](https://pypi.org/project/colored/), and I found it easy to implement. I used the `stylize`, `fg` (foreground), and `attr` (attribute) functions to print in color and boldface to the terminal. There's a great list of named colors -- I was taken by `thistle_1` and `deep_pink_2` -- but any hex value color will work. I'm a big fan of Google's color picker for finding hex values of shades I like.

Of course, I won't always want pink and thistle for my tree, so the user can choose what values to use for the files and the directories.

After using my CLI tree for a couple of days, I recognized another customization that I would like to implement: organization fo the tree by level. Sometimes it would be useful to have this by date, or by size, or alphabetically. By the time I publish the code in my repo, I plan to have this customization implemented too.

