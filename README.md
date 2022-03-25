# The impact of COVID-19 on human mobility pattern in NYC
Xiaoyi Wu

## Introduction
As the most populous city in the United States with 8.8 million people distributed over 300.46 square miles (U.S Census Bureau, 2020), New York City has become the pandemic epicenter (Cordes & Castro, 2020) since the first confirmed case on March 1st. Especially, under the setting of holiday and Omicron variant, NYC experienced unprecedented transmission speed at 2022 New Year’s Eve. This study focuses on the spatio-temporal analysis of human mobility pattern in NYC to study COVID-19’s impact on travel behaviors, and social equity analysis in different contexts to help the government properly response to public health emergencies.

## Data
This study uses the smart-device pattern data from December to January in 2019-2020, 2020-2021, 2021-2022 from SafeGraph. In addition, this study collect ACS 2019 5-year data to analyze mobility pattern in different race and income contexts to discuss the social equity issues and make policy implications of travel restrictions for the local government. 

Instead of collecting data of ZCTA level at first, I gather the data of census tract level since this is much more precise. Here is the data source:
|     Data     | Geographic Level |           Source            | 
| :------------: | :------------------------: | :------------------------: | 
|    Mobility Pattern Data   | Block Group  |    [SafeGraph](https://www.safegraph.com/)    | 
| Core Place Data | Block Group  |     [SafeGraph](https://www.safegraph.com/)             | 
| Demographic Data e.g. median income, race | Census Tract |     [ACS 2019 5-year data](https://www.census.gov/data/developers/data-sets/acs-5year.html)       |
| Geographic boundary Data | Census Tract |   [US Census Bureau](https://www1.nyc.gov/site/planning/data-maps/open-data/census-download-metadata.page)       |  

Table 1.  Data

## Methods
- Analyzing the spatial shifting pattern of human mobility 
- Comparing the spatial pattern of human mobility before and after COVID-19's outbreak
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

