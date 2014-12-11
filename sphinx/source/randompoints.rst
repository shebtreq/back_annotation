Random Points
==========================================






Grid table:

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



*escape* ``with`` "\"

\*escape* \``with`` "\\"



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


The |biohazard| symbol must be used on containers used to dispose of medical waste.
.. |biohazard| image:: biohazard.png


.. image:: images/ball1.gif


.. _my-reference-label:


This is the text of the section.

It refers to the section itself, see :ref:`my-reference-label`.


.. literalinclude:: example.rb
   :language: ruby
   :emphasize-lines: 12,15-18
   :linenos:

name
|name|

   .. |name| replace:: replacement *text*



Lorem ipsum [Ref]_ dolor sit amet.

.. [Ref] Book or article reference, URL or whatever.