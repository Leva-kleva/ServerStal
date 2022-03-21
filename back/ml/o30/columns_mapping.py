def rename_columns(data, year):
    if year == 2019:
        data = data.rename(columns = columns_2019)
    if year == 2020:
        data = data.rename(columns = columns_2020)
    if year == 2021:
        data = data.rename(columns = columns_2021)
    return data   
    
    
columns_2019 = {'2016, Нематериальные активы, RUB': 'немат_активы_lag3', 
 '2017, Нематериальные активы, RUB': 'немат_активы_lag2',
 '2018, Нематериальные активы, RUB': 'немат_активы_lag1',
 '2016, Основные средства , RUB' : 'ос_lag3',
 '2017, Основные средства , RUB' : 'ос_lag2',
 '2018, Основные средства , RUB' : 'ос_lag1',
 '2016, Внеоборотные активы, RUB' : 'внеоб_активы_lag3',
 '2017, Внеоборотные активы, RUB' : 'внеоб_активы_lag2',
 '2018, Внеоборотные активы, RUB' : 'внеоб_активы_lag1',
 '2016, Дебиторская задолженность, RUB' : 'дебит_зад_lag3',
 '2017, Дебиторская задолженность, RUB' : 'дебит_зад_lag2',
 '2018, Дебиторская задолженность, RUB' : 'дебит_зад_lag1',
 '2016, Оборотные активы, RUB' : 'обор_активы_lag3',
 '2017, Оборотные активы, RUB' : 'обор_активы_lag2',
 '2018, Оборотные активы, RUB' : 'обор_активы_lag1',
 '2016, Уставный капитал , RUB' : 'ук_lag3',
 '2017, Уставный капитал , RUB' : 'ук_lag2',
 '2018, Уставный капитал , RUB' : 'ук_lag1',
 '2016, Капитал и резервы, RUB' : 'капитал_резервы_lag3',
 '2017, Капитал и резервы, RUB' : 'капитал_резервы_lag2',
 '2018, Капитал и резервы, RUB' : 'капитал_резервы_lag1',
 '2016, Заёмные средства (долгосрочные), RUB' : 'заемн_ср_долгоср_lag3',
 '2017, Заёмные средства (долгосрочные), RUB' : 'заемн_ср_долгоср_lag2',
 '2018, Заёмные средства (долгосрочные), RUB' : 'заемн_ср_долгоср_lag1',
 '2016, Долгосрочные обязательства, RUB' : 'долгоср_обязат_lag3',
 '2017, Долгосрочные обязательства, RUB' : 'долгоср_обязат_lag2',
 '2018, Долгосрочные обязательства, RUB' : 'долгоср_обязат_lag1',
 '2016, Заёмные средства (краткосрочные), RUB' : 'заемн_ср_кратк_lag3',
 '2017, Заёмные средства (краткосрочные), RUB' : 'заемн_ср_кратк_lag2',
 '2018, Заёмные средства (краткосрочные), RUB' : 'заемн_ср_кратк_lag1',
 '2016, Кредиторская задолженность, RUB' : 'кредит_задол_lag3',
 '2017, Кредиторская задолженность, RUB' : 'кредит_задол_lag2',
 '2018, Кредиторская задолженность, RUB' : 'кредит_задол_lag1',
 '2016, Краткосрочные обязательства, RUB' : 'кратк_обязат_lag3',
 '2017, Краткосрочные обязательства, RUB' : 'кратк_обязат_lag2',
 '2018, Краткосрочные обязательства, RUB' : 'кратк_обязат_lag1',
 '2016, Выручка, RUB' : 'выручка_lag3',
 '2017, Выручка, RUB' : 'выручка_lag2',
 '2018, Выручка, RUB' : 'выручка_lag1',
 '2016, Себестоимость продаж, RUB' : 'себест_продаж_lag3',
 '2017, Себестоимость продаж, RUB' : 'себест_продаж_lag2',
 '2018, Себестоимость продаж, RUB' : 'себест_продаж_lag1',
 '2016, Прибыль (убыток) до налогообложения , RUB' : 'прибыль_до_налога_lag3',
 '2017, Прибыль (убыток) до налогообложения , RUB' : 'прибыль_до_налога_lag2',
 '2018, Прибыль (убыток) до налогообложения , RUB' : 'прибыль_до_налога_lag1',
 '2016, Прибыль (убыток) от продажи, RUB' : 'прибыль_lag3',
 '2017, Прибыль (убыток) от продажи, RUB' : 'прибыль_lag2',
 '2018, Прибыль (убыток) от продажи, RUB' : 'прибыль_lag1'}

