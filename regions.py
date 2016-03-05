district_names  = ['Центральный федеральный округ',
                   'Северо-Западный федеральный округ',
                   'Южный федеральный округ',
                   'Северо-Кавказский федеральный округ',
                   'Приволжский федеральный округ', 
                   'Уральский федеральный округ', 
                   'Сибирский федеральный округ', 
                   'Дальневосточный федеральный округ', 
                   'Крымский федеральный округ']
assert len(district_names) == 9

rf_name = "Российская Федерация"

# changed to unordered list
reference_region_names = ['Российская Федерация',
  'Центральный федеральный округ',
  'Белгородская область',
  'Брянская область',
  'Владимирская область',
  'Воронежская область',
  'Ивановская область',
  'Калужская область',
  'Костромская область',
  'Курская область',
  'Липецкая область',
  'Московская область',
  'Орловская область',
  'Рязанская область',
  'Смоленская область',
  'Тамбовская область',
  'Тверская область',
  'Тульская область',
  'Ярославская область',
  'г. Москва',
  'Северо-Западный федеральный округ',
  'Республика Карелия',
  'Республика Коми',
  'Архангельская область',
  'Ненецкий авт. округ',
  'Архангельская область без авт. округа',
  'Вологодская область',
  'Калининградская область',
  'Ленинградская область',
  'Мурманская область',
  'Новгородская область',
  'Псковская область',
  'г. Санкт-Петербург',
  'Южный федеральный округ',
  'Республика Адыгея',
  'Республика Калмыкия',
  'Краснодарский край',
  'Астраханская область',
  'Волгоградская область',
  'Ростовская область',
  'Северо-Кавказский федеральный округ',
  'Республика Дагестан',
  'Республика Ингушетия',
  'Кабардино-Балкарская Республика',
  'Карачаево-Черкесская Республика',
  'Республика Северная Осетия - Алания',
  'Чеченская Республика',
  'Ставропольский край',
  'Приволжский федеральный округ',
  'Республика Башкортостан',
  'Республика Марий Эл',
  'Республика Мордовия',
  'Республика Татарстан',
  'Удмуртская Республика',
  'Чувашская Республика',
  'Пермский край',
  'Кировская область',
  'Нижегородская область',
  'Оренбургская область',
  'Пензенская область ',
  'Самарская область',
  'Саратовская область',
  'Ульяновская область',
  'Уральский федеральный округ',
  'Курганская область',
  'Свердловская область',
  'Тюменская область',
  'Ханты-Мансийский авт. округ - Югра',
  'Ямало-Ненецкий авт. округ',
  'Тюменская область без авт. округов',
  'Челябинская область',
  'Сибирский федеральный округ',
  'Республика Алтай',
  'Республика Бурятия',
  'Республика Тыва',
  'Республика Хакасия',
  'Алтайский край',
  'Забайкальский край',
  'Красноярский край',
  'Иркутская область',
  'Кемеровская область',
  'Новосибирская область',
  'Омская область',
  'Томская область',
  'Дальневосточный федеральный округ',
  'Республика Саха (Якутия)',
  'Камчатский край',
  'Приморский край',
  'Хабаровский край',
  'Амурская область',
  'Магаданская область',
  'Сахалинская область',
  'Еврейская авт. область',
  'Чукотский авт. округ',
  'Крымский федеральный округ',
  'Республика Крым',
  'г. Севастополь']
  
