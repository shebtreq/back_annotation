TocTree Points
==========================================

".. toctree::"
This directive inserts a “TOC tree” at the current location, using the individual TOCs (including “sub-TOC trees”) of the documents given in the directive body. Relative document names (not beginning with a slash) are relative to the document the directive occurs in, absolute names are relative to the source directory. A numeric maxdepth option may be given to indicate the depth of the tree; by default, all levels are included. [1]

Consider this example (taken from the Python docs’ library reference index):

.. toctree::
   :maxdepth: 2

   intro
   strings
   datatypes
   numeric
   (many more documents listed here)


   :numbered:
   :titlesonly:
   :glob:
   :hidden:



Including Random Points page here

.. include:: randompoints.rst
   