FROM fusuf/asenauserbot:latest
RUN git clone https://github.com/HerLockDev/MisakiiUserBot /root/misakiuserbot
WORKDIR /root/misakiuserbot/
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]
