---
layout: post
author: louloucodes
---

# Today I Learned: Python tip
### The little lambda that could

I needed to find the maximum of values in a dictionary. I had an old school (and inefficient) solution in mind:
```
max = 0
max_key = ''
for entry in my_dictionary:
    if len(my_dictionary[entry]) > max:
        max = len(my_dictionary[entry])
        max_key = entry
```
And then I made the wise choice to see if there is a better way, and of course there is. *Always check the documentation.* Documentation is still a bit of a slog for me, so often I have to search for examples too.
Here is the [documentation](https://docs.python.org/3/library/functions.html#max).

I don't remember what the example was, so I will record my own! Here it is for posterity:
```
max(my_dictionary.keys(), key = (lambda entry: len(my_dictionary[entry]))
```

How wonderful!

I have not unleashed the complete power of the [`max` function](https://docs.python.org/3/library/functions.html#max) as described in the documentation, but I now have a taste of it. Also can be used with [`min`](https://docs.python.org/3/library/functions.html#min) and [`sorted`](https://docs.python.org/3/library/functions.html#sorted) and maybe even other yet-to-be-discovered-by-me functions.

Python :snake:, I think I :sparkling_heart: you.
