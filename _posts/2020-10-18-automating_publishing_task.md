---
layout: post
author: louloucodes
title: Automate Publishing Workflow
category: automation
tags: automation shell git workflow tags
---
# Automating my publishing workflow...

### Adventures in tagging, continued

My solution for tagging posts is the 'jekyll-tagging' plugin, which GitHub does not support. I discussed the workaround [in this post](https://louloucodes.github.io/2020/09/10/Adventures-in-Tagging-Part-2.html), and outlined the steps I needed to make ensure that pages for new tags appear.

There aren't that many steps, but they are kind of annoying, so... I wrote a script to automate them. 

This is my first shell script and I am pleased with it :heart_eyes:

```
#! /bin/sh

#automate workflow to publish blog post:
#  make sure new auto-generated tag pages are uploaded
#  add all, commit with message, and push to git

echo Enter commit message
read commit_message
echo Your message is ${commit_message}

pub_dir=~/my_path #I hardcoded this with the actual path

# remove current tag directory
rm -R ${pub_dir}/tag

# create tag directory
mkdir ${pub_dir}/tag

# copy everything from the _site/tag directory to tag
cp -R ${pub_dir}/_site/tag/* ${pub_dir}/tag/

# add, commit, and push
git add .
git commit -m "${commit_message}"
git push

```
And a side note: I discovered that the tag `CLI` isn't working as I expect it to because the tagging process turns it into lowercase `cli`. Which is great! But I have to figure out how to convert that. I'm sure it will be a straightforward, built-in function like Python's `lower()` except in Ruby.
