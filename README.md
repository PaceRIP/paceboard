# paceboard

![Project logo, a sine wave forming gravestones in the negative space.](assets/img/logo.png)

[Blog post](https://info.pace.rip/blog/2021/6/29/) - [Example site](https://info.pace.rip/blog/2021/6/29/paceboard/)

## About

**paceboard** is a template-based static site generator for speedrun leaderboards.

You can configure site details, implement categories, and add runs all from a single Python script (`paceboard.py`).

Category and run information is stored in `csv` files for ease of access and editing.

## Instructions

This guide assumes that you know the basics of hosting your own website. Since paceboard is a *static* site generator, you can host via the free [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages), assuming you know how to use [Git](https://git-scm.com/video/get-going).

Let's get started!

1. Make sure you have the latest version of [Python 3](https://wiki.python.org/moin/BeginnersGuide/Download).
2. [Download](https://github.com/PaceRIP/paceboard/archive/refs/heads/master.zip) or [fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) the paceboard repository.
3. Go to your install location via the command line, then run `python3 paceboard.py`. Follow the prompts to configure and auto-generate your site!
4. Discover you made a typo? Hop into the `csv` folder and you can manually edit the spreadsheets inside. Afterwards, running `python3 scripts/generate.py` will update your site with the new info.

## Template-based?

Within the `templates` folder are the [HTML](https://www.w3schools.com/html/html_intro.asp) files paceboard uses to format the site. If you're feeling intrepid, you can edit these templates to your liking.

During page generation, paceboard swaps out the `tk_` and `lk_` strings with their corresponding values in the database.