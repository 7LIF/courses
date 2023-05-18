################################################################################
##      Specifies the public interface of this module
################################################################################

all = (
    'requires_unauthentication'
    'exec_login',
    'get_current_user',
    'set_auth_cookie',
    'get_auth_from_cookie',
    'delete_auth_cookie',
    'hash_cookie_value',
)


################################################################################
##      Importing necessary modules
################################################################################

from hashlib import sha512
from fastapi import Request, Response, responses, status, HTTPException
from data.models import Student
from common.fastapi_utils import global_request
from services import student_service
from services.student_service import get_student_by_id


################################################################################
##      Constants
################################################################################

AUTH_COOKIE_NAME = 'user_id'
SESSION_COOKIE_MAX_AGE = 86400_00          # 86400 seconds =~ 1 day // 86400_00 seconds =~ 100 days
SECRET_KEY = '8e10d234a1f8eb6f9dd6dfc3a325a0613ad2e620e5b8844cb011470492422bee'





def requires_authentication():
    if not get_current_user():
        raise HTTPUnauthorizedAccess(detail = 'This area requires authentication!')

class HTTPUnauthorizedAccess(HTTPException):
    def __init__(self, *args, **kargs):
        super().__init__(status_code = status.HTTP_401_UNAUTHORIZED, *args, **kargs)






def requires_unauthentication():
    if get_current_user():
        raise HTTPUnauthenticatedOnly(detail = 'This is a public area only!')     
        
class HTTPUnauthenticatedOnly(HTTPUnauthorizedAccess):
    pass









def get_current_user() -> Student | None:
    if student_id := get_auth_from_cookie(global_request.get()):
        return student_service.get_student_by_id(student_id)
    return None




def exec_login(user_id: int) -> Response:
    response = responses.RedirectResponse(url='/', status_code = status.HTTP_302_FOUND)
    set_auth_cookie(response, user_id)
    return response




def set_auth_cookie(response: Response, user_id: int):
    cookie_value = f'{str(user_id)}:{hash_cookie_value(str(user_id))}'
    response.set_cookie(
        AUTH_COOKIE_NAME,
        cookie_value,
        secure = False,             # True -> a cookie só é enviada por HTTPs
        httponly = True,
        samesite = 'lax',
        max_age= SESSION_COOKIE_MAX_AGE,
    )






def get_auth_from_cookie(request: Request) -> int | None:
    if not (cookie_value := request.cookies.get(AUTH_COOKIE_NAME)):
        return None
    
    parts = cookie_value.split(':')
    if len(parts) != 2:
        return None
    
    user_id, hash_value = parts
    hash_check_value = hash_cookie_value(user_id)
    if hash_value != hash_check_value:
        print("Warning: hash mismatch. Invalid cookie value!")
        return None
    
    return int(user_id) if user_id.isdigit() else None







def delete_auth_cookie(response: Response):
    response.delete_cookie(AUTH_COOKIE_NAME)
    



def hash_cookie_value(cookie_value: str) -> str:
    return sha512(f'{cookie_value}{SECRET_KEY}'.encode('utf-8')).hexdigest()



