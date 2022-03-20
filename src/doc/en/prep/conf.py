# nodoctest
# PREP Tutorials documentation build configuration file, created by
# sphinx-quickstart on Tue Jul  3 10:54:56 2012.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

from sage.docs.conf import release
from sage.docs.conf import *  # NOQA

# Add any paths that contain custom static files (such as style sheets),
# relative to this directory to html_static_path. They are copied after the
# builtin static files, so a file named "default.css" will overwrite the
# builtin "default.css". html_common_static_path imported from sage.docs.conf
# contains common paths.
html_static_path = [] + html_common_static_path

# General information about the project.
project = "PREP Tutorials"
copyright = "2012, Rob Beezer, Karl-Dieter Crisman, and Jason Grout"

# The name for this set of Sphinx documents.
html_title = project
html_short_title = project

# Output file base name for HTML help builder.
htmlhelp_basename = 'prep_tutorials'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto/manual]).
latex_documents = [
  ('index', 'prep_tutorials.tex', 'PREP Tutorials',
   'Rob Beezer, Karl-Dieter Crisman, and Jason Grout', 'manual'),
]
