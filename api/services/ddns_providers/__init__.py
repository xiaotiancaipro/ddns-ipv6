from .base import DDNSRecord, DDNS
from .provider_aliyun import AliyunDDNS

PROVIDERS = {
    "aliyun": AliyunDDNS(),
}
__all__ = ["DDNSRecord", "DDNS", "PROVIDERS"]
