---
layout: post
title: Adventures in Navigation
category: jekyll
tags: jekyll liquid navbar tags
---
Add another item to the list of things that are not so easy for
me: tags. 
Something so straightforward as tagging posts and pages
for content should be easy to implement in a language that touts
itself as easy and accessible. 

For a rank beginner (hi!) this is not so easy. I'll save my 
misadventures in linking to tags for another post, because the
true subject here is ...
### The navbar
I encountered issues with the navbar in one of my attempts to
create pages for the tags. All of a sudden, the navbar filled 
with `Tag: aws` and `Tag: python` and all of the other tags 
accumulated through my posts. 

### What is going on?
Some fumbling around -- remember, noob here -- led me to the
default (I think?) header.html in the default minima theme. This
is a reusable snippet of html that can be included on any page,
and is conveniently found in the `_includes` folder.

The culprit was here:

```
...if my_page.title ...

```
See that? `if my_page.title` meant that every single page that
had a title would appear in the navbar. Doh!

### My solution
I added a flag variable to the pages I want to appear in the 
navbar. Specifically, in `about.html` and `blog.html` (should these
be `.md`?), to the front matter:
```
---
navbar: true
---
```
Then I returned to the `header.html` file and changed the 
variable controlling appearance in the header to 
`my_page.navbar`.
### Problem solved! 
And now back to the tagging problem...

### Haha
Also joke's on me when I attempted to cite the Liquid code, my
server raised an error...so I'll have to figure that out too.