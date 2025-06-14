FROM huggingface/lerobot-gpu:latest

RUN /opt/venv/bin/pip install --upgrade --no-cache-dir pip \
    && /opt/venv/bin/pip install --no-cache-dir pyrealsense2 feetech-servo-sdk

RUN apt update