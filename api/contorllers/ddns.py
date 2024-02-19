from flask import Blueprint
from flask_restful import reqparse

from services.ddns_service import DDNSService
from utils.return_data import JsonData

ddns_pb = Blueprint("ddns", __name__)


@ddns_pb.route("/aliyun", methods=["POST"])
def aliyun():
    parser = reqparse.RequestParser()
    parser.add_argument("domain_name", type=str, required=True, location="json")
    parser.add_argument("rr", type=str, required=True, location="json")
    parser.add_argument("value", type=str, required=True, location="json")
    parser.add_argument("type", type=str, required=True, location="json")
    parser.add_argument("ttl", type=int, required=True, location="json")
    args = parser.parse_args()
    provider = DDNSService.get_supplier()
    flag = provider.upgrade_records(
        domain_name=args["domain_name"],
        rr=args["rr"],
        value=args["value"],
        type=args["type"],
        ttl=args["ttl"]
    )
    if not flag:
        return JsonData.error(message="Error: Update failed")
    return JsonData.success(message="Success: Update completed")
