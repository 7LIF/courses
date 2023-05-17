################################################################################
##      Importing necessary modules
################################################################################

from datetime import date, datetime
from decimal import Decimal as dec
from dataclasses import dataclass, field


################################################################################
##      Defining the Course class with attributes
################################################################################

@dataclass
class Course:
    id: int
    category: str
    subcategory: str
    price: dec
    name: str
    summary: str
    trainer_id: int
    trainer_name: str


################################################################################
##      Defining the Trainer class with attributes
################################################################################   

@dataclass
class Trainer:
    id: int
    name: str
    expertise: str
    presentation: str
    twitter: str
    facebook: str
    instagram: str
    linkedin: str


################################################################################
##      Defining the Trainer class with attributes
################################################################################  

@dataclass
class Student:
    id: int
    name: str
    email_addr: str
    birth_date: date
    password: str
    profile_img_url: str | None = None
    created_date: date = field(default_factory=date.today)
    last_login: datetime = field(default_factory=date.today)


################################################################################
##      Defining the Testimonial class with attributes
################################################################################  

@dataclass
class Testimonial:
    user_id: int
    user_name: str
    user_occupation: str
    text: str