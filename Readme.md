# 📚 Sistema de Chamada Escolar

## 📝 Sobre o Projeto
Este projeto é um sistema de chamada escolar desenvolvido com Django. Ele permite o gerenciamento de **alunos**, **professores**, **matérias** e **presenças**. Além disso, possui autenticação via token para garantir segurança no acesso às APIs e uma interface web amigável para usuários.

## 🚀 Comandos Principais

### 🌐 Acessar a interface web:
```bash
HTML: http://127.0.0.1:8000/alunos/
```

### ⚙️ Configuração do ambiente:
```bash
# Criar ambiente virtual
python -m venv ambiente

# Ativar ambiente virtual
ambiente\Scripts\activate
```

### 📦 Instalar dependências:
```bash
pip install dlib-19.24.1-cp311-cp311-win_amd64.whl
pip install -r requirements.txt
```

### 🗃️ Configurar banco de dados:
```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate
```

### 🏃 Executar o servidor:
```bash
python manage.py runserver
```

### 🔑 Criar superusuário:
```bash
python manage.py createsuperuser
```
