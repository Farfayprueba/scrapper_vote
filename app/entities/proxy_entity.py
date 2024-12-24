from dataclasses import dataclass
from .function_entities import *

@dataclass
class ProxyEntity:
	ip      : str
	port    : str
	username: str
	password: str

	@staticmethod
	def from_dict(obj:Any) -> 'ProxyEntity':
		assert isinstance(obj, dict),"object is not dict"
		ip      = from_str(obj.get("proxy_address"))
		port    = from_str(obj.get("port"))
		username    = from_str(obj.get("username"))
		password    = from_str(obj.get("password"))
		return ProxyEntity(ip, port, username, password)
