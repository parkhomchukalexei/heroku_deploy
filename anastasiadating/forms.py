from django.forms import ModelForm, ChoiceField, Form, CharField
from users.models import User, Client


class CreateAnastasiadatingTable(Form):

    all_clients = Client.objects.all()
    all_operators = User.objects.filter(groups__name = '[AD] Operator')
    print(all_operators)
    table_choise = (
        ('1', 'AD'),
        ('0', 'D')
    )
    operator_choise = (
        ((i.id, i) for i in all_operators)
    )
    client_choise = (
        ((i.id, i.name) for i in all_clients)
    )
    month_list = (("1", 'Январь'),("2", 'Февраль'), ("3", 'Март'), ("4", 'Апрель'), ("5",'Май'), ("6", 'Июнь'), ("7", 'Июль'),
             ("8", 'Август'),  ("9", 'Сентябрь'), ("10", 'Октябрь'), ("11", 'Ноябрь'),  ("12", 'Декабрь'))

    month = ChoiceField(choices=month_list)
    operator = ChoiceField(choices=operator_choise)
    client = ChoiceField(choices=client_choise)
    table_type = ChoiceField(choices=table_choise)
    account_id = CharField()
