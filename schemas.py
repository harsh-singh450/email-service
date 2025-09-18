from pydantic import BaseModel, EmailStr
from typing import List, Dict, Any, Union

class EmailSchema(BaseModel):
    recipients: List[EmailStr]
    subject: str
    # The body can now be a dictionary for templates or a simple string
    body: Union[Dict[str, Any], str]