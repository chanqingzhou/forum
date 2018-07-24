from django.core.management.base import BaseCommand, CommandError
from pyp.models import *
from django.shortcuts import get_object_or_404

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        file1 = open("faculty.txt", "r")
        for f in file1:
            f=f.strip()
            if Faculty.objects.filter(faculty_text=f):
                continue
            else:
                test = Faculty(faculty_text=f)
                test.save()
                self.stdout.write(self.style.SUCCESS('added ' + f))
        lis=[['Electrical Engineering',],
            ['Civil and Environment Engineering',],
            ['Mechanical Engineering',],
            ['Biomedical Engineering',],
            ['Chemical Engineering',],
            ['Materials Science Engineering',],
            ['Mathematics and Applied Mathematics',],
            ['Statistics and Applied Statistics',],
            ['Chemistry',],
            ['Physics',],
            ['Life Sciences',],
            ['Pharmacy',],
            ['Computational Biology',],
            ['Psychology',],
            ['Geography',],
            ['History',],
            ['Japanese Studies',],
            ['Chinese Studies',],
            ['Sociology',],
            ['Philosophy',],
            ['Global Studies',],
            ['Social Work',],
            ['Political Science',],
            ['Communicatons and New Media',],
            ['School of Business', 'AC'],
            ['School Of Computing',],
            ['School of Law',]
             ]
        file2=open("module.txt","r")
        for f in file2:
            f=f.strip()
            done=False
            if Module.objects.filter(module_code=f):
                continue;
            for codes in lis:
                if f[0:2] in codes:
                    faculty=get_object_or_404(Faculty,faculty_text=codes[0])
                    faculty.module_set.create(module_text="just testing",module_code=f)
                    done =True
                    break;
            if done:
                self.stdout.write(self.style.SUCCESS('added '+ f))

            self.stdout.write(self.style.SUCCESS('Successfully closed poll'))