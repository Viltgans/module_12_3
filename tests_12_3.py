import module_12.homework_12_1.runner as runner1
import module_12.homework_12_2.runner_and_tournament as tested
import unittest

is_frozen = True

class RunnerTest(unittest.TestCase):

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test = runner1.Runner('Alice')
        for _ in range(10):
            test.walk()

        self.assertEqual(test.distance, 50)

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        test = runner1.Runner('Alice')
        for _ in range(10):
            test.run()

        self.assertEqual(test.distance, 100)

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_1 = runner1.Runner('Maria')
        test_2 = runner1.Runner('Alice')
        for _ in range(10):
            test_1.run()
            test_2.walk()
        self.assertNotEqual(test_1.distance, test_2.distance)


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    def setUp(self):
        self.runner_1 = tested.Runner('Усэйн', 10)
        self.runner_2 = tested.Runner('Андрей', 9)
        self.runner_3 = tested.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            show_result = {}
            for place, runner in result.items():
                show_result[place] = runner.name
            # print(show_result)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        self.tournament = tested.Tournament(90, self.runner_1, self.runner_3)
        self.all_results = self.tournament.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == self.runner_3.name)
        TournamentTest.all_results[1] = self.all_results

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        self.tournament = tested.Tournament(90, self.runner_2, self.runner_3)
        self.all_results = self.tournament.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == self.runner_3.name)
        TournamentTest.all_results[2] = self.all_results

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        self.tournament = tested.Tournament(90, self.runner_1, self.runner_2,  self.runner_3)
        self.all_results = self.tournament.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == self.runner_3.name)
        TournamentTest.all_results[3] = self.all_results

if __name__ == '__main__':
    unittest.main()