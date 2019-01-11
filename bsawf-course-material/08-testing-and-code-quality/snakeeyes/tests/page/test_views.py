from flask import url_for


class TestPage(object):
    def test_home_page(self, client):
        """ Home page should respond with a success 200. """
        response = client.get(url_for('page.home'))
        assert response.status_code == 200

    def test_terms_page(self, client):
        """ Terms page should respond with a success 200. """
        response = client.get(url_for('page.terms'))
        assert response.status_code == 200

    def test_privacy_page(self, client):
        """ Privacy page should respond with a success 200. """
        response = client.get(url_for('page.privacy'))
        assert response.status_code == 200

    def test_faq_page_returns(self, client):
        """ FAQ page should respond with success 200 and 
        contain <title></title> tag """
        response = client.get(url_for('page.faq'))
        assert response.status_code == 200 

    def test_faq_page_title(self, client):
        """ faq page should contain a <title></title> tag """
        response = client.get(url_for('page.faq'))
        content = str(response.data)
        assert "<title>" in content