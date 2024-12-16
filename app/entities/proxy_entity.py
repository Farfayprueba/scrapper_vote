from dataclasses import dataclass
from .function_entities import *

@dataclass
class ProxyEntity:
	ip       :  str
	port     :  str
	country  :  str
	city     :  str

	@staticmethod
	def from_dict(obj:Any) -> 'ProxyEntity':
		assert isinstance(obj, dict),"object is not dict"
		ip      = from_str(obj.get("ip"))
		port    = from_str(obj.get("port"))
		country = from_str(obj.get("country"))
		city    = from_str(obj.get("city"))
		return ProxyEntity(ip, port, country, city)
