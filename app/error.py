from fastapi import Request
from fastapi.responses import JSONResponse


async def general_exception_handler(
    request: Request,
    exc: Exception
):
    # In production, we will log the real error here.
    # The user should NOT see the technical error details.

    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error"
        }
    )