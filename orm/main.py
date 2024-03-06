from pony.orm import Database

from pony.orm import (Json, PrimaryKey, Required, db_session, select, desc, Set, get, Optional)

db = Database(provider="mysql",
              host='localhost',
              port=3306,
              user='root',
              password='123456',
              database='sandbox'
              )


class Info(db.Entity):
    _table_ = 'info'
    id = PrimaryKey(int, auto=True)
    key = Required(str, 50)
    name = Required(str, 30, default="未知")  # 如果是必须的话必须加默认值
    url = Optional(str, 100)
    comment = Optional(str, 50, nullable=True)


class Student(db.Entity):
    s_id = PrimaryKey(int, auto=True)
    name = Required(str)
    courses = Set("Course")

class Course(db.Entity):
    c_id = PrimaryKey(int, auto=True)
    name = Required(str)
    semester = Required(int)
    students = Set(Student)

if __name__ == '__main__':
    db.generate_mapping(create_tables=True)
    with db_session:
        p = Info.get(id=1)
        print(p.comment)
