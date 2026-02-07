import logging
from flask import Flask, render_template, Response, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)  # 只显示错误日志，不显示访问请求日志

# 预生成 10MB 块
chunk_10mb = os.urandom(10 * 1024 * 1024)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chart.min.js')
def chart():
    return render_template('chart.min.js')

@app.route('/ping')
def ping():
    return "pong"

@app.route('/download')
def download():
    # 生成一个 100MB 的大块
    chunk = b'0' * (100 * 1024 * 1024)
    def generate():
        # 确保 10 秒内发不完
        for _ in range(100000000000000000000000000):
            yield chunk
    return Response(generate(), mimetype='application/octet-stream')

@app.route('/upload', methods=['POST'])
def upload():
    # 流式读取以防内存撑爆
    chunk_size = 4096
    while True:
        chunk = request.stream.read(chunk_size)
        if not chunk:
            break
    return "OK"

if __name__ == '__main__':
    # threaded=True 对于处理并发测速请求至关重要
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=False)