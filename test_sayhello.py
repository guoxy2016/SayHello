import unittest

from flask import abort

from sayhello import app, db
from sayhello.models import Message


@app.route('/500')
def internal_server_error_for_test():
    abort(500)


class SayHelloTestCase(unittest.TestCase):
    def setUp(self) -> None:
        app.config.update(
            TESTING=True,
            WTF_CSRF_ENABLED=False,
            SQLALCHEMY_DATABASE_URI='sqlite:///:memory:'
        )
        db.create_all()
        self.client = app.test_client()
        self.runner = app.test_cli_runner()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()

    def test_app_exist(self):
        self.assertFalse(app is None)

    def test_app_is_testing(self):
        self.assertTrue(app.testing)

    def test_404_page(self):
        response = self.client.get('/nothing')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 404)
        self.assertIn('The requested URL was not found on the server', data)
        self.assertIn('返回主页', data)

    def test_500_page(self):
        response = self.client.get('/500')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 500)
        self.assertIn('服务器错误', data)
        self.assertIn('返回主页', data)

    def test_index_page(self):
        response = self.client.get('/')
        data = response.get_data(as_text=True)
        self.assertIn('你好', data)

    def test_create_message(self):
        response = self.client.post('/', data=dict(username='张三', body='测试用例'), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn('成功', data)
        self.assertIn('测试用例', data)

    def test_form_validation(self):
        response = self.client.post('/', data=dict(username=' ', body='测试用例'), follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertIn('这是必填的字段', data)

    def test_forge_command(self):
        result = self.runner.invoke(args=['forge'])
        self.assertIn('Done!', result.output)
        self.assertEqual(Message.query.count(), 20)

    def test_forge_command_with_count(self):
        result = self.runner.invoke(args=['forge', '--count', '50'])
        self.assertIn('Done!', result.output)
        self.assertEqual(Message.query.count(), 50)

    def test_init_db_commend(self):
        result = self.runner.invoke(args=['init-db'])
        self.assertIn('database initialized', result.output)

    def test_init_db_comment_with_drop(self):
        result = self.runner.invoke(args=['init-db', '--drop'], input='y\n')
        self.assertIn('All data well be delete, do you want to continue?', result.output)
        self.assertIn('drop all database.', result.output)
        self.assertIn('database initialized', result.output)
