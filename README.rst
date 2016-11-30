========
kirigami
========

Taking PaperCut to The Next Level.

About
-----
The basic kirigami distribution contains tools for interacting with the Simon's
Rock PaperCut managed print server from Python. The ``Connection`` class is
publicly exported for use in other applications. The ``kirigami`` python
package is a pure Python driver for using the school managed print services.

Support / Feedback
------------------
For issues with, questions about, or feedback for kirigami, please look into
our `support channels
<https://src-code.simons-rock.edu/git/print-central/kirigami/issues>`_. Please
do not email any of the kirigami developers directly with issues or questions -
you're more likely to get an answer on the ``#kirigami`` channel on chat_.

Please contact the primary maintainer, Dennis Chen, either on chat_, or by
other means such as email for any other concerns.

Installation
------------
The latest master branch of kirigami can be installed with `pip
<http://pypi.python.org/pypi/pip>`_::

  $ python3 -m pip install https://src-code.simons-rock.edu/git/print-central/kirigami/archive/master.tar.gz

You can also download the project source and do::

  $ python3 setup.py install

Dependencies
------------
`netifaces <https://pypi.python.org/pypi/netifaces>`_ is required for the
enumeration of network devices.

.. _chat: https://chat.simons-rock.edu/