columns_2020 = {'2017, Нематериальные активы, RUB': 'немат_активы_lag3', 
 '2018, Нематериальные активы, RUB': 'немат_активы_lag2',
 '2019, Нематериальные активы, RUB': 'немат_активы_lag1',
 '2017, Основные средства , RUB' : 'ос_lag3',
 '2018, Основные средства , RUB' : 'ос_lag2',
 '2019, Основные средства , RUB' : 'ос_lag1',
 '2017, Внеоборотные активы, RUB' : 'внеоб_активы_lag3',
 '2018, Внеоборотные активы, RUB' : 'внеоб_активы_lag2',
 '2019, Внеоборотные активы, RUB' : 'внеоб_активы_lag1',
 '2017, Дебиторская задолженность, RUB' : 'дебит_зад_lag3',
 '2018, Дебиторская задолженность, RUB' : 'дебит_зад_lag2',
 '2019, Дебиторская задолженность, RUB' : 'дебит_зад_lag1',
 '2017, Оборотные активы, RUB' : 'обор_активы_lag3',
 '2018, Оборотные активы, RUB' : 'обор_активы_lag2',
 '2019, Оборотные активы, RUB' : 'обор_активы_lag1',
 '2017, Уставный капитал , RUB' : 'ук_lag3',
 '2018, Уставный капитал , RUB' : 'ук_lag2',
 '2019, Уставный капитал , RUB' : 'ук_lag1',
 '2017, Капитал и резервы, RUB' : 'капитал_резервы_lag3',
 '2018, Капитал и резервы, RUB' : 'капитал_резервы_lag2',
 '2019, Капитал и резервы, RUB' : 'капитал_резервы_lag1',
 '2017, Заёмные средства (долгосрочные), RUB' : 'заемн_ср_долгоср_lag3',
 '2018, Заёмные средства (долгосрочные), RUB' : 'заемн_ср_долгоср_lag2',
 '2019, Заёмные средства (долгосрочные), RUB' : 'заемн_ср_долгоср_lag1',
 '2017, Долгосрочные обязательства, RUB' : 'долгоср_обязат_lag3',
 '2018, Долгосрочные обязательства, RUB' : 'долгоср_обязат_lag2',
 '2019, Долгосрочные обязательства, RUB' : 'долгоср_обязат_lag1',
 '2017, Заёмные средства (краткосрочные), RUB' : 'заемн_ср_кратк_lag3',
 '2018, Заёмные средства (краткосрочные), RUB' : 'заемн_ср_кратк_lag2',
 '2019, Заёмные средства (краткосрочные), RUB' : 'заемн_ср_кратк_lag1',
 '2017, Кредиторская задолженность, RUB' : 'кредит_задол_lag3',
 '2018, Кредиторская задолженность, RUB' : 'кредит_задол_lag2',
 '2019, Кредиторская задолженность, RUB' : 'кредит_задол_lag1',
 '2017, Краткосрочные обязательства, RUB' : 'кратк_обязат_lag3',
 '2018, Краткосрочные обязательства, RUB' : 'кратк_обязат_lag2',
 '2019, Краткосрочные обязательства, RUB' : 'кратк_обязат_lag1',
 '2017, Выручка, RUB' : 'выручка_lag3',
 '2018, Выручка, RUB' : 'выручка_lag2',
 '2019, Выручка, RUB' : 'выручка_lag1',
 '2017, Себестоимость продаж, RUB' : 'себест_продаж_lag3',
 '2018, Себестоимость продаж, RUB' : 'себест_продаж_lag2',
 '2019, Себестоимость продаж, RUB' : 'себест_продаж_lag1',
 '2017, Прибыль (убыток) до налогообложения , RUB' : 'прибыль_до_налога_lag3',
 '2018, Прибыль (убыток) до налогообложения , RUB' : 'прибыль_до_налога_lag2',
 '2019, Прибыль (убыток) до налогообложения , RUB' : 'прибыль_до_налога_lag1',
 '2017, Прибыль (убыток) от продажи, RUB' : 'прибыль_lag3',
 '2018, Прибыль (убыток) от продажи, RUB' : 'прибыль_lag2',
 '2019, Прибыль (убыток) от продажи, RUB' : 'прибыль_lag1'}

