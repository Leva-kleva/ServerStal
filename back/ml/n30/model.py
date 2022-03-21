import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore")
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import joblib

standard_skaler_fin = joblib.load('ml/n30/ss_fin_30.pkl')
fin_model = joblib.load('ml/n30/fin_model_no_woe30_15_best.pkl')
final_model = joblib.load('ml/n30/final_model_no_woe30_15_best.pkl')

input_fin_data = pd.read_csv('ml/n30/input_fin_data.csv', sep=';', header=None).set_index(0)
input_fin_data = input_fin_data[1].to_dict()


def get_score(input_data):
    input_1 = pd.DataFrame()

    input_1.loc[0, 'div_ук_lag3_заемн_ср_кратк_lag2'] = input_data['ук_lag3'] / input_data['заемн_ср_кратк_lag2']
    input_1.loc[0, 'div_прибыль_до_налога_lag2_прибыль_lag3'] = input_data['прибыль_до_налога_lag2'] / input_data[
        'прибыль_lag3']
    input_1.loc[0, 'div_немат_активы_lag2_заемн_ср_кратк_lag3'] = input_data['немат_активы_lag2'] / input_data[
        'заемн_ср_кратк_lag3']
    input_1.loc[0, 'div_немат_активы_lag1_прибыль_lag2'] = input_data['немат_активы_lag1'] / input_data['прибыль_lag2']
    input_1.loc[0, 'div_внеоб_активы_lag3_долгоср_обязат_lag1'] = input_data['внеоб_активы_lag3'] / input_data[
        'долгоср_обязат_lag1']
    input_1.loc[0, 'mult_кредит_задол_lag1_кратк_обязат_lag2'] = input_data['кредит_задол_lag1'] * input_data[
        'кратк_обязат_lag2']
    input_1.loc[0, 'div_log_кратк_обязат_lag2_log_выручка_lag1'] = np.log(input_data['кратк_обязат_lag2']) / np.log(
        input_data['выручка_lag1'])
    input_1.loc[0, 'div_немат_активы_lag1_заемн_ср_кратк_lag2'] = input_data['немат_активы_lag1'] / input_data[
        'заемн_ср_кратк_lag2']

    # для обработки деления на 0 и пропусков
    input_1 = input_1.fillna(0)
    input_1[input_1.isin([np.inf, -np.inf])] = 0  # заменим нулем

    input_1_scaled = standard_skaler_fin.transform(input_1)
    fin_score_predict = fin_model.predict_proba(input_1_scaled)[0][1]

    input_2 = pd.DataFrame()
    input_2.loc[0, 'fin_module_score'] = fin_score_predict
    input_2.loc[0, 'Факт. 60_0-19'] = 1 if input_data['факт_60'] <= 19 else 0
    input_2.loc[0, 'Факт. 3_80-100'] = 1 if (input_data['факт_3'] >= 80) & (input_data['факт_3'] <= 100) else 0
    input_2.loc[0, 'Факт. 1_is100'] = 1 if input_data['факт_1'] == 100 else 0
    input_2.loc[0, 'Факт. 59_0-19'] = 1 if input_data['факт_59'] <= 19 else 0

    final_score_predict = final_model.predict_proba(input_2)[0][1]
    return {"var": max(0, round(final_score_predict*100, 1))}
