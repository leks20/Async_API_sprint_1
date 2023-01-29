from typing import Dict


def get_body(
    query_: str, from_: int, size_: int, sort_by_: str, sort_order_: str
) -> Dict:
    return {
        "query": {"bool": {"must": [{"multi_match": {"query": query_}}]}},
        "sort": [{sort_by_: {"order": sort_order_}}],
        "from": from_,
        "size": size_,
    }
