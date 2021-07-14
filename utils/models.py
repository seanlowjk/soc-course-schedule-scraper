from json import dumps

from utils.constants import DEFAULT_INDENT


class LessonData:
    def __init__(self):
        self.module_code = None
        self.module_name = None
        self.modular_credits = None
        self.semester_one_info = None
        self.semester_two_info = None

    def add_module_code(self, module_code):
        self.module_code = module_code

    def add_module_name(self, module_name):
        self.module_name = module_name

    def add_modular_credits(self, modular_credits):
        self.modular_credits = modular_credits

    def add_semester_one_info(self, semester_one_info):
        self.semester_one_info = semester_one_info

    def add_semester_two_info(self, semester_two_info):
        self.semester_two_info = semester_two_info

    def to_json(self):
        result = {
            "module_code": self.module_code,
            "module_name": self.module_name,
            "modular_credits": self.modular_credits,
            "semesters": {},
        }

        if self.semester_one_info is not None:
            result["semesters"]["1"] = self.semester_one_info

        if self.semester_two_info is not None:
            result["semesters"]["2"] = self.semester_two_info

        return dumps(result, indent=DEFAULT_INDENT)


class SemesterData:
    def __init__(self):
        self.groups = []
        self.exams = []
        self.lecturers = []

    def add_group(self, group):
        self.groups.append(group)

    def add_lecturer(self, lecturer):
        self.lecturers.append(lecturer)

    def add_exam(self, exam):
        self.exams.append(exam)

    def append_group_info(self, data):
        self.groups[-1] += " " + data

    def is_not_available(self):
        return len(self.groups) == 0 \
            and len(self.lecturers) == 0 \
            and len(self.exams) == 0

    def to_dict(self):
        return {
            "groups": self.groups,
            "exams": self.exams,
            "lecturers": self.lecturers
        }
