import mysql.connector
import datetime


class BloodDonorManager:

    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='M7@vQ9#Lp2!Xr8$Zn5&K',
                database='blood_db'
            )
            if self.connection.is_connected():
                print("Database is connected successfully!")
        except Exception as e:
            print(e)
# we can call it to simplify the code
    def get_object(self,id):
        try:
            cursor_obj=self.connection.cursor()
            query="""select * from donor where id = %s"""

            value=(id,)
            cursor_obj.execute(query,value)
            result=cursor_obj.fetchone()
            return result
        except Exception as e:
            print(e)


    def post(self, **kwarg):

        try:
            self.cursor_obj = self.connection.cursor()

            query = ('''insert into donor(name,blood_group,phone,city,last_donation)
                    values(%s,%s,%s,%s,%s)''')

            values = [v for v in kwarg.values()]

            self.cursor_obj.execute(query, values)
            self.connection.commit()
            print("added successfully")
        except Exception as e:
            print(e)

    def get(self):

        try:
            self.cursor_obj = self.connection.cursor()

            query = '''select * from donor'''
            self.cursor_obj.execute(query)

            result = self.cursor_obj.fetchall()

            for data in result:
                print(data)
        except Exception as e:
            print(e)

    def retrive(self, id=None):

        try:
            result=self.get_object(id=id)
            print(result)
        except Exception as e:
            print(e)


    # we can do this way also
    # def delete(self, id=None):
    #
    #     try:
    #
    #         result=self.get_object(id=id)
    #
    #         if result != None:
    #             cursor_obj=self.connection.cursor()
    #             query = """delete from donor where id=%s"""
    #             value=(id,)
    #
    #             cursor_obj.execute(query,value)
    #             self.connection.commit()
    #             print("donor deleted successfully")
    #         else:
    #             print("there is no donor in this id")
    #     except Exception as e:
    #         print(e)

    def delete(self, id=None):
        try:
            self.cursor_obj = self.connection.cursor()

            query = "DELETE FROM donor WHERE id=%s"
            value = (id,)

            self.cursor_obj.execute(query, value)
            self.connection.commit()

            if self.cursor_obj.rowcount > 0:
                print("donor deleted successfully")
            else:
                print("there is no donor with this id")

        except Exception as e:
            print(e)

    def update(self,id=None,**kwargs):

        try:
            result=self.get_object(id)

            if result!=None:
                self.cursor_obj=self.connection.cursor()
                placeholder=""
                for key in kwargs.keys():
                    placeholder+=key+"=%s,"
                placeholder=placeholder.rstrip(",")
                query=f"update donor set {placeholder} where id=%s"
                values=[v for v in kwargs.values()]
                values.append(id)
                self.cursor_obj.execute(query,values)
                self.connection.commit()
                print("updated successfully")
            else:
                print("donor details doesn't exist in data")
        except Exception as e:
            print(e)

class_object = BloodDonorManager()
# class_object.post(naame="Tony",blood_group='O+',phone='949494949449',city='kochi',last_donation=datetime.datetime.today())
class_object.get()
#class_object.retrive(5)
# class_object.delete(5)
#class_object.update(1,name='tom',city='bulgaria')