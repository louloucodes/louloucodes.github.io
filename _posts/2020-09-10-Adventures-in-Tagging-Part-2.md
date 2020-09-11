---
layout: post
tags: tags ruby jekyll github workflow
---

It turns out that celebrating successful tagging was premature. The links to the tags worked *only on my local machine*. 

There were a couple of wrong turns in my search to find the solution...that I will not record. The final answer came from my husband*. He read the documentation -- and it made sense to him. [Here is the link to GitHub's page about approved plug-ins.](https://docs.github.com/en/github/working-with-github-pages/about-github-pages-and-jekyll). 

The key information here is
> GitHub Pages cannot build sites using unsupported plugins. If you want to use unsupported plugins, generate your site locally and then push your site's static files to GitHub.

Is the `jekyll-tagging` plugin supported by GitHub? **No**, it is not. 
When I build my site locally with `bundle exec jekyll serve`, the tagging gem generates tag pages in the `_site` folder, from which the pages are served.

GitHub does NOT serve pages from `_site` -- and there's no way to get around it. (I shouldn't say "no way," rather, no way that I found.)

The solution is to change my workflow**.

#### Workflow before:
1. Write a blog post on my machine.
2. Generate my site locally: `bundle exec jekyll serve`.
3. Push changes to the GitHub repo.

#### Workflow now:
1. Write a blog post on my machine.
2. Generate my site locally: `bundle exec jekyll serve`.
3. Replace the existing `tag` directory in the home directory with the `tag` directory from `_site` (the static files referred to in the quote above).
4. Push changes to the Github repo.

I will probably end up writing a bash script to automate the workflow, but that will be another blog post.

Proof of concept: see the tag links below? Click on one of them! 

The * above on husband because this one word does not do justice to all of his roles in my life: mentor, champion, git whisperer, programming wizard, to name just a few. He's generally awesome.

I generally avoid the word workflow** because I dislike business jargon, but here it feels meaningful and descriptive.
