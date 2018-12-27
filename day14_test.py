import day14


def test_day14_score_lessthan10():
    R = day14.RecipeList([4, 5])
    R.cycle()
    assert len(R.recipes) == 3
    assert R.recipes == [4, 5, 9]


def test_day14_score_morethan10():
    R = day14.RecipeList([7, 8])
    R.cycle()
    assert len(R.recipes) == 4
    assert R.recipes == [7, 8, 1, 5]


def test_day14_example_two_iterations():
    R = day14.RecipeList([3, 7])
    R.cycle()
    assert len(R.recipes) == 4
    assert R.recipes == [3, 7, 1, 0]
    assert R.elf1 == 0
    assert R.elf2 == 1
    R.cycle()
    assert len(R.recipes) == 6
    assert R.recipes == [3, 7, 1, 0, 1, 0]
    assert R.elf1 == 4
    assert R.elf2 == 3


def test_day14_example_nine_iterations():
    day14.day14(9) == '5158916779'


def test_day14_example_five_recipes():
    day14.day14(5) == '0124515891'


def test_day14_example_eightteen_recipes():
    day14.day14(18) == '9251071085'
# After 5 recipes, the scores of the next ten would be 0124515891.
# After 18 recipes, the scores of the next ten would be 9251071085.
# After 2018 recipes, the scores of the next ten would be 5941429882.


def test_day14_example_2018_recipes():
    day14.day14(2018) == '5941429882'
