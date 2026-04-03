# Imagem base do Python (versão estável e leve)
FROM python:3.11-slim

# Define o diretório onde as coisas vão acontecer dentro do container
WORKDIR /app

# Copia os requisitos e instala as bibliotecas
# Importante: scikit-learn deve ser a mesma versão que você usou no Notebook
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o seu código (appClassificacao.py) e o seu modelo (.pkl)
COPY . .

# Expõe a porta 5000 (padrão do Flask)
EXPOSE 5000

# Comando para rodar a API usando Gunicorn (servidor de produção)
RUN pip install gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "appClassificacao:app"]