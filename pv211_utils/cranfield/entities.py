from typing import Any

from ..entities import DocumentBase, QueryBase


class CranfieldDocumentBase(DocumentBase):
    """A Cranfield collection document.

    Parameters
    ----------
    document_id : int
        A unique identifier of the document.
    authors : Any
        A unique identifiers of the authors of the document.
    bibliography : Any
        The bibliographical entry for the document.
    title : Any
        The title of the document.
    body : Any
        The abstract of the document.

    Attributes
    ----------
    authors : Any
        A unique identifiers of the authors of the document.
    bibliography : Any
        The bibliographical entry for the document.
    title : Any
        The title of the document.

    """
    def __init__(self, document_id: int, authors: Any, bibliography: Any, title: Any, body: Any):
        self.authors = authors
        self.bibliography = bibliography
        self.title = title
        super().__init__(document_id, body)


class CranfieldQueryBase(QueryBase):
    """A Cranfield collection query.

    Parameters
    ----------
    query_id : int
        A unique identifier of the query.
    body : Any
        The text of the query.

    """
    def __init__(self, query_id: int, body: Any):
        super().__init__(query_id, body)
