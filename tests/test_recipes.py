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


def test_ready_flag_true_when_all_ingredients_present():
    result = suggest_recipes(["яйца", "молоко", "помидоры", "лук"], top_n=3)
    assert result[0]["ready"] is True


def test_ready_recipes_go_first():
    # Омлет: яйца, молоко, помидоры, лук — всё есть → должен быть первым
    result = suggest_recipes(
        ["яйца", "молоко", "помидоры", "лук", "сыр", "макароны", "чеснок"],
        top_n=3,
    )
    assert result[0]["name"] == "Омлет с овощами"
    assert result[0]["ready"] is True
