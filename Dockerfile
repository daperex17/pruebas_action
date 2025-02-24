FROM python:3.9.13-buster

WORKDIR /app

COPY . .

# Actualiza pip antes de instalar dependencias
RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]
