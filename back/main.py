import json
from flask import Flask, request, make_response, abort, session
import ml
import schemes
import objects
import conf

app = Flask(__name__)
app.config['SECRET_KEY'] = conf.secret_key
app.secret_key = conf.secret_key  # os.urandom(24)

models = {
    # ("old-client", 1): ml.o1.model.get_score,
    # ("old-client", 30): ml.o30.model.get_score,
    # ("old-client", 90): ml.o90.model.get_score,
    # ("new-client", 1): ml.n1.model.get_score,
    ("new-client", 30): ml.n30.model.get_score,
    # ("new-client", 90): ml.n90.model.get_score,
}

form = {
    # ("old-client", 1): objects.objects[("old-client", 1)].keys(),
    ("old-client", 30): objects.objects[("old-client", 30)].keys(),
    # ("old-client", 90): objects.objects[("old-client", 90)].keys(),
    # ("new-client", 1): objects.objects[("new-client", 1)].keys(),
    ("new-client", 30): objects.objects[("new-client", 30)].keys(),
    # ("new-client", 90): objects.objects[("new-client", 90)].keys(),
}

translate = {
    "ук_lag3": "Уставной капитал 3 года назад",
    "заемн_ср_кратк_lag2": "Краткосрочные заемные средства 2 года назад",
    "заемн_ср_кратк_lag3": "Краткосрочные заемные средства 3 года назад",
    "прибыль_до_налога_lag2": "Прибыль до налога 2 года назад",
    "прибыль_lag2": "Прибыль 2 года назад",
    "прибыль_lag3": "Прибыль 3 года назад",
    "выручка_lag1": "Выручка 1 год назад",
    'немат_активы_lag1': "Немат. Активы 1 год назад",
    'немат_активы_lag2': "Немат. Активы 2 год назад",
    'внеоб_активы_lag3': "Внеоб. Активы 3 года назад",
    'долгоср_обязат_lag1': "Долгосрочные обязательства 1 год назад",
    'кратк_обязат_lag2': "Краткосрочные обязательства 2 года назад",
    'кредит_задол_lag1': "Кредиторская задолженность 1 год назад",
    'факт_60': "Факт 60",
    'факт_3': "Факт 3",
    'факт_1': "Факт 3",
    'факт_59': "Факт 59",
    'diesel': "дизель",
    'SYG': 'газ',
    'hybrid': 'гибрид',
    'electro': 'электро',
    'full': 'полный',
    'front': 'передний',
    'rear': 'задний',
    'automatic': 'автомат',
    'variator': 'вариатор',
    'robot': 'робот',
    'mechanics': 'механика',
    'mark': 'марку',
    'Model': 'модель',
    'Generation': 'поколение',
    'Engine': 'тип двигателя',
    'Drive': 'тип привода',
    'Box': 'коробку передач',
    'Mileage': 'пробег',
    'Year': 'год выпуска',
    'Engine_volume': 'объем двигателя',
    'Torque': 'крутящий момент',
}

moc = {
    "ук_lag3": "34534532",
    "заемн_ср_кратк_lag2": "3434",
    "заемн_ср_кратк_lag3": "34334",
    "прибыль_до_налога_lag2": "2432",
    "прибыль_lag2": "2342",
    "прибыль_lag3": "5453",
    "выручка_lag1": "2",
    'немат_активы_lag1': "93873",
    'немат_активы_lag2': "397",
    'внеоб_активы_lag3': "8263",
    'долгоср_обязат_lag1': "937",
    'кратк_обязат_lag2': "84",
    'кредит_задол_lag1': "48464",
    'факт_60': "15",
    'факт_3': "30",
    'факт_1': "100",
    'факт_59': "25",
}
def template_response(body, code, is_json=False):
    if not is_json:
        status = "info" if code < 400 else "error"
        tmp = f'{{"{status}": "{body}"}}'
        body = tmp
    response = make_response(body, code)
    response.headers["Content-Type"] = "application/json"
    return response


@app.route('/request', methods=['POST'])
def req():
    print(request.json)
    # if not schemes.check(request, schemes.req.object):
    #     return template_response('Невалидный запрос', 400)

    type_client = request.json.pop('type-client')[0]
    type_delay = int(request.json.pop('type-delay')[0])
    object = (type_client, type_delay)

    # if not schemes.check(request, schemes.req.post[object]):
    #     return template_response('Невалидный запрос', 400)

    queryset = request.json
    for key, value in queryset.items():
        if value[0].isdigit():
            queryset[key] = int(value[0])
        else:
            try: queryset[key] = float(value[0])
            except: pass

    # if queryset.get('wallsMaterial') is not None:
    #     if queryset['wallsMaterial'][0] == "": queryset['wallsMaterial'] = ['panel']
        # queryset['wallsMaterial'] = [objects.id_materials[queryset['wallsMaterial'][0]]]

    ans = models[object](queryset)
    body, code = ans, 200

    return template_response(json.dumps(body), code, is_json=True)


@app.route('/get_params', methods=['POST'])
def get_params():
    object = request.json['type-client'], int(request.json['type-delay'])
    response = {}
    # print(object)
    # print(form[object])
    s = "<h6 align='center'>*Ниже автоматически введены параметры для ООО 'Рога и Копыта', их можно изменять</h6>"
    for el in form[object]:
        if request.json.get(el) is not None: continue
        if isinstance(objects.objects[object][el], list):
            s += f"<label>{translate[el]}</label>"
            s += f"<input class='w3-input change' type='number' id={el} value='{moc[el]}'>"
    response["data"] = s
    # '<label>Введите ' + json_date['translate'][key] + '</label><input class="w3-input change" type="number" id=' + key + '>'
    # print(response)
    return response


if __name__ == '__main__':
    app.run(debug=conf.debug, port=conf.port, host=conf.host)
