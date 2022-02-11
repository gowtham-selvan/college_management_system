from rest_framework import serializers
class Staffs(serializers.Serializer):
    id = serializers.AutoField(primary_key=True)
    # admin =
    address = serializers.TextField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    

class Courses(serializers.Serializer):
    id = serializers.AutoField(primary_key=True)
    course_name = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    
 
class Subjects(serializers.Serializer):
    id =serializers.AutoField(primary_key=True)
    subject_name = serializers.CharField(max_length=255)
     
    # need to give default course
    course_id =serializers.ForeignKey(Courses)
    # staff_id =
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    
 

class Students(serializers.Serializer):
    id = serializers.AutoField(primary_key=True)
    gender = serializers.CharField(max_length=50)
    profile_pic = serializers.FileField()
    address = serializers.TextField()
    course_id = serializers.ForeignKey(Courses)

 
class Attendance(serializers.Serializer):
   
    # Subject Attendance
    id = serializers.AutoField(primary_key=True)
    subject_id = serializers.ForeignKey(Subjects)
    attendance_date = serializers.DateField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    