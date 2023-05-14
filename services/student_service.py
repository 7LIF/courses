from datetime import date
from random import randrange
from typing import List
from common.auth import hash_password
from common.common import (
    is_valid_email, 
    find_in,
)
from data.models import (
    Student, 
    Testimonial,
)



# variável que simula a base de dados - TEMPORARIAMENTE
_students = []



def get_student_by_email(email: str) -> Student | None:
    if not is_valid_email(email):
        raise ValueError(f'Endereço de email {email} inválido!')
    return find_in(_students, lambda students: students.email == email)


def create_account(
    name: str,
    email: str,
    birth_date: date,
    password: str,
):
    student = Student(
        randrange(10000, 100000),  # id
        name,
        email,
        birth_date,
        hash_password(password),
    )
    _students.append(student)
    return student


def student_count() -> int:
    return 2351


def get_testimonials(count: int) -> List[Testimonial]:
    return [
        Testimonial(
            user_id = 1,
            user_name = 'Francisco Mendonça',
            user_occupation = 'CEO & Fundador',
            text = 'Quidem odit voluptate, obcaecati, explicabo nobis corporis perspiciatis nihil',
        ),
        Testimonial(
            user_id = 2,
            user_name = 'Sara Albuquerque',
            user_occupation = 'Designer',
            text = 'Export tempor illum tamen malis malis eram quae irure esse labore quem cillum quid',
        ),
        Testimonial(
            user_id = 3,
            user_name = 'Ana Silva',
            user_occupation = 'Store Owner',
            text = 'Enim nisi quem export duis labore cillum quae magna enim sint quorum nulla quem ver',
        ),
        Testimonial(
            user_id = 4,
            user_name = 'Fabio Rodrigues',
            user_occupation = 'Freelancer',
            text = 'Fugiat enim eram quae cillum dolore dolor amet nulla culpa multos export minim fug',
        ),
        Testimonial(
            user_id = 5,
            user_name = 'João Pedro Valez',
            user_occupation = 'Entrepreneur',
            text = 'Quis quorun aliqua sint quem legam fore sunt eram irure aliquaveniamtempornoste',
        ),
    ][:count]