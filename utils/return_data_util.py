from flask import jsonify


class JsonData:

    def __init__(self, code: int, data: dict | None, message: str):
        self.code = code
        self.data = data
        self.message = message

    def to_json(self):
        return jsonify({"code": self.code, "message": self.message, "data": self.data})

    @classmethod
    def error(cls, message: str):
        return cls(code=500, data=None, message=message).to_json()

    @classmethod
    def success(cls, message: str, data: dict | None = None):
        return cls(code=200, data=data, message=message).to_json()

    @classmethod
    def build(cls, code: int, data: dict | None, message: str):
        return cls(code=code, message=message, data=data).to_json()
