import requests
from ..entities.function_entities import *
from app.entities.proxy_entity import ProxyEntity

class ProxyModel:

	@classmethod
	def get_proxys(cls, proxyApi:str)->List[ProxyEntity]:
		response = requests.get(
				"https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page=1&page_size=25",
				headers={"Authorization": f"Token {proxyApi}"}
			)
		proxiesJson = response.json()["results"]
		result = [ProxyEntity.from_dict(proxy) for proxy in proxiesJson]
		return result
	