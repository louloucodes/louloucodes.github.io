---
layout: page
title: About
permalink: /about/
---
This page tells you nothing about me! However ...

All the tags on this site:
{% comment %}
Simply list all the tags...
{% endcomment %}
{% for tag in tags %}
    <a href="#{{ tag | slugify }}"> {{ tag }} </a>
{% endfor %}

All posts with tags:
{% comment %}
Simply list all the posts that have a certain tag.
{% endcomment %}

{% for tag in tags %}
    <h2 id="{{ tag | slugify }}">{{ tag }}</h2>
    <ul>
    {% for post in site.posts %}
        {% if post.tags contains tag %}
            <li>
	    <h3>
	    <a href="{{ post.url }}">{{ post.title }}
            <small>{{ post.date | date_to_string }} </small>
	    </a>
            {% for tag in post.tags %}
		<a class="tag" href="/tag/#{{ tag | slugify }}">{{ tag }}</a>
	    {% endfor %}
            </li>
        {% endif %}
    {% endfor %}
    </ul>
{% endfor %}

This is the base Jekyll theme. You can find out more info about customizing your Jekyll theme, as well as basic Jekyll usage documentation at [jekyllrb.com](https://jekyllrb.com/)

You can find the source code for Minima at GitHub:
[jekyll][jekyll-organization] /
[minima](https://github.com/jekyll/minima)

You can find the source code for Jekyll at GitHub:
[jekyll][jekyll-organization] /
[jekyll](https://github.com/jekyll/jekyll)


[jekyll-organization]: https://github.com/jekyll
