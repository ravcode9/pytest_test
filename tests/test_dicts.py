from utils.dicts import get_val

def test_get_val_key_exists():
    data = {"vcs": "mercurial"}
    result = get_val(data, "vcs")
    assert result == "mercurial"

def test_get_val_default():
    data = {"vcs": "mercurial"}
    result = get_val(data, "lol", "not_found")
    assert result == "not_found"

def test_get_val_empty_coll():
    data = {}
    result = get_val(data, "lol", "git")
    assert result == "git"

def test_get_val_default_value_empty_coll():
    data = {}
    result = get_val(data, "vcs", "bazaar")
    assert result == "bazaar"