columns_2021 = {'2018, Нематериальные активы, RUB': 'немат_активы_lag3', 
 '2019, Нематериальные активы, RUB': 'немат_активы_lag2',
 '2020, Нематериальные активы, RUB': 'немат_активы_lag1',
 '2018, Основные средства , RUB' : 'ос_lag3',
 '2019, Основные средства , RUB' : 'ос_lag2',
 '2020, Основные средства , RUB' : 'ос_lag1',
 '2018, Внеоборотные активы, RUB' : 'внеоб_активы_lag3',
 '2019, Внеоборотные активы, RUB' : 'внеоб_активы_lag2',
 '2020, Внеоборотные активы, RUB' : 'внеоб_активы_lag1',
 '2018, Дебиторская задолженность, RUB' : 'дебит_зад_lag3',
 '2019, Дебиторская задолженность, RUB' : 'дебит_зад_lag2',
 '2020, Дебиторская задолженность, RUB' : 'дебит_зад_lag1',
 '2018, Оборотные активы, RUB' : 'обор_активы_lag3',
 '2019, Оборотные активы, RUB' : 'обор_активы_lag2',
 '2020, Оборотные активы, RUB' : 'обор_активы_lag1',
 '2018, Уставный капитал , RUB' : 'ук_lag3',
 '2019, Уставный капитал , RUB' : 'ук_lag2',
 '2020, Уставный капитал , RUB' : 'ук_lag1',
 '2018, Капитал и резервы, RUB' : 'капитал_резервы_lag3',
 '2019, Капитал и резервы, RUB' : 'капитал_резервы_lag2',
 '2020, Капитал и резервы, RUB' : 'капитал_резервы_lag1',
 '2018, Заёмные средства (долгосрочные), RUB' : 'заемн_ср_долгоср_lag3',
 '2019, Заёмные средства (долгосрочные), RUB' : 'заемн_ср_долгоср_lag2',
 '2020, Заёмные средства (долгосрочные), RUB' : 'заемн_ср_долгоср_lag1',
 '2018, Долгосрочные обязательства, RUB' : 'долгоср_обязат_lag3',
 '2019, Долгосрочные обязательства, RUB' : 'долгоср_обязат_lag2',
 '2020, Долгосрочные обязательства, RUB' : 'долгоср_обязат_lag1',
 '2018, Заёмные средства (краткосрочные), RUB' : 'заемн_ср_кратк_lag3',
 '2019, Заёмные средства (краткосрочные), RUB' : 'заемн_ср_кратк_lag2',
 '2020, Заёмные средства (краткосрочные), RUB' : 'заемн_ср_кратк_lag1',
 '2018, Кредиторская задолженность, RUB' : 'кредит_задол_lag3',
 '2019, Кредиторская задолженность, RUB' : 'кредит_задол_lag2',
 '2020, Кредиторская задолженность, RUB' : 'кредит_задол_lag1',
 '2018, Краткосрочные обязательства, RUB' : 'кратк_обязат_lag3',
 '2019, Краткосрочные обязательства, RUB' : 'кратк_обязат_lag2',
 '2020, Краткосрочные обязательства, RUB' : 'кратк_обязат_lag1',
 '2018, Выручка, RUB' : 'выручка_lag3',
 '2019, Выручка, RUB' : 'выручка_lag2',
 '2020, Выручка, RUB' : 'выручка_lag1',
 '2018, Себестоимость продаж, RUB' : 'себест_продаж_lag3',
 '2019, Себестоимость продаж, RUB' : 'себест_продаж_lag2',
 '2020, Себестоимость продаж, RUB' : 'себест_продаж_lag1',
 '2018, Прибыль (убыток) до налогообложения , RUB' : 'прибыль_до_налога_lag3',
 '2019, Прибыль (убыток) до налогообложения , RUB' : 'прибыль_до_налога_lag2',
 '2020, Прибыль (убыток) до налогообложения , RUB' : 'прибыль_до_налога_lag1',
 '2018, Прибыль (убыток) от продажи, RUB' : 'прибыль_lag3',
 '2019, Прибыль (убыток) от продажи, RUB' : 'прибыль_lag2',
 '2020, Прибыль (убыток) от продажи, RUB' : 'прибыль_lag1'}