from pydantic import BaseModel

class QnAReviews(BaseModel):
    number_of_questions: int = 0
    has_valid_question_answer_data: bool = None
    total_number_of_pages_question_answer_data: int = 0
    number_of_questions_listed_on_a_page: int = 0
    total_number_of_reviews: int = 0
    star_rating: float = 0.0
