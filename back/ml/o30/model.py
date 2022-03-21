# import joblib
# import pandas as pd
# import numpy as np
# from sklearn.metrics import roc_auc_score
#
#
# ss_fin_module = joblib.load('ss_fin_30.pkl')
# fin_module30 = joblib.load( 'fin_model_no_woe30_15_best.pkl')
#
# df_2021 = pd.read_csv('counterparty-analysis/agents2021.csv')
# df_2021 = df_2021.drop(['Unnamed: 0'], axis = 1)
#
# import columns_mapping as cm
#
# df_2021 = cm.rename_columns(df_2021, 2021)
#
# df_small = df_2021[['кратк_обязат_lag2','выручка_lag1','кредит_задол_lag1', 'немат_активы_lag1',
#                    'прибыль_lag2', 'немат_активы_lag2', 'заемн_ср_кратк_lag3', 'внеоб_активы_lag3', 'долгоср_обязат_lag1',
#                    'ук_lag3', 'заемн_ср_кратк_lag2', 'прибыль_до_налога_lag2', 'прибыль_lag3']]
#
# df_small['div_log_кратк_обязат_lag2_log_выручка_lag1'] = np.log1p(df_small['кратк_обязат_lag2'])/ \
#     np.log1p(df_small['выручка_lag1'])
# df_small['mult_кредит_задол_lag1_кратк_обязат_lag2'] = df_small['кредит_задол_lag1']* df_small['кратк_обязат_lag2']
# df_small['div_немат_активы_lag1_заемн_ср_кратк_lag2'] = df_small['немат_активы_lag1']/ df_small['заемн_ср_кратк_lag2']
# df_small['div_немат_активы_lag1_прибыль_lag2'] = df_small['немат_активы_lag1']* df_small['прибыль_lag2']
# df_small['div_немат_активы_lag2_заемн_ср_кратк_lag3'] = df_small['немат_активы_lag2']/ df_small['заемн_ср_кратк_lag3']
# df_small['div_внеоб_активы_lag3_долгоср_обязат_lag1'] = df_small['внеоб_активы_lag3']* df_small['долгоср_обязат_lag1']
# df_small['div_ук_lag3_заемн_ср_кратк_lag2'] = df_small['ук_lag3']/ df_small['заемн_ср_кратк_lag2']
# df_small['div_прибыль_до_налога_lag2_прибыль_lag3'] = df_small['прибыль_до_налога_lag2']/ df_small['прибыль_lag3']
#
#
# features = ['div_немат_активы_lag1_заемн_ср_кратк_lag2',
#  'mult_кредит_задол_lag1_кратк_обязат_lag2',
#  'div_прибыль_до_налога_lag2_прибыль_lag3',
#  'div_немат_активы_lag1_прибыль_lag2',
#  'div_ук_lag3_заемн_ср_кратк_lag2',
#  'div_внеоб_активы_lag3_долгоср_обязат_lag1',
#  'div_немат_активы_lag2_заемн_ср_кратк_lag3',
#  'div_log_кратк_обязат_lag2_log_выручка_lag1']
#
# df_small = df_small.fillna(0)
# df_small[df_small.isin([np.inf, -np.inf])] = 0 # заменим нулем
#
# df_small_ss = df_small[features].copy()
#
# df_small_ss[features] = ss_fin_module.transform(df_small_ss[features])
#
# df_2021['preds_test'] = fin_module30.predict_proba(df_small_ss[features])[:,1]
