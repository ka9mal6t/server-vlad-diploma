from fastapi import HTTPException
from starlette import status

UserAlreadyExistException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="User already exist"
)

IncorrectEmailOrPasswordException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect email or password"
)

TokenExpiredTokenException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Token expired"
)

TokenAbsentException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Token is absent"
)

IncorrectTokenFormatException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect token format"
)

UserIsNotExistException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED)


NotCorrectedDataException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Not corrected data"
)

UserIsNotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="User in not found"
)

FriendAlreadyExistException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="User in not found"
)

AttemptsIsLimitedException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Attempts is limited"
)

IncorrectCodeException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Code not found"
)


