FROM python:3.7-alpine
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]