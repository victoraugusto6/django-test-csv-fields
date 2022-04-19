## Repositório para testar inserção de campos em models a partir de um arquivo CSV.

### <strong>Instruções para instalação</strong>:

#### Criar e ativar ambiente virtual Python (venv):

```python -m venv .venv```

```source .venv/bin/activate```

#### <strong>Instalar dependências</strong>:

```pip install requirements.txt```

#### <strong>Instalar dependências, inclusive de desenvolvimento</strong>:

```pip install requirements-dev.txt```

#### Copiar variáveis de ambiente:
```cp contrib/env-sample .env```

#### Rodar Django:
```python manage.py runserver```