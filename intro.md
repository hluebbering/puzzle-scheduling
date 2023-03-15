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


<h1 class="bottomheader"> Predicting Hoefnagel Member Puzzle Hold Times</h1>

</div>




<div class = "authors">

<p>Jonathan Alexander, Madalyn Li, Hannah Luebbering, Aishwarya Singh</p>

</div>



# Introduction


<p class="about">



Hoefnagel Wooden Jigsaw Puzzle Club{cite}`HoefnagelWoodenJigsaw2020` is a company based in Port Townsend, Washington that contains a library of over 1000 **puzzles** rented by a network of puzzle enthusiasts worldwide. Their ultimate business goal is to reduce shipping costs while optimizing for consumer satisfaction. Right now, when an active member of the club finishes a puzzle, they start a return process on the site, which generates a shipping label for the user to ship this puzzle to the next user's location in the overall puzzle network. This next location is determined by a model that considers several factors, such as the puzzle's current location, the next user's location, and the puzzle's rank on the next user's wishlist. 

</p>




## Project Notebooks



```{seealso}

<div class="sidemenu">
  <ul class="sidemenu-entry">
    <i class="fa fa-artistname" aria-hidden="true"></i>
    <code>Preliminary Exploratory Data Analysis </code>
    <li>1.1 Members Data</li> 
    <li>1.2 Packs Data</li>
  </ul>

  <ul class="sidemenu-entry">
    <i class="fa fa-genres" aria-hidden="true"></i>
    <code>Data Cleaning </code>
    <li>2.1 Members Data</li>
    <li>2.2 Packs Data</li>
    <li>2.3 Merged Data </li>
    <li>2.4 Dealing with nulls!!!</li>

  </ul>

  <ul class="sidemenu-entry">
    <i class="fa fa-artistname" aria-hidden="true"></i>
    <code>Feature Engineering </code>
  </ul>

  <ul class="sidemenu-entry">
    <i class="fa fa-myheart" aria-hidden="true"></i>
    <code>Feature Importance </code>
    <li>4.1 OLS Model on complete data</li>
    <li>4.2 LR Model on complete data</li>
    <li>4.3 DT Model on complete data</li>
    <li>4.4 RF Model on complete data</li>
    <li>4.5 Table representing MAE</li>
    <li>4.6 Table representing feature importance</li>

  </ul>

  <ul class="sidemenu-entry">
    <i class="fa fa-length" aria-hidden="true"></i>
    <code>Final Models per person </code>
    <li>5.1 LR model per person</li>
    <li>5.2 DT model per person</li>
    <li>5.3 RF model per person</li>

  </ul>


  
  
</div>
```


## Data Overview

<div class = "mygrid">
<div class = "data">
<span class = "dataset">Data 1. Member Holdtimes</span>
<div class = "myicon 1"></div>
<span class = "vars">Number of Columns: 3</span>
<span class = "vars">Number of Rows: 19733</span>
</div>

<div class = "data">
<span class = "dataset">Data 2. Puzzle Packs</span>
<div class = "myicon 2"></div>
<span class = "vars">Number of Columns: 4</span>
<span class = "vars">Number of Rows: 920</span>
</div>

<div class = "data">
<span class = "dataset">Data 3. Combined Data</span>
<div class = "myicon 3"></div>
<span class = "vars">Number of Columns: 10</span>
<span class = "vars">Number of Rows: 18255</span>
</div>

</div>



### Combined Data Preview



```{code-cell}
:tags: ["hide-input"]
import pandas as pd
member_df = pd.read_csv("data/df_cleaned.csv", header = 0)
member_df.head(4)
```








## Citations




```{bibliography}
:style: plain
```
