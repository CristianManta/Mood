# Mood
A data analysis project consisting of a Python script that maps 5 dimensional data to a 2 dimensional subspace using PCA (principal component analysis) to visualize the essence of its variability. 

The script then colors the projected data according to the response variable, the mood rating (0 - 10), and adds vectors associated to an increase in each original feature. The end goal is to be able to visualize the most important factors that influence the mood of a person by collecting survey data over a long enough period of time.

The 5 features are:

* Sleep quality rating from the night before (0 - 10) --> sq
* Time spent interacting socially (hours) --> si
* Time spent exercising (hours) --> e
* Satisfaction with daily goals (0 - 10) --> gs
* Stress levels rating (0 - 10) --> s

## Illustration
I generated fake data with 8 entries where the person's mood would mostly be improved by better sleep quality and exercise time, and worsened by a sense of goals satisfaction (I know, totally unrealistic, but I wanted to test the contrast), and where stress and social interaction have little impact. It can be found here: [mock.csv](/analysis/mock.csv).


One can arrive at the same conclusions by examining the following plot generated by the script with this input data: the arrow corresponding to goals satisfaction points towards the region with lower mood rating while the arrows corresponding to sleep quality and time spent exercising point towards the region associated with higher mood rating. In contrast, the arrows corresponding to social interaction and and stress point in directions where the mood rating changes the slowest.

![example](/analysis/plot.png)
