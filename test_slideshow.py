import pytest

from .pages.slideshow_page import SlideshowPage


class TestUserCanSlideImagesPage():

    @pytest.mark.regression_test
    def test_user_can_go_to_slideshow_page(self, browser):
        link = "http://challenge.publitas.com/qa.html"
        page = SlideshowPage(browser, link)
        page.open()
        page.should_be_images_displaying()
     