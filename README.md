# Mood
A data analysis project consisting of a Python script that maps data consisting of 5 features to a 2 dimensional subspace using PCA (principal component analysis) to determine which directions explain the most varibility in the data. 

The script then colors the projected data according to the response variable, the mood rating (0 - 10), and adds vectors associated to an increase in each original feature. The end goal is to be able to visualize the most important factors that influence the mood of a person by collecting survey data over a long enough period of time.

The 5 features are:

* Sleep quality rating from the night before (0 - 10) --> sq
* Time spent interacting socially (hours) --> si
* Time spent exercising (hours) --> e
* Satisfaction with daily goals (0 - 10) --> gs
* Stress levels rating (0 - 10) --> s

## Illustration
I generated fake data with 8 entries where the person's mood would mostly be improved by better sleep quality and exercise time, and worsened by a sense of goals satisfaction (I know, totally unrealistic, but I wanted to test the contrast), and where stress and social interaction have little impact. This is the resulting plot. The data can be found here: [mock.csv](/analysis/mock.csv).

![example](/analysis/plot.png)
