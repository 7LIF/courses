################################################################################
##      Importing necessary modules
################################################################################
from fastapi import APIRouter
from fastapi_chameleon import template
from services import course_service, student_service, trainer_service
from common.viewmodel import ViewModel



################################################################################
##      Constants
################################################################################

POPULAR_COURSES_COUNT = 3
SELECTED_COURSES_COUNT = 3
SELECTED_TRAINERS_COUNT = 3
TESTIMONIALS_COUNT = 5



################################################################################
##      Create an instance of the router
################################################################################

router = APIRouter()



################################################################################
##      Define a route for the index/home page
################################################################################

@router.get('/')
@template()
async def index():
    return index_viewmodel()


def index_viewmodel():
    return ViewModel(
        num_courses = course_service.course_count(),
        num_students = student_service.student_count(),
        num_trainers = trainer_service.trainer_count(),
        num_events = 159,
        popular_courses = course_service.most_popular_courses(POPULAR_COURSES_COUNT),
        selected_trainers = trainer_service.select_trainers(SELECTED_TRAINERS_COUNT)
    )



################################################################################
##      Define a route for the about page
################################################################################

@router.get('/about')
@template()
async def about():
    return about_viewmodel()  
    
    
def about_viewmodel():
    return ViewModel(
        num_courses = course_service.course_count(),
        num_students = student_service.student_count(),
        num_trainers = trainer_service.trainer_count(),
        num_events = 159,
        testimonials = student_service.get_testimonials(TESTIMONIALS_COUNT)
    )            
            
