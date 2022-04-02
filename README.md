# The impact of COVID-19 on human mobility pattern and social equity in NYC
Xiaoyi Wu

### Interative map: https://xiaoyi-wu0711.github.io/mobility_web/
This is the draft map which displays temporal changes of people's visit to recreation places in NYC. In the following development, I will integrate 1) total visit count to all places in NYC in different year; 2) mobility changes with socio-economic factors to the map.


## Introduction
As the most populous city in the United States with 8.8 million people distributed over 300.46 square miles (U.S Census Bureau, 2020), New York City has experienced widespread transmission and high infection rate since the first confirmed case on March 1st 2020. 
At the end of March 2020, NYC arrived a peak of COVID-19 and became the pandemic epicenter (Cordes & Castro, 2020) with a weekly mean of 5132 diagnosed cases and 1,566 hospital admissions. 
Identifying the spatio-temporal changes of human mobility pattern before, during and after the peak of COVID-19 is important to analyze COVID-19’s impact on individuals. 
In addition, analyzing mobility changes under the contextual backgrounds suggests the heterogeneity of COVID-19’s impacts on different groups. 
For example, high-income individuals may choose to decrease their visits to wholesale markets and restaurants and buy takeaways services to access necessary foods. 
However, people with low- or moderate- incomes may have no choice but to leave home to buy food with higher risk of infection.

Therefore, this objective of this research is to study the **spatio-temporal changes** of mobility pattern in NYC in March 2019, March 2020 and March 2021 and analyze the **social equity issues** caused by the pandemic. The research is aimed to answer following question:  
1.	What is the spatial distribution of visit counts for different categories? 
2.	What is the temporal change of mobility pattern before, during and after COVID-19?
3.	How do the COVID-19 influence individual's travel behaviors in different contexts?

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

## Expected Results  
 The final deliverable will be a research paper.
 
## Folder Organization
Use `pip install -r requirements.txt` to install packages.
<li>Folder <a href="https://github.com/CPLN-680-Spring-2022/XiaoyiWu-Mobility/tree/main/data"><code>/data</code></a>: with raw data</li>
<li>Folder with <a href="https://github.com/CPLN-680-Spring-2022/XiaoyiWu-Mobility/tree/main/data_save"><code>/data_save</code></a>: processed data based on Python</li>
<li>Folder <a href="https://github.com/CPLN-680-Spring-2022/XiaoyiWu-Mobility/tree/main/scripts"><code>/scripts</code></a>: with Python script code</li>
<ul>
        <li>Script <a href="https://github.com/CPLN-680-Spring-2022/XiaoyiWu-Mobility/blob/main/scripts/1_data_process.ipynb"><code>/1_data_process.ipynb</code></a>: process data</li>
        <li>Script <a href="https://github.com/CPLN-680-Spring-2022/XiaoyiWu-Mobility/blob/main/scripts/2_demographic_merge.ipynb"><code>/2_demographic_merge.ipynb</code></a>: visualize the demographic background and mobility pattern in the study area</li>
        <li>Script <a href="https://github.com/CPLN-680-Spring-2022/XiaoyiWu-Mobility/blob/main/scripts/3_business_category_year.ipynb"><code>/3_business_category_year.ipynb</code></a>: analyze the temporal changes of people's vists to POIs in different categories </li>
        <li>Script <a href="https://github.com/CPLN-680-Spring-2022/XiaoyiWu-Mobility/blob/main/scripts/utils.py"><code>/utils.py</code></a>: functions commonly used for above folders</li>
</ul>
<li><a href="https://github.com/CPLN-680-Spring-2022/XiaoyiWu-Mobility/tree/main/fig"><code>/fig</code></a>:saved figures</li>
<li><a href="https://github.com/CPLN-680-Spring-2022/XiaoyiWu-Mobility/tree/main/doc"><code>/doc</code></a>: slides and reports</li>

</p>

