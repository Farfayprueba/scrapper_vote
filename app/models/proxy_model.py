import requests
from ..entities.function_entities import *
from app.entities.proxy_entity import ProxyEntity

class ProxyModel:

	@classmethod
	def get_proxys(cls, proxyApi: str, country: str = None) -> List[ProxyEntity]:
		all_proxies = []
		page = 1
		page_size = 100 
		while True and page <= 8:
			response = requests.get(
				f"https://proxy.webshare.io/api/v2/proxy/list/?mode=direct&page={page}&page_size={page_size}",
				headers={"Authorization": f"Token {proxyApi}"}
			)
			if response.status_code != 200:
				raise Exception(f"Error {response.status_code}: {response.text}")
			data = response.json()
			proxiesJson = data["results"]
			if country:
				proxiesJson = [proxy for proxy in proxiesJson if proxy.get("country_code") == country.upper()]
			all_proxies.extend([ProxyEntity.from_dict(proxy) for proxy in proxiesJson])
			if not data.get("next"):
				break
			page += 1
		all_proxies.sort(key=lambda proxy: proxy.ip)
		return all_proxies