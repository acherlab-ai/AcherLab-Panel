import os, json, platform
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="AcherLab Panel", version="2.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"service": "AcherLab Panel", "version": "2.0.0", "status": "operational"}

@app.get("/api/system")
def system_info():
    import platform, psutil
    return {
        "hostname": platform.node(),
        "os": f"{platform.system()} {platform.release()}",
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent
    }

@app.get("/api/services")
def services():
    return [
        {"name": "AI Assistant", "status": "active", "icon": "brain"},
        {"name": "Tunnel API", "status": "active", "icon": "network"},
        {"name": "RDP Service", "status": "active", "icon": "desktop"},
        {"name": "VPS Monitor", "status": "active", "icon": "server"}
    ]

@app.post("/api/ai/chat")
def ai_chat(req: ChatRequest):
    msg = req.message.lower().strip()
    replies = {
        "hello": "Xin chao! AcherLab AI san sang ho tro ban.",
        "help": "Toi co the giup: quan ly server, tao tunnel, kiem tra he thong.",
        "status": "He thong AcherLab dang hoat dong tot. Tat ca dich vu online.",
        "tunnel": "Dung AcherLab Tunnel API de tao TCP tunnel. Xem docs tai /docs",
        "rdp": "AcherLab RDP ho tro windows-latest va windows-2022. Chay GitHub Actions.",
        "ai": "AcherLab AI tich hop GPT-4, LLM, va cac mo hinh AI khac."
    }
    for key, reply in replies.items():
        if key in msg:
            return {"reply": reply, "model": "AcherLab AI v2"}
    return {"reply": "Toi la AcherLab AI. Toi co the giup gi?", "model": "AcherLab AI v2"}

@app.get("/api/tunnels")
def list_tunnels():
    return [
        {"name": "SSH Tunnel", "local": "127.0.0.1:22", "remote": "0.0.0.0:2222", "status": "active"},
        {"name": "RDP Tunnel", "local": "127.0.0.1:3389", "remote": "0.0.0.0:3390", "status": "active"},
        {"name": "Web Tunnel", "local": "127.0.0.1:80", "remote": "0.0.0.0:8080", "status": "inactive"}
    ]

@app.get("/api/health")
def health():
    return {"status": "healthy", "uptime": "99.9%", "version": "2.0.0"}