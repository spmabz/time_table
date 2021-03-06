from django.test import TestCase,Client
from django.urls import reverse, resolve
from Announcements.apps import AnnouncementsConfig
from django.apps import apps
from Announcements.models import Announcements
from Courses.models import Courses
from Log_In.models import Lecturer
from Announcements.forms import AnnouncementsForm


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

        self.astd = reverse('astd', args=[1988])
        self.mk = reverse('astaff', args=[100])

    def test_stuff(self):
        response = self.client.get(self.mk)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Register/View_announcement.html')

    def test_astd_GET(self):
        response = self.client.get(self.astd)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'Register/View_announcement.html')

    def test_astd1(self):
        url = reverse('astd', args=[1988])
        self.assertEqual(url, '/login/1988/announcement')

    def test_astaff1(self):
        url = reverse('astaff', args=[1988])
        self.assertEqual(url, '/login/staff1988/announcement' )



    def test_apps(self):
        self.assertEqual(AnnouncementsConfig.name, 'Announcements')
        self.assertEqual(apps.get_app_config('Announcements').name, 'Announcements')


    def create_Announcement(self,Course_Code= 'seven',Course_Name = 'testing'):
        return Courses.objects.create(Course_Code=Course_Code,Course_Name=Course_Name)

    def test_an(self):
        w = self.create_Announcement()
        self.assertTrue(isinstance(w,Courses))
        self.assertEqual(w.__str__(),w.Course_Code)

    def create_A(self,Course_Code = Courses(Course_Code="Course_Code"),Lect_No=Lecturer(Lect_No=10)):

        return Announcements.objects.create(Course_Code=Course_Code,Lect_No=Lect_No)

    def test_a(self):
        w =self.create_A()
        self.assertTrue(isinstance(w,Announcements))
        self.assertEqual(w.__str__(),str(w.Lect_No) + ' - ' + str(w.Course_Code))



    def test_inform(self):
        w = Announcements.objects.create(Course_Code = Courses(Course_Code="Course_Code"),Lect_No=Lecturer(Lect_No=10),Title='Title',Content='Content')
        data ={'Course_Code':w.Course_Code,'Lect_No':w.Lect_No,}
        form = AnnouncementsForm(data=data)
        self.assertFalse(form.is_valid())