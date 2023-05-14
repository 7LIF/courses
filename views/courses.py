# Import necessary modules and functions
from fastapi import APIRouter, Request
from starlette.requests import Request
from fastapi_chameleon import template
from common.viewmodel import base_viewmodel_with
from services import course_service


# Create an instance of the router
router = APIRouter()


AVAILABLE_COURSES_COUNT = 3


@router.get('/courses')
@template()
async def courses(request: Request):
    return courses_viewmodel()


def courses_viewmodel():
    return base_viewmodel_with({
        'available_courses': course_service.available_courses(AVAILABLE_COURSES_COUNT),      
    })
    
    
@router.get('/courses/{course_id}')
@template()
async def courses_details():
    return {
        'id': '5',
        'category': 'Programação',
        'subcategory': 'Programação Web',
        'price': '198',
        'name': 'Desenvolvimento de Websites',
        'summary': 'Consectetur et, temporibus velit inventore porro sint dolore',
        'trainer_id': '1',
        'trainer_name': 'Ricardo Faria',
    }

