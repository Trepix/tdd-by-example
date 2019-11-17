from WasRun import WasRun
from TestCase import TestCase


class TestCaseTest(TestCase):

    def setUp(self):
        pass

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert ("setUp testMethod tearDown " == test.log)


TestCaseTest("testTemplateMethod").run()
