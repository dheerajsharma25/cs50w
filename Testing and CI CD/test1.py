import unittest

from prime import is_prime

class Tests(unittest.TestCase):

	def test_1(self):
		"""Check that 1 is not prime. """
		self.assertFalse(is_prime(1))

	def test_2(self):
		"""Check that 2 is  prime. """
		self.assertTrue(is_prime(2))

	def test_8(self):
		"""Check that 8 is not prime. """
		self.assertFalse(is_prime(8))

	def test_11(self):
		"""Check that 11 is not prime. """
		self.assertTrue(is_prime(11))

	def test_21(self):
		"""Check that 21 is not prime. """
		self.assertFalse(is_prime(21))

	def test_28(self):
		"""Check that 28 is not prime. """
		self.assertFalse(is_prime(28))

	def test_7(self):
		"""Check that 7 is prime. """
		self.assertTrue(is_prime(7))


if  __name__ == "__main__":
	unittest.main()