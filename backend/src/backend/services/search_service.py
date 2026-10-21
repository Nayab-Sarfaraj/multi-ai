import logging

from elasticsearch import Elasticsearch, TransportError

from backend.config.settings import settings

logger = logging.getLogger(__name__)


class SearchService:
    def __init__(self) -> None:
        client_options: dict[str, str | tuple[str, str]] = {}
        if settings.elasticsearch_api_key:
            client_options["api_key"] = settings.elasticsearch_api_key
        elif settings.elasticsearch_password:
            client_options["basic_auth"] = (
                settings.elasticsearch_user,
                settings.elasticsearch_password,
            )

        self._client = Elasticsearch(settings.elasticsearch_url, **client_options)

    @property
    def available(self) -> bool:
        try:
            return self._client.ping()
        except TransportError as exc:
            logger.warning("Elasticsearch health check failed: %s", exc)
            return False
