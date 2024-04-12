FROM python:3.11-alpine
WORKDIR /backend
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD python3 healthcheck_script.py || exit 1
