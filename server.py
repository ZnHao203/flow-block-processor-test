#!/usr/bin/env python3
import os
import sys
import signal
import json
import time
import threading

from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/vote":
            self.handle_vote()
        elif self.path == "/block":
            self.handle_block()
        else:
            self.send_respose(404)
            self.end_headers
            self.wfile.write(b"Not Found")
    
    def handle_vote(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        print("Received body:", post_data.decode('utf-8'))  # Debugging

        try:
            data = json.loads(post_data)
            block_id = data.get('block_id')
            if block_id:
                print(f"The block id of the vote is {block_id}")
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"Received")
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Missing block_id field")
        except json.JSONDecodeError:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid JSON")

    def handle_block(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        print("Received body:", post_data.decode('utf-8'))  # Debugging

        try:
            data = json.loads(post_data)
            block_id = data.get('id')
            view = data.get('view')
            if block_id and view:
                print(f"The id of the block is {block_id}")
                print(f"The view of the block is {view}")
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"Received")
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Missing block_id or view field")
        except json.JSONDecodeError:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid JSON")

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
