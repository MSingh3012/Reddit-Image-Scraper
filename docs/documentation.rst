.. _documentation:

Documentation
=============

Requirements
------------

The following tools are needed to build the documentation

* ``sphinx``
* ``sphinx_rtd_theme``

To install all the requirements simply use pip while currently in the docs
directory

.. code-block:: bash

   pip install -r requirements.txt

This will install all the necessary dependencies.

Usage
-----

The documentation gets built using ``make``, and comes in several flavors.

``make html`` - build the API and narrative documentation web pages, this
is the the default ``make`` target, so running just ``make`` is equivalent to
``make html``.

``make html_noapi`` - same as above, but without running the auto-generated
API docs. When you are working on the narrative documentation, the most time
consuming portion  of the build process is the processing and rending of the
API documentation. This build target skips that.

You can run ``make help`` to see information on all possible make targets.
