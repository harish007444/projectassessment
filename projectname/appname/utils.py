# Example code for generating and verifying JWT tokens
import jwt
from django.conf import settings

def generate_jwt_token(teacher_id, student_id):
    payload = {
        'teacher_id': teacher_id,
        'student_id': student_id,
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token

def verify_jwt_token(token):
    try:
        decoded_payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        teacher_id = decoded_payload['teacher_id']
        student_id = decoded_payload['student_id']
        # Check if teacher_id and student_id match the certificate in the database
        # Return True or False based on the verification result
        return True
    except jwt.ExpiredSignatureError:
        # Handle token expiration
        return False
    except jwt.InvalidTokenError:
        # Handle invalid token
        return False
