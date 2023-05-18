################################################################################
##      Importing necessary modules
################################################################################

from datetime import date
from fastapi import APIRouter, Request, Response, Depends, responses, status
from fastapi_chameleon import template
from common.auth import requires_unauthentication, requires_authentication, set_auth_cookie, delete_auth_cookie, get_current_user, exec_login
from common.common import is_valid_name, is_valid_email, is_valid_birth_date, is_valid_password, is_valid_iso_date
from common.fastapi_utils import form_field_as_str
from common.viewmodel import ViewModel
from services import student_service
from services.student_service import authenticate_student_by_email, get_student_by_email

################################################################################
##      Create an instance of the router
################################################################################

router = APIRouter()




MIN_DATE = date.fromisoformat('1920-01-01')








################################################################################
##      Define a route for the account page
################################################################################

@router.get(
    '/account',
    dependencies = [Depends(requires_authentication)]
)
@template()
async def account():
    return account_viewmodel()
    
def account_viewmodel():
    student = get_current_user()
    assert student is not None
       
    return ViewModel(
        name = student.name,
        email_addr = student.email_addr,     
    )




################################################################################
##     Handling the POST request and view model for account page
################################################################################

@router.post(
    '/account',
    dependencies = [Depends(requires_authentication)]
)
@template(template_file='account/account.html')
async def update_account(request: Request):
    vm = await update_account_viewmodel(request)
    
    if vm.error:
        return vm
    
    return responses.RedirectResponse(url='/', status_code = status.HTTP_302_FOUND)


async def update_account_viewmodel(request: Request):
    form_data = await request.form()
    student = get_current_user()
    assert student is not None
    
    vm = ViewModel()
    vm.error_msg = ''
    vm.name = student.name
    vm.email_addr = form_field_as_str(form_data, 'email_addr').strip()
    new_email = None if vm.email_addr == student.email_addr else vm.email_addr
    current_password = form_field_as_str(form_data, 'current_password').strip()
    new_password = form_field_as_str(form_data, 'new_password').strip()
    
    if not student_service.password_matches(student, current_password):
        vm.error_msg = 'Palavra-passe errada!'
    elif new_email:
        if not is_valid_email(new_email):
            vm.error_msg = f'Endereço de email {new_email} inválido!'
        elif student_service.get_student_by_email(new_email):
            vm.error_msg = f'O endereço de email {new_email} já está registado!'
    elif not is_valid_password(new_password):
        vm.error_msg = 'Palavra-passe inválida!'
    elif student_service.password_matches(student, current_password):
        vm.error_msg = 'A nova palavra-passe não pode ser igual à anterior!'
    
    vm.error = bool(vm.error_msg)
    
    if not vm.error:
        student_service.update_account(
            student.id,
            current_password,
            new_email,
            new_password,
        )
    
    return vm














################################################################################
##      Define a route and View model for the register page
################################################################################

@router.get(
    '/account/register',
    dependencies = [Depends(requires_unauthentication)]
)
@template()
async def register():  
    return register_viewmodel()


def register_viewmodel():
    return ViewModel(
        name = '',
        email_addr = '',
        birth_date = '',
        min_date = MIN_DATE,
        max_date = date.today(),
        password = '',
        checked = False,
    )


################################################################################
##     Handling the POST request and view model for registration
################################################################################

@router.post(
    '/account/register',
    dependencies = [Depends(requires_unauthentication)]
)
@template(template_file='account/register.html')
async def post_register(request: Request):
    vm = await post_register_viewmodel(request)

    if vm.error:
        return vm
    
    return exec_login(vm.new_student_id)




async def post_register_viewmodel(request: Request):
    form_data = await request.form()
    vm = ViewModel(
        name = form_field_as_str(form_data, 'name'),
        email_addr = form_field_as_str(form_data, 'email_addr'),
        birth_date = form_field_as_str(form_data, 'birth_date'),
        password = form_field_as_str(form_data, 'password'),
        new_student_id = None
    )

    if not is_valid_name(vm.name):
        vm.error, vm.error_msg = True, 'Nome inválido!'
    elif not is_valid_email(vm.email_addr):
        vm.error, vm.error_msg = True, 'Endereço de email inválido!'
    elif not is_valid_birth_date(vm.birth_date):
        vm.error, vm.error_msg = True, 'Data de nascimento inválida!'
    elif not is_valid_password(vm.password):
        vm.error, vm.error_msg = True, 'Palavra-passe inválida!'
    elif student_service.get_student_by_email(vm.email_addr):
        vm.error, vm.error_msg = True, f'O endereço de email {vm.email_addr} já está registado!'
    else:
        vm.error, vm.error_msg = False, ''

    if not vm.error:
        student = student_service.create_account(
            vm.name,
            vm.email_addr,
            date.fromisoformat(vm.birth_date),
            vm.password,
        )
        vm.new_student_id = student.id

    return vm


################################################################################
##      Define a route and View model for the login page
################################################################################

@router.get(
    '/account/login',
    dependencies = [Depends(requires_unauthentication)]
)
@template()
async def login():
    return login_viewmodel()
    
def login_viewmodel():
    return ViewModel(
        email_addr = '',
        password = '',  
    )




################################################################################
##     Handling the POST request and view model for login
################################################################################

@router.post(
    '/account/login',
    dependencies = [Depends(requires_unauthentication)]
)
@template(template_file='account/login.html')
async def post_login(request: Request):
    vm = await post_login_viewmodel(request)

    if vm.error:
        return vm
    
    return exec_login(vm.student_id)




async def post_login_viewmodel(request: Request) -> ViewModel:
    form_data = await request.form()
    vm = ViewModel(
        email_addr = form_field_as_str(form_data, 'email_addr'),
        password = form_field_as_str(form_data, 'password'),
        student_id = None,
    )

    if not is_valid_email(vm.email_addr):
        vm.error, vm.error_msg = True, 'Inválido utilizador ou palavra-passe!'
    elif not is_valid_password(vm.password):
        vm.error, vm.error_msg = True, 'Palavra-passe inválida!'
    elif not (student := student_service.authenticate_student_by_email(vm.email_addr, vm.password)):
        vm.error, vm.error_msg = True, 'Utilizador não encontrado!'
    else:
        vm.error, vm.error_msg = False, ''
        vm.student_id = student.id

    return vm

  

################################################################################
##      Define a route and View model for the logout page
################################################################################

@router.get(
    '/account/logout',
    dependencies = [Depends(requires_authentication)]
)
async def logout():
    response = responses.RedirectResponse(url='/', status_code = status.HTTP_302_FOUND)
    delete_auth_cookie(response)
    return response
