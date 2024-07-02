#!/usr/bin/env python3
import os
import sys
import signal
import json
import time
import threading

from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn

import blockchain

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    """Each request in a separate thread"""
    pass

class RequestHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        # Suppress logging
        return

    def do_POST(self):
        # lead different requests to their target function
        if self.path == "/vote":
            self.handle_vote()
        elif self.path == "/block":
            self.handle_block()
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")
    
    def handle_vote(self):
        # handle vote requests
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        # print("Received body:", post_data.decode('utf-8'))  # Debugging

        try:
            data = json.loads(post_data)
            block_id = data.get('block_id')
            if block_id:
                # print(f"The block id of the vote is {block_id}")
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"Vote Received")

                blockchain.process_vote(block_id)
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Missing block_id field")
        except json.JSONDecodeError:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid JSON")

    def handle_block(self):
        # handle block requests
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        # print("Received body:", post_data.decode('utf-8'))  # Debugging

        try:
            data = json.loads(post_data)
            block_id = data.get('id')
            view = data.get('view')
            if block_id and view:
                # print(f"The id of the block is {block_id}")
                # print(f"The view of the block is {view}")
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"Block Received")

                blockchain.add_pending_block(block_id, view)
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Missing block_id or view field")
        except json.JSONDecodeError:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid JSON")

def run(server_class=ThreadingHTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
