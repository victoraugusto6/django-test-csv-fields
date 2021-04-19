import csv
import io
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

from csv_django.csv_file.models import Contato


@permission_required('admin.can_add_log_entry')
def contato_upload(request):
    template = 'contato_upload.html'

    prompt = {
        'order': 'Ordem do CSV deve ser nome, sobrenome, email, endereco_ip, mensagem.'
    }

    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Este não é um arquivo CSV.')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Contato.objects.update_or_create(
            nome=column[0],
            sobrenome=column[1],
            email=column[2],
            endereco_ip=column[3],
            mensagem=column[4],
        )

    context = {}
    return render(request, template, context)
