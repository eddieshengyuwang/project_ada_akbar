# Title

# Abstract
A 150 word description of the project idea, goals, dataset used. What story you would like to tell and why? What's the motivation behind your project?

The Panama Papers are the biggest leak of data in recent history. They are still under exploration, but they have already thrown light on the size of the transaction companies carry out by means of off-shore holdings. This is particularly relevant for the team since we believe that in such a globalized and open world it is crucial to be able to redistribute wealth among the population. Failing to do so will only increase income inequality. For this reason, increasing people’s awareness on the issue will empower them to make conscious consumption decisions: understanding whether the discrepancy between ease of business that exist between tax haven countries and non tax havens, can be a cause of high income inequality in non tax haven countries is fundamental. 


# Research questions

 
**To what extent tax heavens and business friendly regulations attract companies from all over the world and contribute to the income inequality in the home countries?**
In order to answer the above question, the following subquestion have to be answered:

**1)** Which are the jurisdictions in which entities found in Panama papers are registered?

**2)** What countries have the most entities register in the Panama papers?

**3)** What are the burocratic and economic causes pushing entities to go offshore?

**4)** How does the number of entities in a country which are mentioned in the Panama papers reflect with the income inequality within a country?

**Interpretation of the Panama Papers**
As shown by the exploratory analysis, the entity document of the Panama Papers is very interesting: it provides a macroscopic view of how many entities per countries are involved in settling companies offshore or funds offshore. The reasons behind making an offshore company are multiple: setting a company offshore is not a crime, but it can be an indication that the business condition in the home country are not always favorable from a privacy point of view, from a bureaucratic point of view and from a tax point of view. Hence it is crucial to understand why entities decide to set their companies offshore and what is the consequence on the home country from a wealth distribution point of view.


# Dataset
List the dataset(s) you want to use, and some ideas on how do you expect to get, manage, process and enrich it/them. Show us you've read the docs and some examples, and you've a clear idea on what to expect. Discuss data size and format if relevant.

 - Panama Papers dataframe on the cluster
 
 All the following are downloaded from [World Bank Dataset](https://data.worldbank.org)
 - GINI coefficient per country
 - GDP per country
 - GDP per capita per country
 - Time to start a business per country
 - Time spent by business in government regulation per country
 - Tax rate per country 

The discussion about the data size and format is carried out inside the notebook.

# Group memebers contributions 
 - **Gianluca Mancini:** Dataframe preparation, Corporate Tax Rate (all subsections) and Various descriptions.
 - **Tullio Nutta:** Imports, Juristiction and Country counts, GDP data integration, Time dependence between entities presence in Panama Papers, economic indicators and GINI coefficient and Various descriptions.
 - **Eddie Wang:** Handling data size, Understanding the data, Data cleaning, Juristiction and Country counts map visualization, OECD Corporate Tax: Amounts Lost and Various descriptions.

# Libraries required
 - Numpy - 1.14.3
 - Pandas - 0.23.0
 - Seaborn - 0.8.1
 - Scipy - 1.1.0
 - Matplotlib.pyplot - 2.2.2
 - Bokeh - 0.12.16
 - Geopy - 1.17.0


