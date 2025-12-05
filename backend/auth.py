from fastapi import HTTPException, Request
from functools import wraps

from config import X_API_KEY


def require_api_key(func):
    """
    Decorator to require API key authentication
    """

    @wraps(func)
    async def wrapper(*args, **kwargs):
        # Extract request from kwargs or args
        request = None
        for arg in args:
            if isinstance(arg, Request):
                request = arg
                break
        if not request:
            # If no Request object found, check if it's in kwargs
            for key, value in kwargs.items():
                if isinstance(value, Request):
                    request = value
                    break
        if not request:
            raise HTTPException(
                status_code=500,
                detail="Internal server error: Request object not found",
            )
        # Get API key from headers
        api_key = request.headers.get("X-API-Key")
        if not api_key or api_key != X_API_KEY:
            raise HTTPException(status_code=401, detail="Invalid or missing API key")
        return await func(*args, **kwargs)

    return wrapper
