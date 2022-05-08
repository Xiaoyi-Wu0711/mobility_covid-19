# The impact of COVID-19 on human mobility pattern and social equity in NYC
Xiaoyi Wu

### Interative map: https://xiaoyi-wu0711.github.io/mobility_web/
This is the draft map which displays temporal changes of people's visit counts to different business type in March 2019, March 2020 and March 2021. 
There I display: 
- the spatial distribution of human mobility
- the temporal changes of human mobility 
- the distribution of socio-economic factors in NYC


## Introduction
As the most populous city in the United States with 8.8 million people distributed over 300.46 square miles (U.S Census Bureau, 2020), New York City has experienced rapid and widespread transmission since the first confirmed case on March 1st 2020. At the end of March 2020, NYC arrived at the peak of COVID-19 and became the pandemic epicenter (Cordes \& Castro, 2020) with a weekly mean of 5132 diagnosed cases and 1,566 hospital admissions. On March 22, 2020, 'New York State on PAUSE' executive order was declared. It includes a new directive that all non-essential businesses statewide must close in-office personnel functions effective (New York State Official Website, 2020). Identifying the spatio-temporal changes of human mobility pattern before, during and after the outbreak of COVID-19 is important in order to analyze COVID-19’s impact on individuals. In addition, analyzing mobility changes under the contextual backgrounds suggests the heterogeneity of COVID-19’s impacts on different groups. 
For example, high-income individuals may choose to decrease their visits to wholesale markets and restaurants and buy takeaways services to access necessary foods. 
However, people with low- or moderate- incomes may have no choice but to leave home to buy food with higher risk of infection.

Therefore, the objective of this paper is to study the spatio-temporal changes of mobility pattern in NYC in March 2019, March 2020 and March 2021 and analyze the social equity issues caused by the pandemic. The research is aimed to answer the following questions: 
1. What is the spatial shifting pattern of visit counts to different business categories? 
2. What is the temporal change of mobility pattern before, during and after COVID-19?
3. How does COVID-19 influence individual's travel behaviors in different contexts?

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

1. Manhattan Borough was found the most popular places all the time, even it experience largest
degree in visit counts during the pandemic. Low-income people suffer larger economic loss and higher risk of
COVID-19 transmission due to mobility movement, which exposes the social inequity issues in NYC
2. There is disparity in the human mobility during the COVID-19. 
   1. People tend
   to decrease their visits to low-income areas, which indicates the business in these neighborhoods were
   hit hardest during the first month of the COVID-19 by correlation analysis. 
   2. Low-income groups tend to have more visits to low-income and low education attainment
   areas where were found the most confirmed virus cases in March 2020. 
   3. High-income groups have more visits to Lower Manhattan, Staten Island. There was a significant
increase in Staten Island and outskirt of southeast shore of Brooklyn and north end of Queens Borough.
Most of these places are high-income, high education attainment and high vacancy rate areas. They
were also found to have less confirmed case rate in the first month of COVID-19.

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
    <li>Script <a href="https://github.com/Xiaoyi-Wu0711/mobility_covid-19/blob/main/doc/report.pdf"><code>/report.pdf></a>: final report</li>

</ul>
</p>

