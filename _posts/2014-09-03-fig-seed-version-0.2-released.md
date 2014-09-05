---
layout: post
title: "fig-seed version 0.2 released"
published: true
---

### "Release early, release often." - Eric S. Raymond

#Release notes:
* added 'up' feature
* now testing on [Digital Ocean](https://www.digitalocean.com/).

[fig-seed](https://github.com/arbiterofcool/fig-seed), plant your project.

Usage:
  fig-seed.py list
  fig-seed.py up <template_name>
  fig-seed.py [-uv] init [<template_name> <target_directory>]

  -v, --verbose       verbose mode
  -u, --up            fig up -d

Arguments:
  template_name        folder name in template directory
  target_directory     where the template is copied.


Example: fig-seed.py init /tmp/init
         fig-seed.py init fig-flask /tmp/fig-flask
