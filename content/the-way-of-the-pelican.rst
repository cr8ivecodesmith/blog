###################################################
the way of the pelican and the order of silly walks
###################################################

:date: 2013-05-25 18:00
:category: code
:tags: python
:status: published


Once there was boy who wrote magnificent stories about technology and the
internets. He talked about tales of discoveries and adventures, of code and
sorcery, of... *well you get the point*.

Let me tell you his story.


*******************
the art of blogging
*******************

For many months he poured all of his energy in an ancient art called
"blogging".

He learned about the arcane languages called "HTML", "CSS", and
"Javascript" that is used to invoke the necessary spells to put up a
"website" that runs inside these puny looking contraptions called
"servers".

And so he wrote one webpage after another. Days went by like a puff of
smoke. He wrote with so much glee it seemed like madness

One day, while he was out for a walk, he discovered a magical piece of
software called a "CMS". He spent quite a while researching and learning
about it. He learned that in order to wield it one must setup a "Database"
to store the website scriptures among many things.

"This could really improve my blogging techniques!", he thought.

So off with the old and into the new! He started using the "CMS" and got
absorbed in its power and extravagance.


**********
complexity
**********

Many months passed by and his website grew in popularity. Traffic surged
and things appear to have taken a new direction.

He became focused on the black arts of getting more mailing list
subscribers, selling affiliate products, gaining more social network
followers. Even the topics he chose to write about have become focused
around these matters.

He also invoked one "plugin" after another as the CMS permits its wielder to
extend its power with such spells. All of which are for vanity's sake.

Eventually he spent more time configuring than writing.


**************
losing purpose
**************

As he continued down this new path, the boy started becoming weary.
Inspite of the lights, glamour and all things shiny, he felt empty. Lost.

"Everything appears to be going well but it all feels wrong somehow...", he
thought.

For a brief moment (about 2 seconds) he remembered the days of old. With
only a simple parchment he calls a "text editor", he wrote stories of his
discoveries and adventures and how he would go about it for many hours.

It was the good times indeed, with nothing but the innocence and the
passion of sharing.

"I've become lost.", he mumbled.

And so the very next day the boy set off to a journey to find himself once
more.


************************
the order of silly walks
************************

He travelled for many days. He went from one village to the next. He
trekked on great plains, majestic mountains, and myterious forests.

One day while he was out for a drink along a stream, he saw a group of
merry men doing some sort of outlandish dancing.

Curious about what's going on, he cautiously approached one of them.

"What do you call this silly dancing, sir?", the boy asked.

"Dancing?! Preposterous! We are channeling our energies to wield a
powerful, yet cleverly simple, software called the Pelican.", the man
replied.

Later he learned that the group was called the `Order of Silly Walks`.
They too are bloggers like him and gained a cult following of
audience. But they appeared different somehow. They looked happy, fulfilled,
simple and pure to the core.

.. code-block:: html

    <iframe id="player" type="text/html"
        width="640"
        height="480"
        src="http://www.youtube.com/embed/IqhlQfXUk7w?enablejsapi=1&origin="
        frameborder=0>
    </iframe>


**********
a new path
**********

"I must know their secret!", he thought.

Mustering his strength, he asked the man once more...

"You need not ask young man. You appear to have to lost your way and so we
shall show you the path back your self. We shall teach you the way of the
Pelican!", said the man.


**********************
the way of the pelican
**********************

"In this training you shall learn to create good old static websites and
host it on Github!"

"First things first, I shall assume that you have a `Github account`,
`git`, `python`, a `terminal`, and your running `Ubuntu`. Otherwise, move on
and learn them some place else then come back to me."

"Otherwise, let's begin your training."


create an empty git repository
==============================

Go to your Github account and create a new empty repo for your blog and name
it.

.. code-block:: text

    [username].github.io

"Using your `username` is important here so that github will know that 
you're trying to create a Github page.", the man warned.


clone the empty repo locally
============================

Clone it to your local directory

.. code-block:: sh

    $ git clone git@github.com:[username]/[username].github.io.git my_blog
    $ cd my_blog
    my_blog $

Install pelican with markdown and github import.

.. code-block:: sh

    my_blog $ pip install pelican markdown ghp-import


invoke the pelican quickstart
=============================

"Run this powerful spell to configure pelican;"

.. code-block:: sh

    my_blog $ pelican-quickstart

"You will be asked many questions. Answer them as your heart desires."

"Here is an example with important answers highlighted."

.. code-block:: text
    :hl_lines: 12 13 16 17 23 24

    Welcome to pelican-quickstart v3.7.1.

    This script will help you create a new Pelican-based website.

    Please answer the following questions so this script can generate the files
    needed by Pelican.

    > Where do you want to create your new web site? [.] 
    > What will be the title of this web site? My Blog
    > Who will be the author of this web site? Juan Tamad
    > What will be the default language of this web site? [en] 
    > Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) 
    > What is your URL prefix? (see above example; no trailing slash) [username].github.io
    > Do you want to enable article pagination? (Y/n) n
    > What is your time zone? [Europe/Paris] Asia/Manila
    > Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) 
    > Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) 
    > Do you want to upload your website using FTP? (y/N) 
    > Do you want to upload your website using SSH? (y/N) 
    > Do you want to upload your website using Dropbox? (y/N) 
    > Do you want to upload your website using S3? (y/N) 
    > Do you want to upload your website using Rackspace Cloud Files? (y/N) 
    > Do you want to upload your website using GitHub Pages? (y/N) y
    > Is this your personal page (username.github.io)? (y/N) y

    Done. Your new project is available at /home/juan/my_blog


create an article
=================

Create an article in restructured text or markdown.


.. code-block:: sh

    my_blog $ vim content/my-first-blogpost.rst

"You must have the following spell at the top of your file in order for
Pelican to recognize your post."

.. code-block:: text

    ###########
    hello world
    ###########

    :date: 2013-05-25 18:00
    :category: code
    :tags: pelican, python
    :author: juan tamad

    "Somewhere below that you may begin writing your story."

    Hello world!


test your new website
=====================

Generate the HTML files and run a development server

.. code-block:: sh

    my_blog $ ./develop_server.sh start

Check it out

.. code-block:: sh

    my_blog $ firefox http://localhost:8000


release your website
====================

Push your changes to Github

.. code-block:: sh

    my_blog $ git add -A
    my_blog $ git commit -m "The blog has begun!"
    my_blog $ git push -u origin master
    my_blog $ make github

Visit your new shiny site

.. code-block:: sh

    my_blog $ firefox http://[username].github.io


learning more
=============

"This is but a taste of the simplicity and power of the Pelican",
said the man.

"Further your training and
`learn more <http://docs.getpelican.com/en/stable/settings.html>`_
about its ways."


*******
the end
*******

Several months later the boy has finished his training and with his new
found enlightenment, he went back home happier for once more the focus of
his blog is about creating wonderful content. The days of joy went on for
many years... until further notice.
