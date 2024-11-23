import unittest
from utils.validators import validate_email, validate_password
from utils.helpers import generate_unique_id, calculate_age
from datetime import date

class TestUtils(unittest.TestCase):
    def test_email_validation(self):
        valid_emails = ['test@example.com', 'user.name@domain.co.uk']
        invalid_emails = ['invalid-email', 'missing@domain', '@incomplete.com']

        for email in valid_emails:
            self.assertTrue(validate_email(email))
        
        for email in invalid_emails:
            self.assertFalse(validate_email(email))

    def test_password_validation(self):
        valid_passwords = [
            'StrongPass123!', 
            'Secure@2024Password'
        ]
        invalid_passwords = [
            'short', 
            'onlylowercase', 
            'ONLYUPPERCASE', 
            'NoSpecialChar123'
        ]

        for password in valid_passwords:
            self.assertTrue(validate_password(password))
        
        for password in invalid_passwords:
            self.assertFalse(validate_password(password))

    def test_age_calculation(self):
        today = date.today()
        birthdate = date(2000, 1, 1)
        age = calculate_age(birthdate)
        
        self.assertIsInstance(age, int)
        self.assertTrue(age >= 20 and age <= 30)

    def test_unique_id_generation(self):
        ids = [generate_unique_id() for _ in range(100)]
        self.assertEqual(len(set(ids)), 100)

if __name__ == '__main__':
    unittest.main()