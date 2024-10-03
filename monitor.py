import requests
import time

# Aapka Render application ka URL
RENDER_APP_URL = "https://offline-server-2-made-by-amil-2.onrender.com"  # Replace with your actual Render app URL

# Health check interval (seconds)
CHECK_INTERVAL = 60  # Har 60 seconds baad check karega

def check_application():
    try:
        response = requests.get(RENDER_APP_URL)
        if response.status_code == 200:
            print(f"[+] Application is up and running. Status Code: {response.status_code}")
        else:
            print(f"[-] Application might be down. Status Code: {response.status_code}")
            # Yahan aap alert ya notification bhej sakte hain
            restart_application()
    except requests.exceptions.RequestException as e:
        print(f"[-] Application is down. Error: {e}")
        restart_application()

def restart_application():
    print("[!] Restarting the application...")
    # Yahan aapko Render API ko call karna padega ya kisi tarike se application ko restart karna padega
    # For example, you can send a POST request to Render API to trigger a redeploy
    # Yahan par aap Render API ko call karne ka code add kar sakte hain
    # Example (pseudocode):
    # response = requests.post("https://api.render.com/v1/services/YOUR_SERVICE_ID/deploys", headers={"Authorization": "Bearer YOUR_API_KEY"})

if __name__ == "__main__":
    while True:
        check_application()
        time.sleep(CHECK_INTERVAL)
