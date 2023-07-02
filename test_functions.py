import unittest
import random
from typing import List

class MyFunctionsTest(unittest.TestCase):

    def test_sum(self):
        # Test case 1: Testing positive numbers
        result = sum(2, 3)
        self.assertEqual(result, 5)

        # Test case 2: Testing negative numbers
        result = sum(-5, -7)
        self.assertEqual(result, -12)

        # Test case 3: Testing zero
        result = sum(0, 10)
        self.assertEqual(result, 10)

        # Test case 4: Testing random numbers
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        result = sum(a, b)
        self.assertEqual(result, a + b)

    def test_get_bucket_name_from_response(self):
        # Test case 1: Testing with sample response data
        data = {
            'Buckets': [
                {'Name': 'bucket1'},
                {'Name': 'bucket2'},
                {'Name': 'bucket3'}
            ]
        }
        expected_result = ['bucket1', 'bucket2', 'bucket3']
        result = get_bucket_name_from_response(data)
        self.assertEqual(result, expected_result)

        # Test case 2: Testing with an empty response
        data = {'Buckets': []}
        expected_result = []
        result = get_bucket_name_from_response(data)
        self.assertEqual(result, expected_result)

        # Test case 3: Testing with random response data
        buckets = [{'Name': f'bucket{i}'} for i in range(10)]
        data = {'Buckets': buckets}
        expected_result = [bucket['Name'] for bucket in buckets]
        result = get_bucket_name_from_response(data)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
