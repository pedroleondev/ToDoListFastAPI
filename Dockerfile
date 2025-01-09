# Usar uma imagem base do Python
FROM python:3.10-slim

# Criar e definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar apenas os arquivos necessários para o container
COPY requirements.txt .

# Instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do projeto para o container
COPY . .

# Expor a porta usada pela aplicação
EXPOSE 8000

# Comando para rodar a aplicação com Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
