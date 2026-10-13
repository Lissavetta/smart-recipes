from recipes import suggest_recipes


def test_suggest_returns_top_n():
    result = suggest_recipes(["яйца", "молоко", "помидоры", "лук"], top_n=3)
    assert len(result) == 3


def test_suggest_matches_best_recipe_first():
    result = suggest_recipes(["яйца", "молоко", "помидоры", "лук"], top_n=3)
    assert result[0]["name"] == "Омлет с овощами"


def test_suggest_empty_input():
    assert suggest_recipes([]) == []


def test_suggest_ignores_unknown_products():
    assert suggest_recipes(["манго", "папайя"], top_n=3) == []


def test_score_bounds():
    result = suggest_recipes(["яйца", "молоко"], top_n=3)
    for r in result:
        assert 0 < r["score"] <= 1