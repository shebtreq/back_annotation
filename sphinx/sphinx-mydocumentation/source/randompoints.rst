Random Points
=========================================

ReST Syntax Reference



Line blocks
----------

| These lines are
| broken exactly like in
| the source file.


Grid table
-----------

+------------+------------+-----------+ 
| Header 1   | Header 2   | Header 3  | 
+============+============+===========+ 
| body row 1 | column 2   | column 3  | 
+------------+------------+-----------+ 
| body row 2 | Cells may span columns.| 
+------------+------------+-----------+ 
| body row 3 | Cells may  | - Cells   | 
+------------+ span rows. | - contain | 
| body row 4 |            | - blocks. | 
+------------+------------+-----------+


Simple Table
------------

=====  =====  =======
A      B      A and B
=====  =====  =======
False  False  False
True   False  False
False  True   False
True   True   True
=====  =====  =======


Emphasis
----------

*escape* ``with`` "\"

\*escape* \``with`` "\\"



Citations
---------

Citation references, like [CIT2002]_. 
Note that citations may get 
rearranged, e.g., to the bottom of 
the "page".
.. [CIT2002] A citation 
   (as often used in journals).


External hyperlinks, like Python_.
.. _Python: http://www.python.org/
 
Plain text	Typical result
External hyperlinks, like `Python 
<http://www.python.org/>`_.

Internal crossreferences, like example_.
.. _example:

This is an example crossreference target.

Python_ is `my favourite 
programming language`__.
.. _Python: http://www.python.org/

__ Python_

Implict references, like `Random Points`_.


.. _my-reference-label:

This is the text of the section.
It refers to the section itself, see :ref:`my-reference-label`.

.. include:: example.rb


Image Directive
----------------

The |biohazard| symbol must be used on containers used to dispose of medical waste.
.. |biohazard| image:: biohazard.png

.. image:: images/ball1.gif


Replacements
------------

|name|

   .. |name| replace:: replacement *text*
