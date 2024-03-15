import socket
import select
import sys
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.IO import PEM
from .util import flatten_parameters_to_bytestring
import hmac
import hashlib
import base64

""" @author: Aron Nieminen, Mojang AB"""

class RequestError(Exception):
    pass

class Connection:
    """Connection to a Minecraft Pi game"""
    RequestFailed = "Fail"

    def __init__(self, address, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((address, port))
        self.pub_key = self.receive()
        self.secret_key = self.receive()
        self._convert_keys()
        self.lastSent = ""

    def _convert_keys(self):
        self.pub_key = base64.b64decode(self.pub_key)
        self.secret_key = base64.b64decode(self.secret_key)

    def drain(self):
        """Drains the socket of incoming data"""
        while True:
            readable, _, _ = select.select([self.socket], [], [], 0.0)
            if not readable:
                break
            data = self.socket.recv(1500)
            e =  "Drained Data: <%s>\n"%data.strip()
            e += "Last Message: <%s>\n"%self.lastSent.strip()
            sys.stderr.write(e)

    def send(self, f, *data):
        """
        Sends data. Note that a trailing newline '\n' is added here

        The protocol uses CP437 encoding - https://en.wikipedia.org/wiki/Code_page_437
        which is mildly distressing as it can't encode all of Unicode.
        """

        message = b"".join([f, b"(", flatten_parameters_to_bytestring(data), b")", b"\n"])

        # Encrypting message with public key
        public_key = RSA.import_key(self.pub_key)
        cipher = PKCS1_OAEP.new(public_key)
        message_encrypted = cipher.encrypt(message)

        # Combining the HMAC with the message using key
        hmac_msg = hmac.new(self.secret_key, message_encrypted, hashlib.sha256).digest()

        # Encode ciphertext and HMAC with base64
        b64_hmac_message = base64.b64encode(hmac_msg)
        b64_message_encrypted = base64.b64encode(message_encrypted)

        # Send encrypted message + MAC to server
        # print(f"HMAC bytes: {hmac_msg}, HMAC B64 (first 44 chars): {b64_hmac_message.decode('utf-8')}, Ciphertext B64 (After 44 chars): {b64_message_encrypted.decode('utf-8')}")
        self._send(b64_hmac_message + b64_message_encrypted)

    def _send(self, s):
        """
        The actual socket interaction from self.send, extracted for easier mocking
        and testing
        """
        self.drain()
        self.lastSent = s

        self.socket.sendall(s)

    def receive(self):
        """Receives data. Note that the trailing newline '\n' is trimmed"""
        s = self.socket.makefile("r").readline().rstrip("\n")
        if s == Connection.RequestFailed:
            raise RequestError("%s failed"%self.lastSent.strip())
        return s

    def sendReceive(self, *data):
        """Sends and receive data"""
        self.send(*data)
        return self.receive()
