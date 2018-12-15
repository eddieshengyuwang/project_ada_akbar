# THE PANAMA PAPERS

## Link to data story
The data story can be found at [this link](https://ada-akbar.github.io/2018/12/13/panama-papers.html).

# Abstract

The Panama Papers are the biggest leak of data in recent history. They are still under exploration, but they have already thrown light on the size of the transaction companies carry out by means of off-shore holdings. This is particularly relevant for the team since we believe that in such a globalized and open world it is crucial to be able to redistribute wealth among the population. Failing to do so will only increase income inequality. For this reason, increasing people’s awareness on the issue will empower them to make conscious consumption decisions: understanding whether the discrepancy between ease of business that exist between tax haven countries and non tax havens, can be a cause of high income inequality in non tax haven countries is fundamental. 


# Research questions

**Interpretation of the Panama Papers**
As shown by the exploratory analysis, the entity document of the Panama Papers is very interesting: it provides a macroscopic view of how many entities per countries are involved in settling companies offshore or funds offshore. The reasons behind making an offshore company are multiple: setting a company offshore is not a crime, but it can be an indication that the business condition in the home country are not always favorable from a privacy point of view, from a bureaucratic point of view and from a tax point of view. Hence it is crucial to understand why entities decide to set their companies offshore and what is the consequence on the home country from a wealth distribution point of view.

**1)** Which are the jurisdictions in which entities found in Panama papers are registered?

**2)** What countries have the most entities register in the Panama papers?

**3)** What drives entities to go offshore and consequently how does that affect the country? 

**4)** What are the consequences of offshore companies on income inequality?



# Dataset

List the dataset(s) you want to use, and some ideas on how do you expect to get, manage, process and enrich it/them. Show us you've read the docs and some examples, and you've a clear idea on what to expect. Discuss data size and format if relevant.

 - Panama Papers dataframe on the cluster
 
 The following are downloaded from [World Bank Dataset](https://data.worldbank.org)
 - GINI coefficient per country
 - GDP per country
 - GDP per capita per country
 - Time to start a business per country
 - Time spent by business in government regulation per country
 - Tax rate on income, profits and capital gains per country 
 
 The following are downloaded from [Organisation for Economic Co-operation and Development (OECD) database](https://data.oecd.org/)
 - Corporate tax rate per country from 2000
 - Number of businesses per country

The discussion about the data size and format is carried out inside the notebook.

# Group memebers contributions 
 - **Gianluca Mancini:** Dataframe preparation, Tax Rate (all subsections) and Various descriptions. Data story writing.
 - **Tullio Nutta:** Imports, Juristiction and Country counts, GDP data integration, Time dependence between entities presence in Panama Papers, economic indicators and GINI coefficient and Various descriptions.
 - **Eddie Wang:** Handling data size, Understanding the data, Data cleaning, Juristiction and Country counts map visualization, OECD Corporate Tax: Amounts Lost and Various descriptions. Data story coding.
 
### Final presentation
- *Presentation*: Gianluca Mancini 
- *Poster*: Tullio Nutta

# Libraries required
 - Numpy - 1.14.3
 - Pandas - 0.23.0
 - Seaborn - 0.8.1
 - Scipy - 1.1.0
 - Matplotlib.pyplot - 2.2.2
 - Bokeh - 0.12.16
 - Geopy - 1.17.0


