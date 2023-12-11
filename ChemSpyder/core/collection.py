import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator

from datetime import datetime as Datetime


@forge_signature
class Collection(sdRDM.DataModel):
    """The Collection serves as the root object of the data model and can hold multiple Species."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("collectionINDEX"),
        xml="@id",
    )

    name: Optional[str] = Field(
        default=None,
        description="An optional name for the Collection.",
    )

    created: Optional[Datetime] = Field(
        default=None,
        description="The timestamp of this Collection's creation.",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/torogi94/ChemSpyder"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="beaf1b83f535ac4155dab09fb9d3183a3b526dd9"
    )
