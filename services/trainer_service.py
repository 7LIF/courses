from typing import List
from data.models import Trainer


def trainer_count() -> int:
    return 2315



def select_trainers(count: int) -> List[Trainer]:
    return [
        Trainer(
            id = 1,
            name = 'Ricardo Faria',
            expertise = 'Gestão de Turismo',
            presentation = 'Quidem odit voluptate, obcaecati, explicabo nobis corporis perspiciatis nihil',
            twitter = 'https://twitter.com',
            facebook = 'https://www.facebook.com',
            instagram = 'https://www.instagram.com',
            linkedin = 'https://www.linkedin.com',
        ),
        Trainer(
            id = 2,
            name = 'Camila Antunes',
            expertise = 'Nadadora Profissional',
            presentation = 'Quidem odit voluptate, obcaecati, explicabo nobis corporis perspiciatis nihil',
            twitter = 'https://twitter.com',
            facebook = 'https://www.facebook.com',
            instagram = 'https://www.instagram.com',
            linkedin = 'https://www.linkedin.com',
        ),
        Trainer(
            id = 3,
            name = 'Bernardo Nunes',
            expertise = 'Programador',
            presentation = 'Quidem odit voluptate, obcaecati, explicabo nobis corporis perspiciatis nihil',
            twitter = 'https://twitter.com',
            facebook = 'https://www.facebook.com',
            instagram = 'https://www.instagram.com',
            linkedin = 'https://www.linkedin.com',
        ),
    ][:count]

