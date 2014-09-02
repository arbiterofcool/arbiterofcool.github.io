---
layout: post
title: "Planting your project with fig-seed"
published: true
---

# "Why do I have to copy and paste your demo?"

Why not auto-generate and run it? I do not just want the source, 
I want it to see it work. Enter `fig-seed init <example>` and it works.

This is problem that [fig-seed](https://github.com/arbiterofcool/fig-seed) solves.
There is no `fig init` command. This is a common pattern in Ruby.
I want to run a command that creates a default fig.yml, 
Dockerfile and has a default folder structure for each framework. I want a
command to pull an entire demo.

For new projects, I experiment with different web frameworks. I'm required to set up 
an environment and dependencies for each one. This takes hours and days that I cannot
spare.

# Requirements
---------------

`fig-seed init` creates an empty application.

`fig-seed init <example>` duplicates the default example application.

`fig-seed init <example> <alternate>` duplicates an alternate example application.

# Usage
---------------

`fig-seed init fig` creates the Flask application featured on the [Fig](fig.sh) landing page.

`fig-seed init fig-rails` for [Rails](http://www.fig.sh/rails.html)

`fig-seed init fig-django` for [Django](http://www.fig.sh/django.html)

`fig-seed init fig-wordpress` for [Rails](http://www.fig.sh/wordpress.html)