# Title

# Abstract
A 150 word description of the project idea, goals, dataset used. What story you would like to tell and why? What's the motivation behind your project?

The Panama Papers are the biggest leak of data in recent history. They are still under exploration, but they have already thrown light on the size of the transaction companies carry out by means of off-shore holdings. This is particularly relevant for the team since we believe that in such a globalized and open world it is crucial to be able to redistribute wealth among the population. Failing to do so will only increase income inequality. For this reason, increasing people’s awareness on the issue will empower them to make conscious consumption decisions: understanding to what extent wealth is hidden in offshore tax haven, which countries are most affected and which are the biggest players involved in the scandal is fundamental to understand the complexity of the issue and make a change. 


# Research questions
A list of research questions you would like to address during the project. 
We have a bunch of research questions we would like to investigate through this project. Below are starter questions which we may augment/delete/add to as the project progresses:
 - Is there a correlation between country statistics such as Gini coefficient or HDI and the number of country representatives in the Panama Papers?
 - What are the roles of Fortune 500 companies in the papers?
 - How do the timeline of leaked papers look like over the years? Are peaks/valleys associated with certain events at the time?
 - What does the map of the biggest tax havens in the world look like?
 - Which countries are most heavily involved with the leaked papers?
 - What is the estimated amount of “lost capital” in a country due to tax evasion of the biggest companies in that country? How do the amounts compare?
 - What does the black market or organized crime play in relation to the Panama Papers?


# Dataset
List the dataset(s) you want to use, and some ideas on how do you expect to get, manage, process and enrich it/them. Show us you've read the docs and some examples, and you've a clear idea on what to expect. Discuss data size and format if relevant.

 - Forbes Top 2000 Companies
 - Panama Papers dataframe on the cluster
 
The panama paper data frame provided is already pretty clean. 4 different csv files are logically connected by a link file. This would allowed a easy making of the links between the single dataframe and query solving. CSV extension can be easly handle with different python libraries. Following one possible research question it is possible incorporate more data for each country mentioned in the papers, like Gini index or GDP. Data size seems not too critical; during the first queries it would be decide of to use spark or not.


# A list of internal milestones up until project milestone 2
Add here a sketch of your planning for the next project milestone.

 - Deadline 1, 10 Nov: Merging Panama Paper sources with top 2000 companies and carry out descriptive statistics on number of companies that have gone offshore during the years, distribution of companies listed per country, checking how many of the top 2000 companies listed are in the Panama Papers
 - Deadline 2, 17 Nov: Select the top companies present in the Panama Papers and draft a model to estimate the amount if resources they take out from their countries based on their profit/ market-share. In this way the pipeline will be completed
 - Deadline 3, 25 Nov: Investigate the possibility of making a network of biggest intermediators using the nodes provided in the data using a graph database


# Questions for TAa
Add here some questions you have for us, in general or project-specific.

- The Panama Papers are on the spark cluster but on the spreadsheet it says that it is not? Any clarification on the inconsistency? 