summable_regions = [#'Российская Федерация',
  #'Центральный федеральный округ',
  'Белгородская область',
  'Брянская область',
  'Владимирская область',
  'Воронежская область',
  'Ивановская область',
  'Калужская область',
  'Костромская область',
  'Курская область',
  'Липецкая область',
  'Московская область',
  'Орловская область',
  'Рязанская область',
  'Смоленская область',
  'Тамбовская область',
  'Тверская область',
  'Тульская область',
  'Ярославская область',
  'г. Москва',
  #'Северо-Западный федеральный округ',
  'Республика Карелия',
  'Республика Коми',
  #'Архангельская область',
  'Ненецкий авт. округ',
  'Архангельская область без авт. округа',
  'Вологодская область',
  'Калининградская область',
  'Ленинградская область',
  'Мурманская область',
  'Новгородская область',
  'Псковская область',
  'г. Санкт-Петербург',
  #'Южный федеральный округ',
  'Республика Адыгея',
  'Республика Калмыкия',
  'Краснодарский край',
  'Астраханская область',
  'Волгоградская область',
  'Ростовская область',
  #'Северо-Кавказский федеральный округ',
  'Республика Дагестан',
  'Республика Ингушетия',
  'Кабардино-Балкарская Республика',
  'Карачаево-Черкесская Республика',
  'Республика Северная Осетия - Алания',
  'Чеченская Республика',
  'Ставропольский край',
  #'Приволжский федеральный округ',
  'Республика Башкортостан',
  'Республика Марий Эл',
  'Республика Мордовия',
  'Республика Татарстан',
  'Удмуртская Республика',
  'Чувашская Республика',
  'Пермский край',
  'Кировская область',
  'Нижегородская область',
  'Оренбургская область',
  'Пензенская область ',
  'Самарская область',
  'Саратовская область',
  'Ульяновская область',
  #'Уральский федеральный округ',
  'Курганская область',
  'Свердловская область',
  #'Тюменская область',
  'Ханты-Мансийский авт. округ - Югра',
  'Ямало-Ненецкий авт. округ',
  'Тюменская область без авт. округов',
  'Челябинская область',
  #'Сибирский федеральный округ',
  'Республика Алтай',
  'Республика Бурятия',
  'Республика Тыва',
  'Республика Хакасия',
  'Алтайский край',
  'Забайкальский край',
  'Красноярский край',
  'Иркутская область',
  'Кемеровская область',
  'Новосибирская область',
  'Омская область',
  'Томская область',
  #'Дальневосточный федеральный округ',
  'Республика Саха (Якутия)',
  'Камчатский край',
  'Приморский край',
  'Хабаровский край',
  'Амурская область',
  'Магаданская область',
  'Сахалинская область',
  'Еврейская авт. область',
  'Чукотский авт. округ',
  #'Крымский федеральный округ',
  'Республика Крым',
  'г. Севастополь']
  
  
  
def prefilter(raw_region):
    return raw_region.replace("округов", "округа").replace("в том числе","").strip("0123456789").replace(" ", "")
    
def filter_region_name(raw_region_name:str, reference_regions = reference_region_names):
    # COMMENT: raw_region_name:str is type annotation as in https://www.python.org/dev/peps/pep-0484/
    
    """
    Converts a raw region name to reference region name
    Inputs:
        reference_regions - list of reference region names
        raw_region_name - string with raw region name
    Output:
        string with reference region name
           or
        ""  (if no one matched)
    """    
    
    # rationale: we need names with spaces as the result of this function
    reverse_dict = {prefilter(r):r for r in reference_region_names}
    
    matched_reference_names = []
    raw_region_name = prefilter(raw_region_name)
    
    for ref_region in [prefilter(r) for r in reference_regions]:
    
        #exact match   
        if ref_region==raw_region_name:
            return reverse_dict[ref_region] 
            
        #partial match    
        else:
            if ref_region in raw_region_name:
                matched_reference_names.append(reverse_dict[ref_region])
    
    #  only one reference name is similar to raw_region           
    if len(matched_reference_names)==1:
        return matched_reference_names[0]
        
    # return longest matched region    
    ## EP/QUESTION: in what cases is this the case? 'Тюменская область без авт. округов'?
    ##              is it a secure matching procedure?
    elif len(matched_reference_names)>1:
        return max(matched_reference_names, key = len) 
    
    # returning empty string if there is no match
    return ""

if __name__ == "__main__":   

    ## EP / QUESTION: why exactly sample_regions_2 used? arbitrary?    
    from testdata.sample_regions_2 import regions as raw_regions
    
    for r in raw_regions:
        # see the difference between strings like "область" and "область "
        # without __repr__() you cannot see spaces in strings
        filtered = filter_region_name(r) 
        print("Filtered name:", filtered.__repr__(), ", raw name:", r.__repr__())
        assert filtered in reference_region_names