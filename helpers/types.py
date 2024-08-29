from typing import Dict, Union, List, Any

JSONValue = Union[str, int, float, bool, None, List[Any], Dict[str, Any]]
JSONObject = Dict[str, JSONValue]
