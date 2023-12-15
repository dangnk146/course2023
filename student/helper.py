from course.models import *
from course.helper import *
from users.models import *
from users.helper import *
from teacher.helper import *
from .helper import *

def GetMembershipStudentUser(data):
    try:
        class_membership = MembershipStudentUser.objects.get(student=data)
        if class_membership:
            return True
    except:        
        return False