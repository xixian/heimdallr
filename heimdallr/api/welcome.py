from fastapi import APIRouter
from fastapi.responses import HTMLResponse

welcome_router = APIRouter()

@welcome_router.get("/", response_class=HTMLResponse)
async def welcome():
    return """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to Heimdallr!</title>
    <style>
        :root {
            --primary-color: #4285f4;
            --secondary-color: #34a853;
            --accent-color: #ea4335;
            --text-color: #333;
            --light-text: #666;
            --bg-color: #f8f9fa;
            --card-bg: #ffffff;
            --footer-bg: #202124;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.6;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }
        
        .container {
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 2rem;
            max-width: 1200px;
            margin: 0 auto;
            width: 100%;
        }
        
        .welcome-card {
            background-color: var(--card-bg);
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 2.5rem;
            text-align: center;
            width: 100%;
            max-width: 600px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .welcome-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        }
        
        h1 {
            color: var(--primary-color);
            margin-bottom: 1.5rem;
            font-size: 2.2rem;
            font-weight: 600;
        }
        
        .emoji {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
        
        .links {
            display: flex;
            flex-direction: column;
            gap: 1rem;
            margin: 2rem 0;
        }
        
        .link-item {
            display: inline-block;
            padding: 0.8rem 1.5rem;
            background-color: var(--primary-color);
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 500;
            transition: background-color 0.3s ease, transform 0.2s ease;
        }
        
        .link-item:hover {
            background-color: #3367d6;
            transform: scale(1.05);
        }
        
        .link-item.secondary {
            background-color: var(--secondary-color);
        }
        
        .link-item.secondary:hover {
            background-color: #2d9249;
        }
        
        .link-item.accent {
            background-color: var(--accent-color);
        }
        
        .link-item.accent:hover {
            background-color: #d33426;
        }
        
        .small-text {
            color: var(--light-text);
            font-size: 0.9rem;
            margin-top: 1.5rem;
        }
        
        .small-text a {
            color: var(--primary-color);
            text-decoration: none;
            font-weight: 500;
        }
        
        .small-text a:hover {
            text-decoration: underline;
        }
        
        footer {
            background-color: var(--footer-bg);
            color: white;
            text-align: center;
            padding: 1.5rem;
            width: 100%;
        }
        
        footer a {
            color: var(--accent-color);
            text-decoration: none;
            font-weight: 500;
        }
        
        footer a:hover {
            text-decoration: underline;
        }
        
        @media (max-width: 768px) {
            .welcome-card {
                padding: 1.5rem;
            }
            
            h1 {
                font-size: 1.8rem;
            }
            
            .emoji {
                font-size: 2rem;
            }
            
            .link-item {
                padding: 0.7rem 1.2rem;
            }
        }
        
        @media (max-width: 480px) {
            .container {
                padding: 1rem;
            }
            
            .welcome-card {
                padding: 1.2rem;
            }
            
            h1 {
                font-size: 1.5rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="welcome-card">
            <div class="emoji">🎉</div>
            <h1>Welcome to Heimdallr!</h1>
            
            <div class="links">
                <a href="/docs" class="link-item">API Documentation</a>
                <a href="https://heimdallr-configurator.vercel.app/" class="link-item secondary">Configuration Generator</a>
                <a href="https://github.com/LeslieLeung/heimdallr#%E7%A4%BA%E4%BE%8B%E5%BA%94%E7%94%A8" target="_blank" class="link-item accent">Example Applications</a>
            </div>
            
            <p class="small-text">
                Don't know how to use it? Check out our <a href="https://github.com/LeslieLeung/heimdallr#%E7%A4%BA%E4%BE%8B%E5%BA%94%E7%94%A8" target="_blank">documentation</a>
            </p>
        </div>
    </div>
    
    <footer>
        <p>If you like this project, please give it a Star! <a href="https://github.com/leslieleung/heimdallr" target="_blank">GitHub</a></p>
    </footer>
</body>
</html>
"""
