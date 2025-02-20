from django.http import HttpResponse
import os
import subprocess
import pytz
from datetime import datetime

def htop_view(request):  # ✅ Ensure function name is "htop_view" (not "htop_views")
    # Get system username
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown"

    # Get server time in IST
    ist = pytz.timezone("Asia/Kolkata")
    server_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S %Z")

    # Get 'top' command output (first 10 lines)
    try:
        top_output = subprocess.check_output("top -b -n 1 | head -10", shell=True, text=True)
    except Exception as e:
        top_output = f"Error fetching top output: {e}"

    # HTML Response
    response_html = f"""
    <html>
    <head><title>HTop Info</title></head>
    <body>
        <h1>HTop Information</h1>
        <p><strong>Name:</strong> Shrey Patel</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <h2>Top Output:</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return HttpResponse(response_html)
