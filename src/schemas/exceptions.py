from fastapi import HTTPException

NotSuperUserException = HTTPException(status_code=403, detail="You are not a superuser")
