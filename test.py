import unittest
from datetime import datetime, timedelta
from app import app, db
from app.models import User, Post


class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User(username='Alex')
        u.set_password('Qwerty')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('Qwerty'))

    def test_avatar(self):
        u = User(username='alex', email='john@example.com')
        self.assertEqual(u.avatar(128), ('https://www.gravatar.com/avatar/d4c74594d841139328695756648b6bd6'
                                         '?d=identicon&s=128'))

    def test_author_posts(self):
        u1 = User(username='Alex', email='Alex@example.com')
        u2 = User(username='Dmitry', email='Dmitry@example.com')
        db.session.add_all([u1, u2])

        now = datetime.utcnow()
        p1 = Post(title="post from Alex", body='Example Alex', author=u1, date=now + timedelta(seconds=1))
        p2 = Post(title="post2 from Alex", body='Example2 Alex', author=u1, date=now + timedelta(seconds=20))
        p3 = Post(title="post from Dmitry", body='Example Dmitry', author=u2, date=now + timedelta(seconds=4))
        db.session.add_all([p1, p2, p3])
        db.session.commit()

        self.assertEqual(p1.author, u1)
        self.assertEqual(p3.author, u2)
        self.assertNotEqual(p3.author, u1)
        self.assertEqual(list(u1.posts), [p1, p2])

    def test_post_datecreate(self):
        u1 = User(username='Dmitry', email='Dmitry@example.com')
        db.session.add(u1)

        now = datetime.utcnow()
        p1 = Post(title="post from Alex", body='Example Alex', author=u1, date=now)
        db.session.add(p1)

        self.assertEqual(p1.date, now)
        self.assertNotEqual(p1.date, datetime.utcnow() + timedelta(seconds=1))

    def test_posts_order(self):
        u1 = User(username='Dmitry', email='Dmitry@example.com')
        db.session.add(u1)

        now = datetime.utcnow()
        p1 = Post(title="post from Alex", body='Example Alex', author=u1, date=now)
        p2 = Post(title="post from Alex2", body='Example Alex2', author=u1, date=now + timedelta(seconds=10))
        db.session.add_all([p1, p2])
        db.session.commit()
        self.assertEqual(list(Post.query.order_by(Post.date.desc())), [p2, p1])


if __name__ == '__main__':
    unittest.main(verbosity=2)