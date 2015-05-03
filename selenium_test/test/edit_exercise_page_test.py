import unittest
from selenium_test.test_initializer import TestInitializer
from selenium_test.page_objects.page_objects import LoginPage, EditExercisePage, CourseName

class EditExercisePageTest(unittest.TestCase):
    def setUp(self):
        self.driver = TestInitializer().getFirefoxDriverWithLoggingEnabled()
        TestInitializer().recreateDatabase()
        LoginPage(self.driver).loginToCourse(CourseName.APLUS)

    def testShouldSaveExercise(self):
        exerciseName = "Testiharjoitus"
        maxSubmissions = "5"
        maxPoints = "99"
        pointToPass = "50"

        editExercisePage = EditExercisePage(self.driver, 1, 1)

        editExercisePage.setExerciseName(exerciseName)
        editExercisePage.setMaxSubmissions(maxSubmissions)
        editExercisePage.setMaxPoints(maxPoints)
        editExercisePage.setPointsToPass(pointToPass)
        editExercisePage.submit()

        self.assertTrue(editExercisePage.isSuccessfulSave())

        editExercisePage = EditExercisePage(self.driver, 1, 1)
        self.assertEqual(editExercisePage.getExerciseName(), exerciseName)
        self.assertEqual(editExercisePage.getMaxSubmissions(), maxSubmissions)
        self.assertEqual(editExercisePage.getMaxPoints(), maxPoints)
        self.assertEqual(editExercisePage.getPointsToPass(), pointToPass)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)