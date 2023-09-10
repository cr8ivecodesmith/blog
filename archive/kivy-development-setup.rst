##################################
kivy development environment setup
##################################

:date: 2019-03-29 12:57
:category: code
:tags: python,kivy,game-development
:status: published


I've been itching to get back to (re)learning Kivy again by creating games with
it.

With any development endeavor, the environment needs some setting up. It's
really been a while since I've used Kivy so I'm documenting my process with
this post.


**************
pre-requisites
**************

My current machine has the ff. setup:

- Ubuntu 18.04
- `PyEnv <https://github.com/pyenv/pyenv>`_


*************************
setting up the virtualenv
*************************

We will install everything under a pyenv virtualenv based off of Python 3.6.7.

We'll then create a virtualenv for the kivy version we will be using.

.. code-block:: sh

   pyenv install 3.6.7
   pyenv virtualenv 3.6.7 kivy3-1.10.1
   pyenv local kivy3-1.10.1


************************************
install OS packages required by kivy
************************************

We want to install Kivy dependencies for SDL2. I got these from the
`official docs <https://kivy.org/doc/stable/installation/installation-linux.html#dependencies-with-sdl2>`_.


install necessary system packages
---------------------------------

.. code-block:: sh

   sudo apt-get install -y \
       python3-pip \
       build-essential \
       git \
       python3 \
       python3-dev \
       ffmpeg \
       libsdl2-dev \
       libsdl2-image-dev \
       libsdl2-mixer-dev \
       libsdl2-ttf-dev \
       libportmidi-dev \
       libswscale-dev \
       libavformat-dev \
       libavcodec-dev \
       zlib1g-dev

install gstreamer for audio, video (optional)
---------------------------------------------

.. code-block:: sh

   sudo apt-get install -y \
       libgstreamer1.0 \
       gstreamer1.0-plugins-base \
       gstreamer1.0-plugins-good


***************
installing kivy
***************

Make sure the succeeding commands will be ran from within the kivy virtualenv
we created earlier.

At this time, the latest kivy version is ``1.10.1`` which requires
cython ``0.28.2`` to compile. We need to install cython first before we can
install kivy.

.. code-block:: sh

   pip install Cython==0.28.2
   pip install kivy==1.10.1


*****************
installing kivent
*****************

While kivy should be enough for creating games with just the core library, the
types of games I plan to make requires some standard game engine features such
as a physics engine, particle engine, tile map handler, etc.

`KivEnt <http://www.kivent.org/>`_ is a very good and high-performant rendering
engine for this type of work!

The problem is it's not a simple pip install, so I'm documenting it here.

Like in the earlier steps, the folliwing need to be run from the kivy
virtualenv we created.


clone the kivent repository
---------------------------

You can clone this from any directory.

.. code-block:: sh

   git clone git@github.com:kivy/kivent.git
   cd kivent


install the ``kivent_core`` module
----------------------------------

KivEnt is actually comprised of different modules that can be installed
seperately. This allows you the flexibility to utilize it as little or as much
as you want in your kivy projects.

At the heart of it is the ``kivent_core`` module. Let's install that.

.. code-block:: sh

   cd modules/core
   python setup.py build_ext install
   cd ..

That's it!

From here on, you can import the ``kivent_core`` module from your kivy
projects.


********************************
install all other kivent modules
********************************

But why stop there? Let's go ahead and install the other kivent modules as
well.


``kivent_cymunk``
-----------------

The kivent cymunk integrates the cymunk module. Apparently this is a physics
engine. So yay!

Requires:

- cymunk
- kivent core

.. code-block:: sh

   pip install git+git://github.com/tito/cymunk
   cd modules/cymunk
   python setup.py build_ext install
   cd ..


``kivent_particles``
--------------------

This is the kivent module that provides a particle engine!

Requires:

- kivent core

.. code-block:: sh

   cd modules/particles
   python setup.py build_ext install
   cd ..


``kivent_maps``
---------------

This is the kivent module that provides interface for handling tile maps.
Essential for exploration/rpg games!

Requires:

- tmx
- kivent core

.. code-block:: sh

   pip install tmx
   cd modules/maps
   python setup.py build_ext install
   cd ..


``kivent_projectiles``
----------------------

I suppose this provides the engine to handle projectiles? Let's install it
anyway.

Requires:

- kivent core
- kivent cymunk
- kivent particles

.. code-block:: sh

   cd modules/projectiles
   python setup.py build_ext install
   cd ..


************
what's next?
************

So now we have a complete installation of Kivy and KivEnt! The two main
libraries we need in building cross-platform games in Python.

My goal is to create a roguelike game. But I'll start small with some
easier games and/or reverse engineering sample codes from the internets.

I'll try to document my practice here as well.
