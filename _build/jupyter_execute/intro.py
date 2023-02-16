#!/usr/bin/env python
# coding: utf-8

# # Introduction
# 
# 
# <p class="about">
# 
# `Hoefnagel` Wooden Jigsaw Puzzle Club is a company based in Port Townsend, Washington that contains a library of over 1000 **puzzles** rented by a network of puzzle enthusiasts worldwide. Their ultimate business goal is to reduce shipping costs while optimizing for consumer satisfaction. Right now, when an active member of the club finishes a puzzle, they start a return process on the site, which generates a shipping label for the user to ship this puzzle to the next user's location in the overall puzzle network. This next location is determined by a model that considers several factors, such as the puzzle's current location, the next user's location, and the puzzle's rank on the next user's wishlist. 
# 
# </p>
# 
# 
# 
# ```{tableofcontents}
# ```
# 
# 
# 
# Here is a "note" directive:
# 
# ```{note}
# Here is a note
# ```
# 
# 
# Here is an inline directive to refer to a document: {doc}`eda`.
# 
# 
# ```{seealso}
# Jupyter Book uses [Jupytext](https://jupytext.readthedocs.io/en/latest/) to convert text-based files to notebooks, and can support [many other text-based notebook files](https://jupyterbook.org/file-types/jupytext.html).
# ```
# 
# 
# 
# 
# ```{figure} /_static/images/difficulty_dist.png
# :scale: 3%
# ```

# In[1]:


print(2 + 2)


# ## Citations
# 
# You can also cite references that are stored in a `bibtex` file. For example,
# the following syntax: `` {cite}`holdgraf_evidence_2014` `` will render like
# this: {cite}`holdgraf_evidence_2014`.
# 
# Moreover, you can insert a bibliography into your page with this syntax:
# The `{bibliography}` directive must be used for all the `{cite}` roles to
# render properly.
# 
# 
# ```{bibliography}
# ```
