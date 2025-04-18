FROM python:3.11-slim
RUN adduser --disabled-password --gecos "" appuser
USER appuser
WORKDIR /app
COPY --chown=appuser:appuser requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --chown=appuser:appuser . .
EXPOSE 8080
CMD ["python", "main.py"]