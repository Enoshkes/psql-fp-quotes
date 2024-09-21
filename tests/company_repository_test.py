from repository.company_repository import find_company_by_id


def test_company_by_id():
    company = find_company_by_id(1)
    assert company and company['id'] == 1