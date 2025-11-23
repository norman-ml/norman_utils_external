import json
from typing import Dict

from starlette.types import Message, Scope, Receive


class HttpUtils:
    @staticmethod
    def decode_headers(scope: Scope):
        raw_headers = scope.get("headers") or []

        headers: Dict[str, str] = {}
        for name_bytes, value_bytes in raw_headers:
            name = name_bytes.decode()
            value = value_bytes.decode()
            headers[name] = value

        return headers

    @staticmethod
    async def read_body(receive: Receive):
        body = b""
        more_body = True
        while more_body:
            message = await receive()
            body += message.get("body", b"")
            more_body = message.get("more_body", False)
        return body

    @staticmethod
    def replay_body_receive(body_bytes: bytes):
        sent = {"done": False}

        async def receive_replay() -> Message:
            if not sent["done"]:
                sent["done"] = True
                return {"type": "http.request", "body": body_bytes, "more_body": False}
            return {"type": "http.request", "body": b"", "more_body": False}

        return receive_replay

    @staticmethod
    def parse_body_as_json(body_bytes: bytes):
        if not body_bytes:
            return {}
        try:
            return json.loads(body_bytes.decode("utf-8"))
        except Exception:
            return {}
