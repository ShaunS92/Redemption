from django.test import TestCase
import markdown

class PostViewTest(LiveServerTestCase):

    def setUp(self):

        self.client = Client()


    def test_index(self):

        # Create the post

        post = Article()

        post.title = 'My test article'

        post.text = 'This is [a test wiki page](http://127.0.0.1:8000/)'

        post.date_changed = timezone.now()

        post.save()


        # Check new article saved

        all_articles = Article.objects.all()

        self.assertEquals(len(all_articles), 1)


        # Fetch the index

        response = self.client.get('/')

        self.assertEquals(response.status_code, 200)


        # Check the article title is in the response

        self.assertTrue(article.title in response.content)


        # Check the article text is in the response

        self.assertTrue(markdown.markdown(article.text) in response.content)


        # Check the article date is in the response

        self.assertTrue(str(article.pub_date.year) in response.content)

        self.assertTrue(article.pub_date.strftime('%b') in response.content)

        self.assertTrue(str(article.pub_date.day) in response.content)


        # Check the link is marked up properly

        self.assertTrue('<a href="http://127.0.0.1:8000/">my test article</a>' in response.content)

