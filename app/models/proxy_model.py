import requests
from ..entities.function_entities import *
from app.entities.proxy_entity import ProxyEntity

class ProxyModel:

	@classmethod
	def get_proxys(cls, proxyApi: str) -> List[ProxyEntity]:
		all_proxies = []
		page = 1
		page_size = 100 
		while True:
			response = requests.get(
				f"https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page={page}&page_size={page_size}",
				headers={"Authorization": f"Token {proxyApi}"}
			)
			if response.status_code != 200:
				raise Exception(f"Error {response.status_code}: {response.text}")
			data = response.json()
			proxiesJson = data["results"]
			all_proxies.extend([ProxyEntity.from_dict(proxy) for proxy in proxiesJson])
			if not data.get("next"):
				break
			page += 1
		return all_proxies