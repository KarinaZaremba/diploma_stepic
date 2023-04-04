import pytest


@pytest.mark.usefixtures("set_up_mobile_products")
class TestMobileAttributes:
    def test_color_phones(self, search_page):
        search_page.add_mobile_to_cart()
        color = search_page.get_color_text()

        assert color == "Lavender", "The color should be Lavender"

    def test_case_for_mobile(self, search_page, cart_page, coverage_case_page):
        search_page.scroll_to_case()
        search_page.click_checkbox()
        coverage_case_page.choose_new_color()
        produced_by_model = coverage_case_page.get_name_case_for_model_phone()

        assert produced_by_model == "Samsung Galaxy S21 FE", f'Case has been produced for {produced_by_model}'


