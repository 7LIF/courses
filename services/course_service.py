from typing import List
from decimal import Decimal as dec
from data.models import Course



def course_count() -> int:
    return 199


def most_popular_courses(count: int) -> List[Course]:
    return [
        Course(
            id = 1,
            category = 'Hotelaria e Turismo',
            subcategory = 'Gestão',
            price = dec(179),
            name = 'Gestor Turístico',
            summary = 'O curso de Gestor Turístico tem como objetivo formar profissionais capazes de gerir e desenvolver negócios na área do turismo em Portugal. Durante o curso, os alunos terão a oportunidade de aprender sobre planeamento estratégico, marketing turístico, gestão financeira, legislação do turismo, gestão de recursos humanos, entre outros temas relevantes para a gestão de empresas e destinos turísticos. Ao concluir o curso, os alunos estarão preparados para enfrentar os desafios do mercado turístico em constante evolução e contribuir para o desenvolvimento sustentável do turismo em Portugal.',
            trainer_id = 1,
            trainer_name = 'Ricardo Faria',
        ),
        Course(
            id = 2,
            category = 'Natação',
            subcategory = 'Estilos de Natação',
            price = dec(250),
            name = 'Estilo Borboleta',
            summary = 'O curso de natação estilo borboleta tem como objetivo ensinar aos alunos a teoria por trás da técnica do estilo borboleta. Durante o curso, os alunos irão estudar a biomecânica do movimento, a técnica de braçada, pernada, respiração e viradas. O curso será ministrado com a utilização de recursos audiovisuais e materiais didáticos. Os alunos terão a oportunidade de entender melhor como funciona o corpo durante a prática do estilo borboleta e aperfeiçoar seu conhecimento técnico.Ao final do curso, os alunos estarão aptos a compreender a técnica do estilo borboleta e os princípios teóricos que a sustentam, podendo aplicar esse conhecimento na prática para aprimorar seu desempenho na água.',
            trainer_id = 2,
            trainer_name = 'Camila Antunes',
        ),
        Course(
            id = 3,
            category = 'Programação',
            subcategory = 'Programação em C++',
            price = dec(250),
            name = 'Estruturas de Dados em C++',
            summary = 'O curso de Estruturas de Dados em C++ tem como objetivo ensinar aos alunos os fundamentos das estruturas de dados e como implementá-las utilizando a linguagem de programação C++. Durante o curso, os alunos irão aprender sobre conceitos como pilhas, filas, listas, árvores e grafos, bem como técnicas de ordenação e pesquisa. Os alunos terão a oportunidade de aplicar esses conceitos em exercícios práticos, desenvolvendo suas habilidades em programação e resolução de problemas. Além disso, irão aprender sobre a complexidade computacional das diferentes estruturas de dados e algoritmos. Ao final do curso, os alunos estarão aptos a utilizar as estruturas de dados para resolver problemas complexos de programação, melhorar a eficiência de seus algoritmos e desenvolver soluções mais robustas e eficientes em C++.',
            trainer_id = 3,
            trainer_name = 'Bernardo Nunes',
        ),
    ][:count]


def available_courses(count: int) -> List[Course]:
    return [
        Course(
            id = 5,
            category = 'Programação',
            subcategory = 'Programação Web',
            price = dec(198),
            name = 'Desenvolvimento de Websites',
            summary = 'Consectetur et, temporibus velit inventore porro sint dolore',
            trainer_id = 1,
            trainer_name = 'Ricardo Faria',
        ),
        Course(
            id = 6,
            category = 'Marketing',
            subcategory = 'Marketing',
            price = dec(250),
            name = 'SEO - Optimizações Motores de Busca',
            summary = 'Et architecto provident deleniti facere repellat nobis iste.',
            trainer_id = 3,
            trainer_name = 'Bernardo',
        ),
        Course(
            id = 7,
            category = 'Programação',
            subcategory = 'Programação Hardware',
            price = dec(250),
            name = 'Programação de Device Drivers',
            summary = 'Ex voluptatibus amet magnam maxime. Repellat quis eos laudar',
            trainer_id = 2,
            trainer_name = 'Camila Antunes',
        ),
        Course(
            id = 8,
            category = 'Electrónica',
            subcategory = 'Hardware',
            price = dec(280),
            name = 'Microsoldadura de SMD',
            summary = 'Esse est nemo dolorum tempora numquam dolorem in optio sed',
            trainer_id = 3,
            trainer_name = 'Bernardo Nunes',
        ),
    ][:count]