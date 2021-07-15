SPECS_DICT = {
    "parameters": [
        {
            "name": "module",
            "in": "query",
            "type": "string",
            "required": "true"
        }
    ],
    "definitions": {
        "Module": {
            "description": "Simplified module information for the academic year.", 
            "type": "object",
            "required": ["module_code", "module_name", "modular_credits","semesters"], 
            "properties": {
                "module_code": {
                    "type": "string"
                }, 
                "module_name": {
                    "type": "string"
                }, 
                "modular_credits": {
                    "type": "string"
                }, 
                "semesters": {
                    "type": "object",
                    "properties": {
                        "1": {
                            "$ref": "#/definitions/Semester"
                        },
                        "2": {
                            "$ref": "#/definitions/Semester"
                        },
                    }
                }
            }
        },
        "Semester": {
            "description": "Simplified module information for the semester.", 
            "type": "object",
            "required": ["groups", "exams", "lecturers"], 
            "properties": {
                "groups": {
                    "type": "array", 
                    "items": {
                        "type": "string"
                    }
                },
                "exams": {
                    "type": "array", 
                    "items": {
                        "type": "string"
                    }
                },
                "lecturers": {
                    "type": "array", 
                    "items": {
                        "type": "string"
                    }
                }
            }
        }
    },
    "responses": {
        "200": {
            "description": "THe module information in this current academic year.",
        }
    }
}
