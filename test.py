from pathlib import Path

import rtds.rscadfx
import rtds.constants as rc
import socket
import time
import struct



# Establish a connection to an RSCAD FX application.
with rtds.rscadfx.remote_connection() as app:
    # 配置RTDS连接参数
    RTDS_IP = '127.0.0.1'  # RTDS的IP地址
    RTDS_PORT = 5000  
    def generate_wind_speed(start_speed=5.0, end_speed=15.0, duration=20):
        timesteps = int(duration)  # 每秒发送一次数据
        for t in range(timesteps):
            wind_speed = start_speed + (end_speed - start_speed) * (t / duration)
            yield wind_speed
            time.sleep(1)  # 实时仿真需严格同步