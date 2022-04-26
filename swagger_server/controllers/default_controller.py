import connexion
import six

from swagger_server.models.ner_parse_body import NERParseBody  # noqa: E501
from swagger_server import util


def ner_parser(body):  # noqa: E501
    """Parses clinical text

    Parses text to retrieve Named Entities # noqa: E501

    :param body: Optional description in *Markdown*
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = NERParseBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
