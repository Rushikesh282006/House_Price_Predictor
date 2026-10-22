FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Train model if not already present
RUN if [ ! -f house_price_predictor.joblib ]; then python train.py; fi

ENV PORT=8000
EXPOSE 8000

# Start command supporting dynamic $PORT
CMD sh -c "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"
