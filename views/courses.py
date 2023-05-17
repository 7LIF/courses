# Import necessary modules and functions
from fastapi import APIRouter, Request
from fastapi_chameleon import template
from common.viewmodel import ViewModel
from services import course_service
from decimal import Decimal as dec


# Create an instance of the router
router = APIRouter()


AVAILABLE_COURSES_COUNT = 3


@router.get('/courses')
@template()
async def courses(request: Request):
    return courses_viewmodel()


def courses_viewmodel():
    return ViewModel(
        available_courses = course_service.available_courses(AVAILABLE_COURSES_COUNT)   
    )



################################################################################
##      Define a route for the course_details page
################################################################################  
    
@router.get('/courses/{course_id}')
@template()
async def course_details(course_id: int):
    return course_details_viewmodel(course_id)

def course_details_viewmodel(course_id: int):
    if course := course_service.get_course_by_id(course_id):
        return ViewModel(
            course = course
            #id = 5,
            #category = 'Programação',
            #subcategory = 'Programação Web',
            #price = dec(198),
            #name = 'Desenvolvimento de Websites',
            #summary = 'Consectetur et, temporibus velit inventore porro sint dolore',
            #trainer_id = 1,
            #trainer_name = 'Ricardo Faria',
    )
    return ViewModel(
        error = None,
        error_msg = 'Curso não encontrado',
    )
