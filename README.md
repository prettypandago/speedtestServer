# speedtestServer - A Lightweight Network Speed Test Server | Simple Yet Powerful

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue)

A lightweight network speed test server with a clean web interface for testing network download, upload, and latency.

**Languages:** [English](README.md "English version"), [简体中文](README_zh-cn.md "简体中文版")

## ✨ Key Features

- 🚀 **Download Test** - Test your network download speed
- 📤 **Upload Test** - Test your network upload speed  
- 🔔 **Latency Test** - Test network latency (Ping)
- 📊 **Real-time Charts** - Real-time speed test results visualization powered by Chart.js
- 🎨 **Clean Interface** - Modern, lightweight, and user-friendly web frontend
- 🔄 **CORS Support** - Built-in CORS middleware for cross-origin requests

## 📋 Requirements

- Python 3.6+
- Flask
- Flask-cors

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/prettypandago/speedtestServer.git
cd speedtestServer
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Server
```bash
python speedtestServer.py
```

The server will start at `http://localhost:5000`

### 4. Test

Open `http://localhost:5000` in your browser and use the web interface to perform network speed tests.

## 📁 Project Structure

```
speedtestServer/
├── speedtestServer.py      # Flask backend server
├── requirements.txt         # Python dependencies
├── templates/
│   ├── index.html          # Web frontend interface
│   └── chart.min.js        # Chart.js libraryscript
├── LICENSE                 # MIT License
├── README.md               # This file
└── README_zh-cn.md         # Chinese version
```

## 🔌 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Return frontend HTML page |
| `/ping` | GET | Latency test (returns "pong") |
| `/download` | GET | Download test (returns data stream) |
| `/upload` | POST | Upload test (receives file data) |

## ⚙️ Configuration

Edit the configuration in `speedtestServer.py`:

```python
app.run(host='0.0.0.0', port=5000, threaded=True, debug=False)
```

Configuration parameters:
- `host`: Server binding address (`0.0.0.0` listens on all interfaces)
- `port`: Server port number (default 5000)
- `threaded`: Enable multi-threading (essential for handling concurrent requests)
- `debug`: Debug mode toggle

## 📝 Notes

⚠️ **Project is under development** - APIs and features may change. Please test thoroughly before using in production.

## 🤝 Contributing

Pull Requests and Issues are welcome!

## 📜 License

This project is open-sourced under the [MIT License](LICENSE)

---

Thank you for using speedtestServer!
