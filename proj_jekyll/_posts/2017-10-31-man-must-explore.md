---
layout: post
title:  "PANAMA PAPERS"
subtitle: "An exploration"
background: '/img/posts/06.jpg'
---
<style>
  .df_jc{
    float:left;
  }
  .jc{
    display:block;
    margin-left: auto;
    margin-rightL auto
  }
  img {
  display: block;
  margin-left: auto;
  margin-right: auto;
  }
</style>

## Introduction

In 2015, the world was shook from the news over a leaked corpus of 11.5 million financial and attorney-client documents relating to over 200,000 offshore entities called the **Panama Papers**. These documents were created by, and taken from, Panamanian law firm and corporate service provider Mossack Fonseca, and were leaked by an anonymous source.

## Why should I care?

Although Panama is miles away from EPFL, the implications from the leaked papers can relate very much to people here in Switzerland and all over the world. In fact Switzerland ranks first as country with the highest number of entities set up in offshore jurisdictions (37911 entities). While setting a company offshore is not a crime, there are illegitimate (and legitimate) implications that drive companies to do so. For instance, business conditions in the home country may be unfavorable from a privacy, bureaucratic, and economical point of view. On top of that there are not only companies which move offshore, but also individuals which for multiple reasons move their funds offshore.  Despite the fact that we cannot *prove* that companies set up offshore entities for illegal purposes, like tax evasion, it is safe to infer that it is a strong possibility, as even the anonymous leaker "John Doe" [stated](https://panamapapers.sueddeutsche.de/articles/572c897a5632a39742ed34ef/) his intentions were based on growing income inequality and "scale of injustices".

## Our purpose

It is important to dive deeper into the massive corpus of leaked documents [provided here](https://offshoreleaks.icij.org/) to better understand the reasons which influence entities and mainly companies to set holdings offshore. Furthermore, we will explore the consequences that offshore companies have on home countries from a wealth distribution and corporate tax lost revenue point of view so that readers can really understand the order of magnitude that setting up offshore companies have on their country.

## A world map overview

Companies from a home *country* set up entities in various *jurisdictions* (offshore areas). Thus, we first investigate which *jurisdictions* hold the most entities and which home *countries* set up the most entities offshore. These information will be extremely important on the one hand to understand what are the jurisdictions which offer optimal privacy and business conditions to the entities and on the other hand from which countries mostly entities set up offshore companies. The second information, in particular, is pivotal to later find out the reasons influencing entities to go offshore.
<iframe src="/proj_jekyll/assets/jurisdictions_map.html"
    sandbox="allow-same-origin allow-scripts"
    width="100%"
    height="440"
    scrolling="no"
    seamless="seamless"
    frameborder="0">
</iframe>
<iframe src="/proj_jekyll/assets/country_map.html"
    sandbox="allow-same-origin allow-scripts"
    width="100%"
    height="440"
    scrolling="no"
    seamless="seamless"
    frameborder="0">
</iframe>

We observe that many of these jurisdictions are located in *tax havens*, or a country with very low taxation rates for foreigners. Furthermore, the majority of countries that have entities in the papers come from a country with favorable business conditions (Hong Kong, Switzerland and Luxembourg) or fiscal paradises (Panama, Jersey). These countries are very business friendly: in other words they have extremely low tax rate and fot this reason they are called tax havens.
But why would entities already in tax havens go offshore if the business conditions from the country they come from are already optimal? And most importantly, what are the reasons pushing entities in non tax paradises countries to go offshore?

It seems clear that corporate tax level is a strong determinant for entities to set up their business in tax havens. But is it also the reason for which entities from non tax havens set up holding in offshore jurisdictions?

## What drives entities to go offshore?

It is probable that entities from all over the world are firstly influenced to go set their businesses already in countries which offer particularly good business conditions such as Switzlerand, Panama, the Channel Islands (Jersey and Guernsey), Luxemburg, the Cayman Islands, Lichteinstein, Singapore and Monaco, Isle of Man and Gibraltar. These countries are known for being small and very developped with high income per capita, but also to often be tax havens. 


Hence, on the one hand it is crucial to understand what are these business conditions (economic and bureaucratic) that make this set of countries the optimum place to do business, but also to easily go offshore and on the other hand what are the economic and bureaucratic causes which influence entities in the other countries to go offshore. 

Firstly the corporate tax rate in small developed countries is plotted against the number of entities offshore per country in log scale.
By observing the plot below some important considerations can be drawn; two set of countries can be identified: tax havens countries and small developed countries. Firstly the tax havens countries can be identified very easily since they have a high presence in the papers and at the same time they have really low tax rates. The rest of the countries are small developed usually European countries. The trend of non tax havens countries shows that high tax rate is not a factor pushing entities to go offshore; in fact the opposite could be true: there seems to be a negative exponential relationship between presence in panama papers and tax rates, but the two tail test p-value of such relationship seems to imply that no relationship exist between tax rate and number of entities in Panama Papers for small developed countries. However this relationship could imply the presence of an hidden covariate: high tax rate might be synonym of tighter control and regulations on entities going offshore, meaning that countries with tighter controls will naturally have a lower number of offshore companies.

In addition the graph also seems to suggest that the reasons behind the presence of many companies offshore in tax havens is not only the low taxation levels: in fact corporate tax rate of tax havens countries is often comparable to that one of other small european countries. As a matter of fact tax havens countries offer entities favorable conditions to easily set companies offshore compared to other small countries.


PLACE FIG

Now that we have understood what is the relationship between corporate tax rate and presence in Panama Papers for small developed countries, the graph of tax rate and presence in Panama Paper of developping countries is plotted. 

By observing this graphs a negative exponential relationship can be again observed further showing that for this category of countries tax rate is not a factor pushing entities to go offshore: actually the higher the tax rate the lower the number of companies offshore. Contrary to the little evidence found in small developped countries, developping countries show a very clear negative exponential relationship with a two tails p-value of 0.00143. This could be a further proof to the hypothesis that higher tax rates are correlates with higher regulations as shown in the graph for small developped countries; in fact in developping countries the bureaucratic machine and regulation could even disable further entities who are willing to go offshore.

<iframe src="/proj_jekyll/assets/developpingcountries.html"
    sandbox="allow-same-origin allow-scripts"
    width="100%"
    height="650"
    scrolling="no"
    seamless="seamless"
    frameborder="0">
</iframe>

Finally the relationship between the 7 biggest economies and tax rate has been investigated. The economies almost correspond to the G7 countries, but China has taken the place of Canada. 

The figure below shows a completely different picture, compared to the previous ones: taking out Japan, it seems to be a positive exponential relationship between tax rate and number of offshore entities for the economically strongest countries suggesting that in these countries (p-value=0.531), entities are escaping corporate taxation levels by putting their companies offshore. Japan represents an exception among the 7 biggest economies: even though it has a very high tax rate, the presence of Japanese entities in the documents is really low. This could be due to cultural reasons or might be due to the fact that Japanese entities use different means to go offshore and they are not very represented in the Panama Papers themselves.

PLACE FIG

In conclusion it is clear that corporate tax is definitely a factor influencing entities to go offshore, but in different ways according to the set of countries considered. It seems that entities in the major economies are trying to escape high corporate taxation levels. While it seems that lower taxation levels in developing countries implies a higher number of companies set offshore. However it is hard to make inference statements since the correlations are often not strong enough and correlation doesn't imply causation.
 
 Hence corporate tax rate is not the only determinant for entities to go offshore: in fact it was also concluded that corporate tax rate could actually be a proxy variable for other covariates. For instance it is clear that tax havens present ideal conditions for entities to set up offshore companies: additional research should be performed in finding what are theses bureaucratic and economical factors, but the lack of transparency of these countries makes it extremely to find useful data. 
## What consequences do corporations starting offshore entities have on their home country?

### Corporate tax revenue

As determined from above, entities are driven to go offshore **potentially** because of lower taxation rates compared to their home country. Note that **correlation does not mean causation and it is hard to prove that companies are evading tax**, but it is a strong reason for going offshore. Thus, we conduct an analysis on the amount of corporate tax revenue lost in a home country under the (strong*) assumption that companies are evading tax.

To do so, we obtained a [dataset from OECD](https://data.oecd.org/tax/tax-on-corporate-profits.htm) indicating the corporate tax rate % of GDP as well as a [dataset from NAICS](https://www.naics.com/business-lists/counts-by-country/) indicating the number of businesses per country. We can then calculate:


<!-- $$
Potential~Tax~Lost_{country} = \frac{Corporate~Tax~Revenue_{country}}{\#~Businesses_{country}} \times \#~ entities~in~PP_{country}
$$ -->

Below is a graph for the top 15 countries in terms of potential corporate tax revenue loss in USD:

<iframe src="/proj_jekyll/assets/tax_loss.html"
    sandbox="allow-same-origin allow-scripts"
    width="100%"
    height="550"
    scrolling="no"
    seamless="seamless"
    frameborder="0">
</iframe>

As seen from the graph, aside from Switzerland, many of the countries are not losing that much corporate tax revenue when compared to their actual corporate tax revenue. This may be because usually only large businesses with high profits have the motivation to transfer their money overseas, as they pay a larger percentages in home corporate tax. Thus they would average a higher `Avg tax per business` and consequently increase overall `Potential corporate tax loss`. Thus the graph above may be an **underestimation** of the actual potential tax evasion. Nonetheless, a large amount of tax revenue (especially in Switzerland) is potentially lost, which can be used for the government to reinvest in their country. Overall the impact of offshore entities appearing in the Panama Papers can have real big effect towards the home country in terms of lost capital!

## What about staying onshore?
 
The exploration above has provided numerous insights not only on the causes influencing entities to go offshore, but also on the consequences that such practises have on the home countries and could have on world income inequality in the long run, as the unknown leaker as mentioned. Some of the causes behind going offshore can be explained with data; in fact further researches are needed to obtain a greater quantity of data and use them to explore which are determinants of the number of offshore companies. In addition the phenomenon is also a sociological one and the story of each entity should be treated separately. All in all a stakeholder analysis should be performed to understand which are the individuals that, hidden behind the privacy curtains of the offshore jurisdictions, evade taxation disabling a proper redistribution of wealth. 

PLACE FIG





