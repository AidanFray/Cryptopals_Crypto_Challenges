import base64
import unittest
import commonTestCode

# SET 2
import Set2.Challenge9.Challenge9 as c9
import Set2.Challenge10.Challenge10 as c10
import Set2.Challenge11.Challenge11 as c11
import Set2.Challenge12.Challenge12 as c12
import Set2.Challenge13.Challenge13 as c13
import Set2.Challenge14.Challenge14 as c14
import Set2.Challenge15.Challenge15 as c15
import Set2.Challenge16.Challenge16 as c16


class Set2(unittest.TestCase):

    def test_C9(self):
        expected = "YELLOW SUBMARINE\x04\x04\x04\x04"
        actual = c9.task9()

        self.assertEqual(actual, expected)

    def test_C10(self):
        expected = commonTestCode.loadData("/../Set2/Challenge10/data.txt")
        actual = str(c10.task10())[2:-1]

        self.assertEqual(actual, expected)

    def test_C11(self):

        # Repeats the test
        for _ in range(500):

            # Obtains the chosen mode, and the actual mode
            expected, actual = c11.task11()
            self.assertEqual(actual, expected)

    def test_C12(self):
        expected = base64.b64decode(c12.appendString).decode('utf-8')
        actual = c12.task12()

        self.assertEqual(actual, expected)

    def test_C13_decode(self):
        testInput = "foo=bar&baz=qux&zap=zazzle"

        expected = "{\n  foo: 'bar',\n  baz: 'qux',\n  zap: 'zazzle'\n}"
        actual = c13.decode(testInput)

        self.assertEqual(actual, expected)

    def test_C13_encode(self):
        testInput = "{\n  foo: 'bar',\n  baz: 'qux',\n  zap: 'zazzle'\n}"

        expected = "foo=bar&baz=qux&zap=zazzle"
        actual = c13.encode(testInput)

        self.assertEqual(actual, expected)

    def test_C13_encode_decode(self):
        testInput = "test=great&outcome=correct&time=wellspent&percentage=100"

        expected = testInput
        actual = c13.encode(c13.decode(testInput))

        self.assertEqual(actual, expected)

    def test_C13_profile_gen(self):

        expected = "email=foo@bar.com&uid=10&role=user"
        actual = c13.profile_for("foo@bar.com")

        self.assertEqual(actual, expected)

    def test_C13_profile_invalid(self):
        with self.assertRaises(Exception) as context:
            c13.profile_for("foo@bar.com&role=admin")

        # Checks exception message
        self.assertEqual("Invalid email!", context.exception.args[0])

    def test_C13_encrypt_decrypt(self):
        expected = "test=great&outcome=correct&time=wellspent&percentage=100"

        # Super secret
        key = b'gHEvzQiiVFtkppxjAKiweg=='

        e = c13.encrypt_user_profile(expected, key)
        actual = c13.decrypt_user_profile(e, key)

        self.assertEqual(actual, expected)

    def test_C14(self):
        # [2:-1] Is removing the b'' notation
        expected = str(base64.b64decode(c14.target_bytes))[2:-1]
        actual = c14.task14()

        self.assertEqual(actual, expected)

    def test_C15(self):
        c15.task15()

    def test_C16(self):
        self.assertEqual(c16.task16(), True)
