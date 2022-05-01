#Importing the libraries
import pytest
import sqlite3
class GradeBook:
    '''
    Gradebook class initializes sqlite3 connection in memory. it then creates a table in the database.
    It has metohds to upload name and grade to the database created in the memory. It also has a method to
    find the grade of an student stored in the memory database.

    '''
    def __init__(self):
        """
        Returns
        -------
        None.
        Constructor takes on private parameter. It Initializes database to the memory.
        sets the cursor to private  database and creates a table as well.
        """
        con = sqlite3.connect(":memory:")
        self.__database = con.cursor()
        self.__database.execute("CREATE TABLE student_grade (name text, grade real)")

    def upload_grades(self, grades):
        '''
        Parameters
        ----------
        grades : list
            list of tuples to be uploaded in the table.

        Returns
        -------
        None.

        '''
        self.__database.executemany("INSERT INTO student_grade VALUES (?,?)", grades)

    def student_grade(self, name):
        """
        Parameters
        ----------
        name : str
            Name of the student for which grade is to be searched.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        self.__database.execute("SELECT grade FROM student_grade WHERE name = ?", (name,))
        return self.__database.fetchone()[0]




# creating the object of the GradeBook class
my_gradebook = GradeBook()
# five test data
student_grades = [("Sean", 9.7), ("Mark", 9.3), ("Jennifer", 9.5), ("Kisha", 9.6), ("Andrew", 9.8)]
#Parameterizing of a test is done to run the test against multiple sets of inputs.
@pytest.mark.parametrize("name, grade", student_grades)
def test_gradebook(name, grade):
    '''
    Parameters
    ----------
    name : string
        name of the student
    grade : float
       garde of the student.

    Returns
    -------
    None.

    It is used to test the grade of the student.
    '''
    my_gradebook.upload_grades(student_grades)
    grade_output = my_gradebook.student_grade(name)
    assert grade_output == grade
