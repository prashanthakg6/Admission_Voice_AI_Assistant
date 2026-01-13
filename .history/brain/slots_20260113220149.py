# brain/slots.py

REQUIRED_SLOTS = {
    "COURSE_QUERY": ["course_name"],
    "ELIGIBILITY": ["course_name"],
    "FEES": ["course_name"],
    "DEADLINES": ["course_name"],
    "DOCUMENTS": ["course_name"],
}

OPTIONAL_SLOTS = {
    "ELIGIBILITY": ["percentage", "subjects", "exam_type"],
    "FEES": ["hostel_required"],
}
