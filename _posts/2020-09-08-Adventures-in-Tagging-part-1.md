---
layout: post
tags: tags ruby git til
---
The headline is
### I got the tagging to work!!!
Don't know why I expected tagging to have some sort of easy implementation. Clearly I don't know what I'm doing! 

Attempts included:
* creating tag pages by hand. Clearly the wrong solution.
* writing a python script to create tag pages. Turned out to be the wrong solution because (1) the way I wrote it require running the script every time I create a post and (2) the foundation for Jekyll is Ruby.
* finding the ['jekyll-tagging'](https://github.com/pattex/jekyll-tagging) gem*, blindly following the readme, and getting super frustrated that "it isn't working!"
* finding [this blog post](https://jameshfisher.com/2019/05/05/how-can-i-add-tags-to-a-jekyll-blog/) and copy-pasting the code. **This was actually *almost* there.**
* deciding that I should really sit down and understand the code that I had just copy-pasted...never having looked at Ruby before, this was not a 5 minute exercise. Some odd syntax to learn here. I would like to shake James H. Fisher's hand for writing the tag generating code in the first place.
* multiple branches in my github repo, and finally one frustrated reset master to at least 10 commits back.

But here I am! I have tags with links that work and pages that have information on them! Hooray! I'm going to bed.

TIL from * above: There's an app for that! In Python, there's a package for that! And now I know that in Ruby, there's a gem for that! 
