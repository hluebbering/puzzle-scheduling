---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---


<div class = "header">

<div class = "topheader">
<span class = "school">University of Washington</span>
<span class = "department">Data Science</span>
</div>


<h1 class="bottomheader"> Puzzle Schedules | 2023 </h1>

</div>




<div class = "authors">

<p>Jonathan Alexander, Madalyn Li, Hannah Luebbering, Aishwarya Singh</p>

</div>



# Introduction


<p class="about">

`Hoefnagel` Wooden Jigsaw Puzzle Club is a company based in Port Townsend, Washington that contains a library of over 1000 **puzzles** rented by a network of puzzle enthusiasts worldwide. Their ultimate business goal is to reduce shipping costs while optimizing for consumer satisfaction. Right now, when an active member of the club finishes a puzzle, they start a return process on the site, which generates a shipping label for the user to ship this puzzle to the next user's location in the overall puzzle network. This next location is determined by a model that considers several factors, such as the puzzle's current location, the next user's location, and the puzzle's rank on the next user's wishlist. 

</p>





<span class = "toc">Project Notebooks:</span>

```{seealso}
- Notebook 1. Preliminary Data Analysis and Data Cleaning
- Notebook 2. EDA
```






<span class = "toc">Project Data:</span>

<div class = "mygrid">
<div class = "data" style = "background: #9ed342a6;">
<span class = "dataset">Data 1. member holdtimes/packs</span>
<div class = "myicon 1"></div>
<span class = "vars">nrows: </span>
</div>

<div class = "data" style = "background: #40d3e2a6;">
<span class = "dataset">Data 2. packs</span>
<div class = "myicon 2"></div>
<span class = "vars">nrows: </span>
</div>

<div class = "data" style = "background: #41a7e0a6;">
<span class = "dataset">Data 3. Combined Data</span>
<div class = "myicon 3"></div>
<span class = "vars">nrows: </span>
</div>

</div>



<span class = "toc">Combined Data Preview: </span>



```{code-cell}
import pandas as pd
member_df = pd.read_csv("data/members_packs_cleaned.csv", header = 0)
member_df.head()
```


```{figure} /_static/images/hold_times_dist.png
:scale: 3%
```



## Project Goals 


## Conclusions

















## Citations

You can also cite references that are stored in a `bibtex` file. For example,
the following syntax: `` {cite}`holdgraf_evidence_2014` `` will render like
this: {cite}`holdgraf_evidence_2014`.



```{bibliography}
```
