from requests import get
from bs4 import BeautifulSoup

from utils.models import (
    LessonData,
    SemesterData
)
from utils.constants import (
    LESSON_INDICATORS,
    MODULAR_CREDIT_HEADER,
    SEMESTER_ONE,
    SEMESTER_TWO,
    COURSE_SCHEDULE_URL,
    GROUP_HEADER,
    EXAM_HEADER
)


def is_not_lesson(elem):
    for indicator in LESSON_INDICATORS:
        if indicator in elem.strip():
            return False

    return True


def parse_module_code(element, module_data):
    module_data.add_module_code(element.text)


def parse_module_ext_info(element, module_data):
    data = element.text.replace(MODULAR_CREDIT_HEADER, "\n")
    ext_info = data.split("\n")

    module_data.add_module_name(ext_info[0].strip())
    module_data.add_modular_credits(ext_info[1].strip())


def parse_module_data(element, module_data, semester_number):
    semester_data = SemesterData()

    for elem in element.recursiveChildGenerator():
        # Is Lecture / Sectional Teaching
        if isinstance(elem, str) and GROUP_HEADER in elem.strip():
            semester_data.add_group(elem.strip())
        # Is Exam
        elif isinstance(elem, str) and EXAM_HEADER in elem.strip():
            semester_data.add_exam(elem.strip())
        # Is Lecturer
        elif isinstance(elem, str) and is_not_lesson(elem):
            if elem.strip() != "-":
                semester_data.add_lecturer(elem.strip())
        # Is Lesson
        elif isinstance(elem, str):
            semester_data.append_group_info(elem.strip())

    if semester_data.is_not_available():
        return

    if semester_number == SEMESTER_ONE:
        module_data.add_semester_one_info(semester_data.to_dict())
    elif semester_number == SEMESTER_TWO:
        module_data.add_semester_two_info(semester_data.to_dict())


def get_module_data(module):
    data = get(COURSE_SCHEDULE_URL)
    soup = BeautifulSoup(data.text, features="html.parser")

    table_data = soup.findChildren("table")[0]
    table_rows = table_data.findChildren(['th', 'tr'])

    for table_row in table_rows:
        module_data = LessonData()
        module_information = table_row.findChildren(["td"])

        if len(module_information) == 0:
            continue

        module_code = module_information[0].text

        if module_code != module:
            continue

        parse_module_code(module_information[0], module_data)
        parse_module_ext_info(module_information[1], module_data)
        parse_module_data(module_information[2], module_data, SEMESTER_ONE)
        parse_module_data(module_information[3], module_data, SEMESTER_TWO)

        return module_data.to_json()

    return None
