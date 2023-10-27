# The impact of COVID-19 on human mobility pattern and social equity in NYC
Xiaoyi Wu

### Interative map: https://xiaoyi-wu0711.github.io/mobility_web/
This is the draft map which displays temporal changes of people's visit counts to different business type in March 2019, March 2020 and March 2021. 
There I display: 
- the spatial distribution of human mobility
- the temporal changes of human mobility 
- the distribution of socio-economic factors in NYC

### Report: https://github.com/Xiaoyi-Wu0711/mobility_covid-19/blob/main/doc/report.pdf


## Abstract
#### Background:
Human mobility is critical to understand, evaluate, predict and control the transmission of COVID-19.

#### Research Gap: 
Based on previous work, this study built a comprehensive understanding of COVID-19’s influence on human mobility and social equity at micro level with cell-phone tracked Point of Interest data, and provided a quantitive evidence of underlying disparity in New York emergency response system.

#### Methods:
Spatiotemporal analysis of human mobility from the pre-outbreak of COVID-19 to reopening phrases in New York City was conducted to detect the uneven changes of travel behaviors and travel purpose under different education, income, racial and age contexts. Sets of time-varying linear regression models were generated to examine the varied association between social-economic factors, COVID-19 cases and human mobility at different pandemic stages. 

#### Results
Results revealed the consistency of COVID-19’s impact on travel reduction and the heterogeneity on individual response in different social-economic groups. For example, during the outbreak of COVID-19, significant decrease in visit counts was observed cross the city. However, people from bottom-quartile household income areas suffered higher transmission risk with the less decreasing degree in human mobility to gain necessary needs and service, while people from top-quartile income groups were exposed to lower transmission risk with increasing trend to move to suburban areas.

## Data

|     Data     | Geographic Level |           Source            | 
| :------------: | :------------------------: | :------------------------: | 
|    Mobility Pattern Data   | Block Group  |    [SafeGraph](https://www.safegraph.com/)    | 
| Core Place Data | Block Group  |     [SafeGraph](https://www.safegraph.com/)             | 
| Demographic Data e.g. median income, race | Census Tract |     [ACS 2019 5-year data](https://www.census.gov/data/developers/data-sets/acs-5year.html)       |
| Geographic boundary Data | Census Tract |   [US Census Bureau](https://www1.nyc.gov/site/planning/data-maps/open-data/census-download-metadata.page)       |  


## Methods
- Analyzing the spatial distribution of human mobility 
- Comparing the spatial pattern of human mobility before/during/after COVID-19
- Analyzing people's mobility pattern and access to necessary services in different contexts
  
## Conclusion
1. There is a general reduction trend in human mobility during the pandemic and this decreasing trend was maintained through to the March of 2021(Figure 1). Particularly,
visits to necessary goods and services including transportation, education, health care, wholesale and
retail(Table 2), and food saw a significant decrease.

2. Manhattan Borough was found the most popular place all the time, even it experienced largest
decrease in visit counts during the outbreak of COVID-19.

2. There is disparity in the human mobility during the COVID-19. Bottom-quartile income people suffer higher economic loss and higher risk of
COVID-19 transmission due to mobility, which exposes the social inequity issues in NYC.
   1. People tend
   to decrease their visits to low-income areas in large degree such as Upper Manhattan, which indicates the business in these neighborhoods were
   hit hardest during the first month of the COVID-19. 
   2. Bottom-income groups tend to have more visits to low-income and low education attainment
   areas where were found the most confirmed virus cases in March 2020. 
   3. Top-income groups have more visits to Lower Manhattan, Staten Island, which are high-income and high education attainment areas. There was even a significant increase
in Staten Island and outskirt of southeast shore of Brooklyn and north end of Queens Borough in
March 2020. Since these places have high vacancy ratewith low confirmed case
rate in the first month(Buchanan et al., 2020), this indicates top-income groups migrated to
outskirt of the city during the outbreak of COVID-19.
   4. bottom-income groups of people was found have more smaller decrease degree of visit
counts during the outbreak of COVID-19 and larger decrease degree after COVID-19 compared to
top-income groups. Particularly, bottom-income people have smaller decrease to visit count of food,
health care, wholesale and retail, transportation and education POIs in the first month of COVID-19.
This indicates bottom-income people need to leave home to purchase necessary goods, services and
work to secure thier daily living.

## Expected Results  
 The final deliverable will be a research paper and a dashboard.
 
## Folder Organization
Use `pip install -r requirements.txt` to install packages.
<li>Folder <a href="https://github.com/CPLN-680-Spring-2022/XiaoyiWu-Mobility/tree/main/data"><code>/data</code></a>: with raw data</li>
<li>Folder with <a href="https://github.com/CPLN-680-Spring-2022/XiaoyiWu-Mobility/tree/main/data_save"><code>/data_save</code></a>: processed data based on Python</li>
<li>Folder <a href="https://github.com/CPLN-680-Spring-2022/XiaoyiWu-Mobility/tree/main/scripts"><code>/scripts</code></a>: with Python script code</li>
<ul>
        <li>Script <a href="https://github.com/CPLN-680-Spring-2022/XiaoyiWu-Mobility/blob/main/scripts/1_data_process.ipynb"><code>/1_data_process.ipynb</code></a>: process data</li>
        <li>Script <a href="https://github.com/CPLN-680-Spring-2022/XiaoyiWu-Mobility/blob/main/scripts/2_demographic_merge.ipynb"><code>/2_demographic_merge.ipynb</code></a>: visualize the demographic background and mobility pattern in the study area</li>
        <li>Script <a href="https://github.com/CPLN-680-Spring-2022/XiaoyiWu-Mobility/blob/main/scripts/3_business_category_year.ipynb"><code>/3_business_category_year.ipynb</code></a>: analyze the temporal changes of people's vists to POIs in different categories </li>
        <li>Script <a href="https://github.com/Xiaoyi-Wu0711/mobility_covid-19/blob/main/scripts/4_ori_dest_pair.ipynb"><code>/4_ori_dest_pair.ipynb</code></a>: construct original-destination matrix and calculate the flow volume change in income contexts during COVID-19</li>
        <li>Script <a href="https://github.com/Xiaoyi-Wu0711/mobility_covid-19/blob/main/scripts/5_ori_dist_category.ipynb"><code>/5_ori_dist_category.ipynb</code></a>: calculate the flow volume change to necessary goods/service in income contexts during COVID-19</li>
        <li>Script <a href="https://github.com/Xiaoyi-Wu0711/mobility_covid-19/blob/main/scripts/6_js__visit_count_business.ipynb"><code>/6_js__visit_count_business.ipynb</code></a>: data preparing for dashboard visualization</li>
        <li>Script <a href="https://github.com/Xiaoyi-Wu0711/mobility_covid-19/blob/main/scripts/7_regression.ipynb"><code>/7_regression.ipynb.ipynb</code></a>: data preparing for coefficient analysis</li>
</ul>
<li><a href="https://github.com/Xiaoyi-Wu0711/mobility_covid-19/blob/main/fig/"><code>/fig</code></a>:saved figures</li>
<li><a href="https://github.com/Xiaoyi-Wu0711/mobility_covid-19/blob/main/doc/"><code>/doc</code></a>: slides and reports</li>
<ul>
    <li>Script <a href="https://github.com/Xiaoyi-Wu0711/mobility_covid-19/blob/main/doc/report.pdf"><code>/report.pdf</a>: final report</li>

</ul>
</p>

