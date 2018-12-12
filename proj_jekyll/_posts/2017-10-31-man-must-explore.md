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

Although Panama is miles away from EPFL, the implications from the leaked papers can relate very much to people here in Switzerland and all over the world. In fact Switzerland ranks first in the number of entities set up in offshore jurisdictions at 37911. While setting a company offshore is not a crime, there are illegitimate (and legitimate) implications that drive companies to do so. For instance, business conditions in the home country may be unfavorable from a privacy, bureaucratic, and tax point of view. Despite the fact that we cannot *prove* that companies set up offshore entities for illegal purposes, like tax evasion, it is safe to infer that it is a strong possibility, as even the anonymous leaker "John Doe" stated his intentions were based on growing income inequality and "scale of injustices".

## Our purpose

It is important to dive deeper into the massive corpus of leaked documents [provided here](https://offshoreleaks.icij.org/) to better understand the reasoning why entities choose to set companies offshore so that future cases can be avoided. Furthermore, we will explore the consequences that offshore companies have on home countries from a wealth distribution and corporate tax lost revenue point of view so that readers can really understand the order of magnitude that setting up offshore companies have on their country.

## A world map overview

Companies from a home *country* set up entities in various *jurisdictions* (offshore areas). Thus, we first investigate which *jurisdictions* hold the most entities and which home *countries* set up the most entities offshore.
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

We observe that many of these jurisdictions are located in *tax havens*, or a country with very low taxation rates for foreigners. Furthermore, the majority of countries that have entities in the papers come from a country with favorable business conditions (Hong Kong, Switzerland and Luxembourg) or fiscal paradises (Panama, Jersey). Again these countries have very low taxation rates for foreigners, thus we consider taxation heavily in our analysis in the next section.

## What drives entities to go offshore?

**TO DO**

<iframe src="/proj_jekyll/assets/developpingcountries.html"
    sandbox="allow-same-origin allow-scripts"
    width="100%"
    height="650"
    scrolling="no"
    seamless="seamless"
    frameborder="0">
</iframe>

## What consequences do corporations starting offshore entities have on their home country?

**TO DO**

### Corporate tax revenue

As determined from above, entities are driven to go offshore **potentially** because of lower taxation rates compared to their home country. Note that **correlation does not mean causation and it is hard to prove that companies are evading tax**, but it is a strong reason for going offshore. Thus, we conduct an analysis on the amount of corporate tax revenue lost in a home country under the (strong*) assumption that companies are evading tax.

To do so, we obtained a [dataset from OECD](https://data.oecd.org/tax/tax-on-corporate-profits.htm) indicating the corporate tax rate % of GDP as well as a [dataset from NAICS](https://www.naics.com/business-lists/counts-by-country/) indicating the number of businesses per country. We can then calculate:

![](/proj_jekyll/img/tax_eq.png)


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

<blockquote class="blockquote">The dreams of yesterday are the hopes of today and the reality of tomorrow. Science has not yet mastered prophecy. We predict too much for the next year and yet far too little for the next ten.</blockquote>

<img class="img-fluid" src="https://source.unsplash.com/Mn9Fa_wQH-M/800x450" alt="Demo Image">

<span class="caption text-muted">To go places and do things that have never been done before – that’s what living is all about.</span>
\*maybe not :P
