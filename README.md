# Russian regional economic datasets

##Pseudocode for data import 

Started implementation at [pseudo.py](pseudo.py)


TODO: need test for import results, checking the following - 
```
def_dict0 = {'varname':'PPI_PROM_ytd', 
     'folder':'11 цены производителей', 
   'filename':'индексы цен производителей промышленных товаров.xlsm',
      'sheet':'пром.товаров',
     'anchor':'B5', 'anchor_value': 96.6} 

# df_get_summable_regions
df1 = df_get_all_rows_from_sheet(def_dict0)

# check anchor cell, upper-left corner
assert df1.iloc[0,0] == def_dict0['anchor_value']

# check rows names are equal to testable_sidebar_doc if testign for df_get_summable_regions
# ...

# check some random hardcoded values from datafra,me, including lower right corner
# ...

```

TODO: seprate preparation and algorighm - save publication in 'sourcefiles' folder + unpack + name + import test

```
def get_filename(def_dict):
   return os.path.join(project_root_folder, 'sourcefiles', ...,  def_dict['folder'], def_dict['filename'])
   
assert os.path.exists(get_filename(def_dict0))   

```


1. RAR file downloaded manually 
2. Unpack RAR file to local folder
3. Define a list of imported Excel sheets as a list of source definitions
4. Source definition is: (assinged varname, folder, filename, sheet, optional anchor cell)  
  - *assinged varname* must match/be similar to variables used in <https://github.com/epogrebnyak/rosstat-kep-data>
  - *optional anchor cell* is usually B5 or B6. It is always B column. 
5. Emit a stream of (assinged varname, rown, coln, value) from sheet - use xlrd?
  - may substitute coln, rown with colx, rowx
6. Convert *coln* to date, based on fact that all date ranges start with Jan 2009 (column B = Jan 2009, column C = Feb 2009, etc): ```dt = col_to_date(coln, source_def)```
7. Convert *rown* to region name ```region_name = row_to_region_name(rown, sheet)``` making comparison to reference list of regions.
8. Get dataframes as below:
```    
df1 = df_get_all_rows_from_sheet(source_def)
df2 = df_get_summable_regions(source_def)
df3 = df_get_districts(source_def)
df4 = df_get_RF(source_def)
```
Note: from every sheet can also read a flat stream like (varname, region_name, date, value). 

9. Extend to full dataset as ```rf_df = df_get_all_RF()```
10. Save:
 - all obtained dataframes as sheets in resulting files as tables  RF + districts + summable regions
 - as all-RF data by variable and by date
 - suggested pattern in xls (for SA)
 - list of variables


## Source URL
<http://www.gks.ru/wps/wcm/connect/rosstat_main/rosstat/ru/statistics/publications/catalog/doc_1246601078438>


# Информация для ведения мониторинга социально-экономического положения субъектов Российской Федерации

Материал содержит важнейшие социально-экономические показатели по регионам России, формируемые Росстатом в соответствии с распоряжением Правительства Российской Федерации от 15 июня 2009г. №806-р для мониторинга процессов в реальном секторе экономики, финансово-банковской и социальной сферах субъектов Российской Федерации, а также другие статистические данные, характеризующие текущее социально-экономическое положение субъектов Российской Федерации: индексы промышленного производства, продукции сельского хозяйства, строительства, оборота розничной торговли, платных услуг населению, инвестиций в основной капитал, потребительских цен. Включены показатели, характеризующие финансовую деятельность организаций, просроченную задолженность по заработной плате, денежные доходы населения, а также данные о структуре занятости и ее динамике.
    Представленная информация позволяет оценивать ежемесячные изменения в экономике и социальной сфере субъектов Российской Федерации. 
    Приводятся данные оперативной отчетности, которые уточняются в последующих выпусках. 

«Информация для ведения мониторинга социально-экономического положения субъектов Российской Федерации» выпускается ежемесячно с апреля 2009 года.

График публикации в 2015 году: <http://www.gks.ru/gis/images/graf-oper2015.htm>
