FROM python:3-alpine

RUN apk add --no-cache gcc musl-dev libffi-dev

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/home/appuser/.local/bin:$PATH"

COPY agents-with-adk/requirements.txt requirements.txt

# Create and switch to a non-root user
RUN adduser -u 5678 --disabled-password --gecos "" appuser
USER appuser

# Install dependencies as the non-root user
RUN PATH="/home/appuser/.local/bin:$PATH" python -m pip install --upgrade pip && \
    PATH="/home/appuser/.local/bin:$PATH" python -m pip install --no-cache-dir --use-deprecated=legacy-resolver --root-user-action=ignore -r requirements.txt && \
    PATH="/home/appuser/.local/bin:$PATH" adk --help

WORKDIR /app
COPY . /app

# Debug: Verify the directory structure
RUN ls -la /app
RUN ls -la /app/agents-with-adk

EXPOSE 8080

CMD ["sh", "-c", "adk web /app/agents-with-adk --port ${PORT:-8080}"]
