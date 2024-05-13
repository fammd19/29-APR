from config import CONN, CURSOR

class Student:

    all=[]

    def __init__(self, name, degree, year_level):
        self.id=None
        self.name = name
        self.degree = degree
        self.year_level = year_level
    #ID as None as that is generated when save to db

    #Defines the output
    def __str__(self):
        return f"{self.id}{self.name} - {self.degree}"


    def save(self):
        if not self.id: #since id is only created when added to database, new students wont have an id yet

            sql = """
                INSERT INTO students (name, degree, year_level) VALUES
                (?,?,?)
            """

            CURSOR.execute(sql, (self.name, self.degree, self.year_level))
            CONN.commit()

            self.id = CURSOR.execute("SELECT last_insert_rowid() FROM students").fetchone()[0]

        #if someone calls save but actually wants to update an existing
        else:
            self.update()


    def update(self):
        sql = "UPDATE students SET name=?, degree=?, year_level=? WHERE id=?"

        CURSOR.execute(sql, (self.name, self.degree, self.year_level, self.id))
        CONN.commit()

    #Allows you to create and store an instance in one step
    @classmethod
    def create(cls, name, degree, year_level):
        student = cls (name, degree, year_level)

        student.save()

        return student

    @classmethod
    def create_table(cls):
        sql="""CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            degree TEXT NOT NULL,
            year_level INTEGER NOT NULL
            )
        """
        CURSOR.execute(sql)
        

    @classmethod
    def drop_table(cls):
        sql="""DROP TABLE IF EXISTS students"""

        CURSOR.execute(sql)


    @classmethod
    def new_from_db(cls, row):
        #this is is bscially reverse engineering the constructor (__init__)
        student = cls(row[1], row[2], row[3]) #name, degree, year_level
        student.id = row[0] #on its own row becasue we don't pass ID into init
        return student


    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM students"
        
        all_students=CURSOR.execute(sql).fetchall()

        cls.all = [cls.new_from_db(row) for row in all_students]
        return cls.all


    @classmethod
    def find_by_id(cls, id):
        sql="SELECT * FROM students WHERE id=?"

        student = CURSOR.execute(sql, (id,)).fetchone()

        return student


    @classmethod
    def find_by_name(cls, name):
        sql="SELECT * FROM students WHERE name=?"

        student = CURSOR.execute(sql, (name,)).fetchall()

        return student()

    @classmethod
    def find_or_create_by(cls, name, degree, year_level):
        find_sql = CURSOR.execute("SELECT * FROM students WHERE name=? AND degree = ? AND year_level = ?", (name, degree, year_level)).fetchone()

        student_found = None

        if find_sql:
            student_found=cls.new_from_db(find_sql)
        else:
            student_found=cls.create(name,degree,year_level)

        return student_found



