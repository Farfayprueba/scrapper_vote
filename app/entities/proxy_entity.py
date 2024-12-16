from dataclasses import dataclass
from .function_entities import *

@dataclass
class ProxyEntity:
	ip       :  str
	port     :  str

	@staticmethod
	def from_dict(obj:Any) -> 'ProxyEntity':
		assert isinstance(obj, dict),"object is not dict"
		ip      = from_str(obj.get("proxy_address"))
		port    = from_str(obj.get("port"))
		return ProxyEntity(ip, port)
