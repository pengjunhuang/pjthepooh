Title: I Chose Pelican 
Date: 2016-09-25 20:20
Modified: 2016-09-25 20:20
Category: Geek
Tags: blog, pelican, python, web development
Slug: i-chose-pelican
Authors: PJ
Summary:
<!--Status: draft-->

[TOC]

I have been thinking about making a personal website for awhile, but just could not find time to actually work on it. It takes time but I know it is worth it. A month ago, I was struggling on what framework to use and where to host it. Until recently, I learned and tried three different frameworks and finally decided what is the best for me. 

# Static or Dynamic
This was the first question I asked myself. I was biased to dynamic because I want my website to connect with a database, though it is not necessary. The process of setting up the whole dynamic website would definitely help me explore a new area in my life. There is a short way and a long way to accomplish it. The short way is to use a web-hosting service such as Wordpress, Blogger and Weebly; while the long is to build it myself using some web development platform.

Anyway, I chose static at the end. Below are the reasons. 

# Django
One of the main purposes I'm making a website is trying to learn new things through the process, so of course the drag-and-click feature is not something I would look for. At first I started to learn django. After two weeks of researching online materials, I was able to make a decent skelton successfully connecting to a database, but I was exhausted and not satisfied. I think django is an overkill for my website. Although django is great for professional web development, the investment of learning this framework does not give me a quick pay back. The learning process did help me build a good understanding of web development; I gave up though. 
 
# Wordpress
Using a hosting server, users are able to SSH the server but do not have permission to install applications. Plus, it is costly compared to other approaches. I decided to give it a try and installed wordpress in my AWS EC2 micro. That way at least I would have full control and be able to play around with MySQL. Things went pretty well in the first couple days, but my server began to suffer running out of RAM soon after. In the following week, I kept trying many different ways to optimize the configuration of the web, PHP, and database, nothing seemed to work. I finally moved the database to an RDS instance, but my website was still not able to be hosted smoothly, loading very slowly and even timing out. As it was too annoying, I decided to move to a static web.   
 
# Pelican
For static website, there are several popular platforms, e.g. [Hexo](https://hexo.io/) (javascript), [Jekyll](https://jekyllrb.com/) (ruby) and [Pelican](http://blog.getpelican.com/) (python). Users only need to know some basic syntax of the language to begin. I picked pelican simply because it is written in python. All of these frameworks have a large community of developers and users, so there are tons of themes and plugins available. 
 
The initial setup of Pelican is simple and it will provide a dummy template to begin with; however, I did need to spend some time on customization and settings. With Pelican's simplicity, I can focus on my writing and not being distracted by thinking how to format my post because the theme does all the jobs for me. If I want to edit the theme, it is easy enough too. So far from writing to deploying a new post, I do not need to touch the mouse, which is a pretty smooth process. 

# Ending
Last month was all about trial and error. In the end I was able to learn new things. Most importantly I built my website the way I like. Of course there are some downsides of using Pelican, but I can bear them. I may write up a post about how to build a blog with Pelican later :) 


 
